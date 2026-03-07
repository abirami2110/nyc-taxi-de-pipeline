.PHONY: ingest load dbt_run dbt_test app all

PYTHON=.venv/bin/python

ingest:
	$(PYTHON) src/ingest/download.py

load:
	$(PYTHON) src/load/load_to_duckdb.py

dbt_run:
	cd nyc_taxi_dbt && ../.venv/bin/dbt run

dbt_test:
	cd nyc_taxi_dbt && ../.venv/bin/dbt test

app:
	$(PYTHON) -m streamlit run app.py

all: ingest load dbt_run dbt_test