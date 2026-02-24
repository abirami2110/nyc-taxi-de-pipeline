import duckdb
import pandas as pd
import streamlit as st

st.title("NYC Taxi — Mini Data Warehouse Demo")

con = duckdb.connect("warehouse.duckdb")

# Metric from raw (optional)
total = con.execute("select count(*) as trips from raw.yellow_trips").df()
st.metric("Total trips (raw)", int(total["trips"][0]))

# Query dbt mart
df = con.execute("""
select * 
from analytics.fact_daily_trips
order by trip_date
""").df()

# Charts
st.line_chart(df.set_index("trip_date")[["trips"]])
st.line_chart(df.set_index("trip_date")[["avg_distance"]])
st.line_chart(df.set_index("trip_date")[["total_revenue"]])

st.dataframe(df.tail(20))