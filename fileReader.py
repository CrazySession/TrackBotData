#! python 3
# --- JSON File Reader ---

import json, requests, bs4, os

#init Var for pageNo
no = 1

#Change Dir to Save Folder / Create Save Folder
currentDir = os.getcwd()

try:
    os.chdir(currentDir+'\\Saves')
except FileNotFoundError:
    os.makedirs('.\\Saves')
    os.chdir(currentDir+'\\Saves')

#Downloading Data from trackobot.com API
while True:
    pageNo = '&page=' + str(no)
    url = 'https://trackobot.com/profile/history.json?username=dawn-nightblade-5831&token=HfGxFHW6hbK46NkBZW55' + pageNo
    response = requests.get(url)
    response.raise_for_status()

    #Load JSON
    gameStats = json.loads(response.text)
    
    #Load / Create Excel Spreadsheet --- necessary in while loop cause if not same month! ------ except FileNotFoundError:

    #Load / Create Sheet ---- necessary in while loop cause if not same day!

    #Write JSON to Excel Spreadsheet
    w = gameStats['history']

    L = len(w)

    for i in range(L):
        print(w[i]['id'] , w[i]['mode'] , w[i]['hero'], w[i]['hero_deck'], w[i]['opponent'],
          w[i]['opponent_deck'], w[i]['coin'], w[i]['result'],w[i]['rank'],w[i]['added'])

    no +=1

    checkURL = 'https://trackobot.com/profile/history?username=dawn-nightblade-5831&token=HfGxFHW6hbK46NkBZW55' + pageNo
    res = requests.get(checkURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text , "html.parser")
    elems = soup.select('div p')
    
    try:
        if 'No results uploaded yet' in elems[0].getText():
            print('Jobs done!')
            break
    except IndexError:
        print('next page')
        continue
    
