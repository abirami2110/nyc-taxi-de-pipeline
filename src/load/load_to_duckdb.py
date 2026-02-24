import duckdb
from pathlib import Path

db_path = "warehouse.duckdb"
parquet_path = Path("data/yellow_tripdata_2024-01.parquet")

con = duckdb.connect(db_path)

con.execute("create schema if not exists raw;")
con.execute("drop table if exists raw.yellow_trips;")
con.execute("""
create table raw.yellow_trips as
select * from read_parquet(?)
""", [str(parquet_path)])

count = con.execute("select count(*) from raw.yellow_trips").fetchone()[0]
print("Loaded rows:", count)
print("DB:", db_path)