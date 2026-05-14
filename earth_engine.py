print("ZERO WASTE AI EARTH ENGINE RUNNING")

import pandas as pd
import random
from datetime import datetime

data = {
    "site_id": [],
    "methane_flux": [],
    "risk_score": [],
    "scan_time": []
}

for i in range(20):
    data["site_id"].append(f"SITE_{i}")
    data["methane_flux"].append(random.randint(100, 2000))
    data["risk_score"].append(random.randint(1, 100))
    data["scan_time"].append(str(datetime.now()))

df = pd.DataFrame(data)

df.to_csv("live_scan.csv", index=False)

print(df.head())

print("Live scan generated successfully")