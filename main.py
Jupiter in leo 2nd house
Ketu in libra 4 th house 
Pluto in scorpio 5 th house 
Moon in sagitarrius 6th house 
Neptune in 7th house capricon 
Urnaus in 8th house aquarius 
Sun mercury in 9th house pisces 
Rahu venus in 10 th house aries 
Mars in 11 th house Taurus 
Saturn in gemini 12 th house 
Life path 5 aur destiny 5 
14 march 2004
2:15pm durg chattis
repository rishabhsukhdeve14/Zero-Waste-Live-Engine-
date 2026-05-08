import requests
import datetime

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

data = requests.get(url).json()

timestamp = datetime.datetime.now()

print("Data fetched at:", timestamp)
print(data)

with open("data.txt", "a") as f:
    f.write(f"{timestamp} - {data}\n")