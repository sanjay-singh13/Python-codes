import pandas as pd


# url = 'https://twitter.com/Jagdish56858/status/1323654971745685507'

# handle = url.split('/')[3]
# print(handle)

data = pd.read_excel('03-November-2020.xlsx',sheet_name='Complain List')
url_data = list(data[data.columns[2]])[2:]

complaint_data = data[data.columns[2,4]]

handles = []
for url in url_data:
  if 'https' in str(url):
    handle = url.split('/')[3]
    handles.append(handle)

# df_handles = pd.DataFrame(handles).groupby([0]).max()
# print(df_handles)

freq = {}

for item in handles:
  if item in freq:
    freq[item] += 1 
  else:
    freq[item] = 1

for key, value in freq.items():
  if value > 1:
    # print('{} : {}'.format(key,value))
    for url in url_data:
      if key in str(url):
        print('{} : {}'.format(key,url))


