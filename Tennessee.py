import timeit
import requests
import json

startTime = timeit.default_timer()

# list containing each response from Google Map's API
r = [0] * 100
# iterators
i = 0
j = 0
# comma separated list to hold lat, lng values
csl = []
counter = 0


def get_coordinates():
    string = "http://maps.googleapis.com/maps/api/geocode/json?address=" + str(counter)
    requestLine = requests.get(string)
    list = (requestLine.json()['results'])
    i = 0
    j = 0
    for y in range(len(list)):
        comparator = requestLine.json()['results'][j]['formatted_address']
        if 'Tennessee' in comparator:
            lat = (requestLine.json()['results'][j]['geometry']['bounds']['northeast']['lat'])
            lng = (requestLine.json()['results'][j]['geometry']['bounds']['northeast']['lng'])
            entry = comparator + ': ' + str(lat) + ',' + str(lng)
            csl.append(entry)

        j += 1
    i += 1
    j = 0


for x in range(100):
    string = "http://maps.googleapis.com/maps/api/geocode/json?address=" + str(x)
    r[x] = requests.get(string)

for x in r:

    list = (r[i].json()['results'])
    for y in range(len(list)):
        comparator = r[i].json()['results'][j]['formatted_address']
        if 'Tennessee' in comparator:
            lat = (r[i].json()['results'][j]['geometry']['bounds']['northeast']['lat'])
            lng = (r[i].json()['results'][j]['geometry']['bounds']['northeast']['lng'])
            entry = comparator + ': ' + str(lat) + ',' + str(lng)
            csl.append(entry)

        j += 1
    i += 1
    j = 0

print(csl)
print(len(csl))

# Test code for if Tennesee is found in each request

# comparator = r[0].json()['results'][0]['formatted_address']
# if 'Tennessee' in comparator:
#     print('Mission accomplished')
# else:
#     print('Try again')
#
#
# print(type(r[0].json()['results']))
# list = (r[0].json()['results'])
# print(len(list))

# Test code for getting coordinates and adding the to list

# print(r[11].json()['results'][1]['formatted_address'])
# print(type(r[11].json()['results'][1]['formatted_address']))
# print(r[11].json()['results'][1]['geometry']['bounds']['northeast']['lat'])
# print(r[11].json()['results'][1]['geometry']['bounds']['northeast']['lng'])
# lat = (r[11].json()['results'][1]['geometry']['bounds']['northeast']['lat'])
# lng = (r[11].json()['results'][1]['geometry']['bounds']['northeast']['lng'])
# entry = str(lat) + ',' + str(lng)
# print(entry)
# csl.append(entry)
# print(csl)

endTime = timeit.default_timer()
print(endTime - startTime)
