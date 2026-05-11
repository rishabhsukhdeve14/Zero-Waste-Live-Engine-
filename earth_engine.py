import pandas as pd
from datetime import datetime

df = pd.read_csv("master_landfills.csv")

results = []

for index, row in df.head(100).iterrows():

    results.append([
        datetime.utcnow(),
        row['id'],
        row['state'],
        row['city'],
        row['lat'],
        row['lon'],
        1900 + index,
        "Simulated-Live"
    ])

out = pd.DataFrame(results)

out.to_csv(
    "live_methane_data.csv",
    mode="a",
    header=False,
    index=False
)

print("DONE")