import ee
import pandas as pd
from datetime import datetime

ee.Initialize(project='YOUR_PROJECT_ID')

# master landfill file
df = pd.read_csv("master_landfills.csv")

dataset = ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_CH4") \
    .select("CH4_column_volume_mixing_ratio_dry_air") \
    .sort("system:time_start", False)

latest = dataset.first()

results = []

for index, row in df.iterrows():

    point = ee.Geometry.Point([row['lon'], row['lat']])

    value = latest.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point,
        scale=1000
    ).get("CH4_column_volume_mixing_ratio_dry_air")

    try:
        methane = ee.Number(value).getInfo()

        results.append([
            datetime.utcnow(),
            row['id'],
            row['state'],
            row['city'],
            row['lat'],
            row['lon'],
            methane,
            "Sentinel-5P"
        ])

    except:
        pass

out = pd.DataFrame(results)

out.to_csv(
    "live_methane_data.csv",
    mode="a",
    header=False,
    index=False
)

print("DONE")