import requests
import boto3

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

local_file = "data/yellow_tripdata_2024-01.parquet"

r = requests.get(url)

with open(local_file, "wb") as f:
    f.write(r.content)

s3 = boto3.client("s3")

s3.upload_file(
    local_file,
    "abi-nyc-taxi-data-lake",
    "raw/yellow_tripdata_2024-01.parquet"
)

print("Uploaded to S3")