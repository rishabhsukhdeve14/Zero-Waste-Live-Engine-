import ee
import pandas as pd
import datetime

# Initialize Earth Engine with Project ID
ee.Initialize(project='stalwart-fx-490910-e3')

# Load Sentinel-5P Methane Dataset
collection = ee.ImageCollection(
    "COPERNICUS/S5P/OFFL/L3_CH4"
).select("CH4_column_volume_mixing_ratio_dry_air")

# India region
india = ee.Geometry.Rectangle([68, 6, 97, 37])

# Get latest methane image
image = collection.filterBounds(india).sort(
    "system:time_start", False
).first()

# Calculate mean methane over India
stats = image.reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=india,
    scale=10000,
    maxPixels=1e9
)

methane = stats.getInfo()

# Timestamp
timestamp = datetime.datetime.now()

# Save data
data = {
    "timestamp": [str(timestamp)],
    "methane_data": [str(methane)]
}

df = pd.DataFrame(data)

df.to_csv(
    "india_methane_data.csv",
    mode="a",
    header=False,
    index=False
)

print("Methane data updated:", timestamp)
print(methane)