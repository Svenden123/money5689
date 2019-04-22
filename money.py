import json
import urllib.request

page = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
data = json.loads(page.read())
valutes = data['Valute']


maxVal = 0
maxValName = ''
for name in valutes:
    if valutes[name]['Value'] > maxVal:
        maxVal = valutes[name]['Value']
        maxValName = valutes[name]['Name']
print(maxValName)
