import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input("Enter the location name: ")
    if address == "quit" or address == "q":
        break
    url = main_api + urllib.parse.urlencode({'address': address})
    print(url)
    json_data = requests.get(url).json()
    print()
    json_status = json_data['status']
    print("Api Staus = ", json_status)
    print()
    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])
        print()
        formatted_add = json_data['results'][0]['formatted_address']
        print(formatted_add)
