#! python 3
# --- JSON File Reader ---

import json, requests, sys, pprint

#Downloading Data from trackobot.com API
url = 'https://trackobot.com/profile/history.json?username=dawn-nightblade-5831&token=HfGxFHW6hbK46NkBZW55'
response = requests.get(url)
response.raise_for_status()

'''urlTwo = 'https://trackobot.com/profile?page=2.json?username=dawn-nightblade-5831&token=HfGxFHW6hbK46NkBZW55'
responseTwo = requests.get(urlTwo)
responseTwo.raise_for_status()'''

#Load JSON
gameStats = json.loads(response.text)
#gameStatsTwo = json.loads(responseTwo.text)


w = gameStats['history']
#e = gameStatsTwo['history']

L = len(w)

for i in range(L):
    print(w[i]['mode'] , w[i]['hero'], w[i]['hero_deck'], w[i]['opponent'],
      w[i]['opponent_deck'], w[i]['coin'], w[i]['result'],w[i]['rank'])

'''for j in range(len(e)):
    print(e[j]['mode'] , e[j]['hero'], e[j]['hero_deck'], e[j]['opponent'],
          e[j]['opponent_deck'], e[j]['coin'], e[j]['result'],e[j]['rank'])
          '''


