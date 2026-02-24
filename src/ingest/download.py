from pathlib import Path
import requests

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
OUT = Path("data/yellow_tripdata_2024-01.parquet")

OUT.parent.mkdir(parents=True, exist_ok=True)

if not OUT.exists():
    with requests.get(URL, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(OUT, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

print("Saved:", OUT)