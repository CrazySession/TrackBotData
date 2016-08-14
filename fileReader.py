# --- CSV File Reader ---

import csv

dailyFile = open('E:/PythonProjects/TrackBotData/CSV_Files/14_08_2016.csv')
fileReader = csv.reader(dailyFile)
dailyData = list(fileReader)

print(dailyData)
