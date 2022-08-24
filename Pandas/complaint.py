import pandas as pd


data = pd.read_excel('03-November-2020.xlsx',sheet_name='Complain List')

complaints = []

for index, value in enumerate(data['REMARK']):
  if str(value) == 'YES':
    complaints.append(data['URL'][index])

frequency = {}

for url in complaints:
  handle = url.split('/')[3]
  if handle in frequency:
    frequency[handle] += 1
  else:
    frequency[handle] = 1

for key, value in frequency.items():
  if value > 2:
    print('{} : {}'.format(key,value))



