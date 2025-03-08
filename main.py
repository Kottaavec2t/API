import requests
from methods import profile, error
import API_KEY

headers = {
   "Authorization": f"Bearer {API_KEY.API_KEY}",
    "Accept": "application/json"
}

tag = str(input("Enter your tag : #"))
response = requests.api.get(f"https://api.brawlstars.com/v1/players/%23{tag}", headers=headers)
if response.status_code == 200:
    data = response.json()
    image = profile(data)
    image.show()
else:
    image = error(response)
    image.show()
