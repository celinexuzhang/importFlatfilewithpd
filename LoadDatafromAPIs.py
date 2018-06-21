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

url = 'http://www.omdbapi.com/?apikey=8bab14d3&t=Game of Thrones'
r=requests.get(url)
json_data=r.json()
for key in json_data.keys():
    print(key + ':', json_data[key])

# Assign URL to variable: url
url='http://www.omdbapi.com/?t=social+network&apikey=ff21610b'

# Package the request, send the request and catch the response: r
r = requests.get(url)
text=r.json()
# Print the text of the response
for key in text.keys():
    print(key + ':',text[key])

#Wikipedia API
#Assign the relevant URL to the variable url.
#Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
#The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string; use the function print() to print this string to the shel
# Assign URL to variable: url
url='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data=r.json()
#uery will return nested JSONs, that is, JSONs with JSONs
for key in json_data.keys():
    print(key + ':', json_data[key])
# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)