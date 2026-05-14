from sentinelsat import SentinelAPI
from datetime import date

# LOGIN
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

api = SentinelAPI(
    username,
    password,
    'https://apihub.copernicus.eu/apihub'
)

# INDIA AREA
footprint = """
POLYGON((68 8, 68 37, 97 37, 97 8, 68 8))
"""

# SEARCH PRODUCTS
products = api.query(
    footprint,
    date=('2025-01-01', date.today()),
    platformname='Sentinel-5P'
)

print("TOTAL PRODUCTS FOUND:", len(products))

for product in list(products.items())[:5]:
    print(product)