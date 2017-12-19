# reading source code of a website page from the internet

import urllib.request

# store the url page into file object
file = urllib.request.urlopen("http://mahtabalam.website/mini.html")

# read data from file and display it
print(file.read())