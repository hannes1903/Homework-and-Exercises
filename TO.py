
#for countdown in 5, 4, 3, 2, 1, "hey!":
 #   print(countdown)

#cliches = [
#        "At the end of the day",
#       "Having said that",
#       "The fact of the matter is",
#       "Be that as it may",
#       "The bottom line is",
#       "If you will",
#      ]
#print(cliches[3])

#LIST []

#quotes = {
 #       "Moe": "A wise guy, huh?",
 #       "Larry": "Ow!",
 #       "Curly": "Nyuk nyuk!",
 #        }
#stooge = "Curly"

# print(stooge, "says:", quotes[stooge])

# DICTONARY {}


import json
from urllib.request import urlopen
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])
