import requests
url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'
r=requests.get(url)
json_data=r.json()
for key in json_data.keys():
    print(key + ':', json_data[key])

url = 'http://www.omdbapi.com/?t=social&apikey=8bab14d3'
r=requests.get(url)
json_data=r.json()
for key in json_data.keys():
    print(key + ':', json_data[key])
