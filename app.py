import duckdb
import pandas as pd
import streamlit as st

st.title("NYC Taxi — Mini Data Warehouse Demo")

con = duckdb.connect("warehouse.duckdb")

total = con.execute("select count(*) as trips from raw.yellow_trips").df()
st.metric("Total trips (raw)", int(total["trips"][0]))

df = con.execute("""
select
  date_trunc('day', tpep_pickup_datetime) as day,
  count(*) as trips,
  avg(trip_distance) as avg_distance
from raw.yellow_trips
group by 1
order by 1
""").df()

st.line_chart(df.set_index("day")[["trips"]])
st.line_chart(df.set_index("day")[["avg_distance"]])

st.dataframe(df.tail(20))