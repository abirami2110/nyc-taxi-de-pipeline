# nyc-taxi-de-pipeline
NYC Taxi Data Engineering Pipeline
End-to-end local data engineering pipeline built with:

Python (ingestion)
DuckDB (warehouse)
dbt (transformations & tests)
Streamlit (dashboard)
Architecture
NYC Taxi Parquet → DuckDB (raw) → dbt (staging + mart) → Streamlit Dashboard

Data Model
raw.yellow_trips
analytics.stg_yellow_trips (view)
analytics.fact_daily_trips (table)
How to Run
Create virtual env
pip install -r requirements.txt
python src/ingest/download.py
python src/load/load_to_duckdb.py
dbt run
streamlit run app.py
Features
Modular transformations via dbt
Data tests (not_null)
Lineage graph via dbt docs
Analytical dashboard
