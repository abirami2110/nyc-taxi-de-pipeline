**NYC Taxi Data Engineering Pipeline**

End-to-end Data Engineering pipeline demonstrating modern analytics engineering practices using Python, DuckDB, dbt, orchestration, and CI.

The project ingests raw NYC Taxi trip data, processes it through a warehouse layer, applies modular transformations using dbt, and exposes analytical insights via a Streamlit dashboard.

This repository demonstrates key data engineering concepts used in production pipelines including:

- ELT data architecture

- Warehouse modelling

- Incremental transformations

- Data quality testing

- Workflow orchestration

- CI/CD automation

**Architecture**

Raw Dataset
    ↓
Python Ingestion Pipeline
    ↓
DuckDB Analytical Warehouse
    ↓
dbt Transformation Layer (Staging → Marts)
    ↓
Streamlit Analytics Dashboard

**Pipeline flow:**

NYC Taxi Parquet
      ↓
DuckDB Raw Tables
      ↓
dbt Staging Models
      ↓
dbt Mart Tables
      ↓
Dashboard
**Tech Stack**
**Core Languages**

- Python
- SQL
  
**Data Engineering Tools**
  
- DuckDB — analytical warehouse
- dbt — transformation modelling & testing
- Prefect — pipeline orchestration
- GitHub Actions — CI/CD automation

**Visualization**

- Streamlit — interactive dashboard

**Development**

- Git — version control
- Makefile — pipeline automation
  
**Project Structure**

nyc-taxi-de-pipeline
│
├── data
│   └── raw parquet datasets
│
├── src
│   ├── ingest
│   │   └── download.py
│   │
│   ├── load
│   │   └── load_to_duckdb.py
│   │
│   └── orchestration
│       └── flow.py
│
├── nyc_taxi_dbt
│   ├── models
│   │   ├── staging
│   │   └── marts
│   │
│   ├── tests
│   └── dbt_project.yml
│
├── app.py
├── Makefile
└── README.md

**Data Pipeline Components**

**1. Data Ingestion**

src/ingest/download.py

Downloads the NYC Taxi dataset and stores it as Parquet files.

Why Parquet?

- Columnar storage
- Highly compressed
- Optimized for analytical queries

Example output:

data/yellow_tripdata_2024-01.parquet

**2. Data Warehouse**

Warehouse engine:

**DuckDB**

DuckDB is an embedded analytical database designed for high-performance OLAP workloads.

Benefits:

- Extremely fast for analytical queries
- No external database server required
- Native support for Parquet
- Ideal for local analytics pipelines

Loading script:

src/load/load_to_duckdb.py

This script:

1. Reads the Parquet dataset
2. Creates schema raw
3. Loads the dataset into DuckDB

Output table:

raw.yellow_trips

**3. Transformation Layer (dbt)**

Transformations are handled using dbt (Data Build Tool).

dbt enables modular SQL transformations with version control and testing.

Key advantages:

- Version-controlled transformations
- Dependency management
- Automated data testing
- Built-in data lineage
- Staging Layer

**Model:**

analytics.stg_yellow_trips

**Purpose:**

- Clean raw dataset
- Standardize column names
- Apply base transformations

**Mart Layer**

**Model:**

analytics.fact_daily_trips

Aggregated metrics:

- Daily trip counts
- Average trip distance
- Total trip revenue

This model uses incremental processing to improve performance when datasets grow.

Additional Fact Table
analytics.fact_trips

Provides trip-level normalized records for deeper analytical exploration.

Data Quality Tests

**dbt tests implemented:**

not_null

unique

**These tests ensure:**

- Primary keys are valid
- No missing critical fields
- Dataset integrity

**Run tests:**

dbt test
Data Lineage

dbt automatically generates data lineage documentation.

**Generate docs:**

dbt docs generate
dbt docs serve

**Example lineage:**

raw.yellow_trips
      ↓
stg_yellow_trips
      ↓
fact_daily_trips

This enables full traceability of transformations.

Analytics Dashboard

**Visualization tool:**

Streamlit

**Application file:**

app.py

Dashboard provides insights such as:

Daily trip volumes

Average trip distance

Revenue trends

Aggregated trip metrics

**Run locally:**

streamlit run app.py
Pipeline Automation

The project includes a Makefile for easy pipeline execution.

Run the full pipeline:

make all

**Individual steps:**

make ingest
make load
make dbt_run
make dbt_test
make app
Workflow Orchestration

Pipeline orchestration is implemented using Prefect.

**Pipeline tasks:**

download → load → dbt run → dbt test

Orchestration script:

src/orchestration/flow.py

**Run orchestrated pipeline:**

python src/orchestration/flow.py
Continuous Integration

GitHub Actions pipeline automatically runs:

Python linting

dbt compilation

unit tests

This ensures pipeline integrity before merging code changes.

Example Analytical Insights

The processed dataset enables analysis such as:

- Trip demand patterns
- Daily revenue trends
- Travel distance behaviour
- Time-series mobility insights

**Future Improvements**

**Possible production upgrades:**

- Store raw data in AWS S3
- Replace DuckDB with Redshift or Snowflake
- Schedule pipeline using Airflow
- Deploy dashboard publicly
- Add data observability checks

Author

Abirami Ramamoorthy
London, United Kingdom

**Data & Analytics Engineer specializing in:**

data pipelines

analytics engineering

cloud data platforms
