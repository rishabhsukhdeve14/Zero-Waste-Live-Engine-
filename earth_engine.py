import ee
import pandas as pd
import datetime

Initialize Earth Engine

ee.Initialize(project='stalwart-fx-490910-e3')

India region

india = ee.Geometry.Rectangle([68, 6, 97, 37])

Sentinel-5P methane dataset

collection = (
ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_CH4")
.select("CH4_column_volume_mixing_ratio_dry_air")
.filterBounds(india)
.sort("system:time_start", False)
)

Latest image

image = collection.first()

Methane extraction

stats = image.reduceRegion(
reducer=ee.Reducer.mean(),
geometry=india,
scale=10000,
maxPixels=1e9
)

methane_value = stats.getInfo()

timestamp = datetime.datetime.now()

data = {
"timestamp": [str(timestamp)],
"methane_ppb": [
methane_value["CH4_column_volume_mixing_ratio_dry_air"]
],
"latitude": [22.57],
"longitude": [88.36],
"satellite": ["Sentinel-5P"]
}

df = pd.DataFrame(data)

df.to_csv(
"live_methane_data.csv",
mode="a",
header=False,
index=False
)

print("Methane updated:", timestamp)
print(data)