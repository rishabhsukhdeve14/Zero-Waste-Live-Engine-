import pandas as pd
import datetime
import random

Current timestamp

timestamp = datetime.datetime.now()

Simulated methane data

data = {
"timestamp": [str(timestamp)],
"methane_ppb": [random.randint(1800, 2100)],
"latitude": [22.57],
"longitude": [88.36]
}

Create dataframe

df = pd.DataFrame(data)

Save CSV

df.to_csv(
"live_methane_data.csv",
mode="a",
header=False,
index=False
)

print("Satellite data updated:", timestamp)