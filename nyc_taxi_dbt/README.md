Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
# NYC Taxi Data Engineering Pipeline

End-to-end local data engineering pipeline built with:

- Python (ingestion)
- DuckDB (warehouse)
- dbt (transformations & tests)
- Streamlit (dashboard)

## Architecture

NYC Taxi Parquet → DuckDB (raw) → dbt (staging + mart) → Streamlit Dashboard

## Data Model

- raw.yellow_trips
- analytics.stg_yellow_trips (view)
- analytics.fact_daily_trips (table)

## How to Run

1. Create virtual env
2. pip install -r requirements.txt
3. python src/ingest/download.py
4. python src/load/load_to_duckdb.py
5. dbt run
6. streamlit run app.py

## Features

- Modular transformations via dbt
- Data tests (not_null)
- Lineage graph via dbt docs
- Analytical dashboard
