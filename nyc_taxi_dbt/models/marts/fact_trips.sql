{{ config(materialized='table') }}

select
    date_trunc('day', tpep_pickup_datetime) as trip_date,
    count(*) as total_trips,
    avg(trip_distance) as avg_trip_distance,
    sum(total_amount) as total_revenue
from {{ ref('stg_yellow_trips') }}
group by 1