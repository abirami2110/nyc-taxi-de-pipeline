from pathlib import Path
from prefect import flow, task
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
DBT = REPO_ROOT / ".venv" / "bin" / "dbt"

def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)

@task
def ingest():
    run([str(PYTHON), "src/ingest/download.py"], cwd=REPO_ROOT)

@task
def load():
    run([str(PYTHON), "src/load/load_to_duckdb.py"], cwd=REPO_ROOT)

@task
def dbt_run():
    run([str(DBT), "run"], cwd=REPO_ROOT / "nyc_taxi_dbt")

@task
def dbt_test():
    run([str(DBT), "test"], cwd=REPO_ROOT / "nyc_taxi_dbt")

@flow(name="nyc_taxi_pipeline")
def nyc_taxi_pipeline():
    ingest()
    load()
    dbt_run()
    dbt_test()

if __name__ == "__main__":
    nyc_taxi_pipeline()