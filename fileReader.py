#! python 3
# --- JSON File Reader ---

import json, requests, bs4, os, openpyxl, xlsxwriter

#init Var for pageNo
no = 1

Aug = 'August' # temp Var for 2.3

rowA = 1
rowB = 1
rowC = 1

#1.0Change Dir to Save Folder / Create Save Folder
currentDir = os.getcwd()

try:
    os.chdir(currentDir+'\\Saves')
except FileNotFoundError:
    os.makedirs('.\\Saves')
    os.chdir(currentDir+'\\Saves')

#2.0Downloading Data from trackobot.com API
while True:
    pageNo = '&page=' + str(no)
    url = 'https://trackobot.com/profile/history.json?username=dawn-nightblade-5831&token=HfGxFHW6hbK46NkBZW55' + pageNo
    response = requests.get(url)
    response.raise_for_status()

    #2.1Load JSON
    gameStats = json.loads(response.text)
    
    #2.2Load / Create Excel Spreadsheet --- necessary in while loop cause if not same month! ------ except FileNotFoundError:
    try:
        wb = openpyxl.load_workbook('August_2016.xlsx')
    except FileNotFoundError:
        workbook = xlsxwriter.Workbook('August_2016.xlsx')
        worksheet = workbook.add_worksheet()
        workbook.close()
        wb = openpyxl.load_workbook('August_2016.xlsx')

    #2.3Load / Create Sheet ---- necessary in while loop cause if not same day!
    Sheet = wb.get_active_sheet()
    title = Sheet.title

    if title != Aug:
        wb.create_sheet(index=0, title = Aug)
        wb.save('August_2016.xlsx')
            

    #2.4Write JSON to Excel Spreadsheet
    w = gameStats['history']

    L = len(w)

    wb = openpyxl.load_workbook('August_2016.xlsx')
    sheet = wb.get_sheet_by_name(Aug)

    #iterate through dictionary

    for i in range(L):
        sheet['A'+str(rowA)] = w[i]['id']
        rowA += 1          
        #print(row)

    for i in range(L):
        sheet['B'+str(rowB)] = w[i]['mode']
        rowB += 1
        #print(row)

    for i in range(L):
        sheet['C'+str(rowC)] = w[i]['hero']
        rowC += 1 
        #print(row)
    
    wb.save('August_2016.xlsx')

    #Set rows to first empty row
    highestRow = sheet.get_highest_row()
    highestRow +=1

    rowA = highestRow
    rowB = highestRow
    rowC = highestRow

    '''
    for i in range(L):
        print(w[i]['id'] , w[i]['mode'] , w[i]['hero'], w[i]['hero_deck'], w[i]['opponent'],
          w[i]['opponent_deck'], w[i]['coin'], w[i]['result'],w[i]['rank'],w[i]['added'])
    '''
    #Iterate the page count to check for next page on trackbot
    no +=1

    #2.5Check next page if there is more content to dl otherwise stop searching
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
    
