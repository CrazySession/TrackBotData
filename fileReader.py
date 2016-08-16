#! python 3
# --- JSON File Reader ---

import json, requests, bs4
# deleted sys and pprint

pageNo = '&page=1'

#Downloading Data from trackobot.com API
url = 'https://trackobot.com/profile/history.json?username=dawn-nightblade-5831&token=HfGxFHW6hbK46NkBZW55&page=1' + pageNo
response = requests.get(url)
response.raise_for_status()

#Load JSON
gameStats = json.loads(response.text)


w = gameStats['history']

L = len(w)

for i in range(L):
    print(w[i]['id'] , w[i]['mode'] , w[i]['hero'], w[i]['hero_deck'], w[i]['opponent'],
      w[i]['opponent_deck'], w[i]['coin'], w[i]['result'],w[i]['rank'])


