# A python program to retrieve different parts of a url
import urllib.parse

url = 'http://mahtabalam.website/mini.html'
tpl = urllib.parse.urlparse (url)
print (tpl)  # display the content of the tuple

# display the diffrent parts of url
print ("scheme: ", tpl.scheme)
print ("Netloc: ", tpl.netloc)
print ("Path: ", tpl.path)
print ("Params: ", tpl.params)
print ("Query: ", tpl.query)
print ("Fragment: ", tpl.fragment)

# scheme: Gives the protocol name used in the url
# netloc: Gives the website name on the net with port number if present
# path: gives the path of the webpage

