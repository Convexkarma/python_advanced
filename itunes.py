import requests
import sys

if len (sys.argv) < 2:
    print ("Too little arguments")
    sys.exit()

print( requests.get ("https://itunes.apple.com/entity=song&limit=1&term=" + sys.argv[1]))

