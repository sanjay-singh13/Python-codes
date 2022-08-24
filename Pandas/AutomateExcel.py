import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'shift-data.xlsx'
excel_file_2 = 'third-shift-data.xlsx'

df_first_shift = pd.read_excel(excel_file_1,sheet_name='first')
df_second_shift = pd.read_excel(excel_file_1,sheet_name='second')
df_third_shift = pd.read_excel(excel_file_2)

# print(df_first_shift['Name'])
#merge sheets into one sheet
all_data = pd.concat([df_first_shift,df_second_shift,df_third_shift])
mean_all_data = all_data.groupby(['Name']).mean()
person_productivity = mean_all_data.loc[:,'Production Run Time (Min)':'Products Produced (Units)']
# print(person_productivity.groupby(['Name']).max())

person_productivity.plot(kind='bar')
plt.show()

all_data.to_excel('output.xlsx')
