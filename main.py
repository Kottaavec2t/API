import requests
from methods import profile, error

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImE5OGNkNDljLWJjOTAtNGM5YS04ZWM5LTcxZjQ5MmVhZjgwZiIsImlhdCI6MTc0MTAyNDEyOSwic3ViIjoiZGV2ZWxvcGVyLzkxY2JiZDI3LWE1MDktZmNjZC01OGM1LTYyODI0MzRjMTFhZiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc2LjE5MS4yMDEuODkiXSwidHlwZSI6ImNsaWVudCJ9XX0.pfsB4jwooLcnb2wwjhaRS_NqAx-CKgbJRhZLQMEGC_kjtA9yF86lWEFidUD80QPBKmVspCedxB6jApsJczmDUg"

headers = {
   "Authorization": f"Bearer {API_KEY}",
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
