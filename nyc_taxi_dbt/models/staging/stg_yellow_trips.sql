{{ config(materialized='view') }}

select
  VendorID as vendor_id,
  tpep_pickup_datetime as pickup_ts,
  tpep_dropoff_datetime as dropoff_ts,
  passenger_count,
  trip_distance,
  fare_amount,
  total_amount,
  payment_type,
  PULocationID as pu_location_id,
  DOLocationID as do_location_id
from raw.yellow_trips