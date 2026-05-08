import requests
import datetime

url = "https://jsonplaceholder.typicode.com/todos/1"

data = requests.get(url).json()

timestamp = datetime.datetime.now()

print("Data fetched at:", timestamp)
print(data)

with open("data.txt", "a") as f:
    f.write(f"{timestamp} - {data}\n")