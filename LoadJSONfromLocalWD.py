import json

#since json file is a flat file, thus, no need to use 'rb', can use 'r'
#note: you can have a json file as a 'list', JSON is built on two structures:1- A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.2- An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence
metrics_file= open('C:/Users/celin/OneDrive/Desktop/Learning/KaggleCompete/ZillowEconomicsData/zecon/all_available_metrics.json', 'r')
metrics_data = json.load(metrics_file)
print(type(metrics_data))

field_file= open('C:/Users/celin/OneDrive/Desktop/Learning/KaggleCompete/ZillowEconomicsData/zecon/fields_per_level.json')
field_data=json.load(field_file)
print(type(field_data))

#Use a for loop to print all key-value pairs in the dictionary json_data.
for key, value in field_data.items():
    print(key+':', value)

#you can access a value in a dictionary using the syntax: dictionary[key].
for key in field_data.keys():
    print(key + ':', field_data[key])
