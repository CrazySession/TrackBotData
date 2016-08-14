#! python 3
# --- JSON File Reader ---

import json, requests, sys, pprint

#Downloading Data from trackobot.com API
url = 'https://trackobot.com/profile/history.json?username=dawn-nightblade-5831&token=HfGxFHW6hbK46NkBZW55'
response = requests.get(url)
response.raise_for_status()

#Load JSON
gameStats = json.loads(response.text)


print(gameStats)


