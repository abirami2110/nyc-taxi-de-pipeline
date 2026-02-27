{{ config(
    materialized='incremental',
    unique_key='trip_date'
) }}

with daily as (
    select
      date_trunc('day', pickup_ts) as trip_date,
      count(*) as trips,
      avg(trip_distance) as avg_distance,
      sum(total_amount) as total_revenue
    from {{ ref('stg_yellow_trips') }}

    {% if is_incremental() %}
      -- only process days newer than what's already in the table
      where date_trunc('day', pickup_ts) > (select max(trip_date) from {{ this }})
    {% endif %}

    group by 1
)

select * from daily