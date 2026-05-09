import datetime

print("Earth Engine Automation Started")

timestamp = datetime.datetime.now()

with open("live_data.txt", "a") as f:
    f.write(f"Updated at: {timestamp}\n")

print("Data Updated Successfully")