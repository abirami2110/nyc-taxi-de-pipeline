{{ config(materialized='table') }}

select
  date_trunc('day', pickup_ts) as trip_date,
  count(*) as trips,
  avg(trip_distance) as avg_distance,
  sum(total_amount) as total_revenue
from {{ ref('stg_yellow_trips') }}
group by 1
order by 1