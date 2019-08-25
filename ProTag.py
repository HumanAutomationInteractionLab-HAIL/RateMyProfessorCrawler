import re
import os
import pandas as pd


#教授评价tag去重(测试用)
inputfile='F:/datasample/datasample.csv'
df1=pd.read_csv(inputfile)
ProTag=df1.loc[:, ['professor_name', 'tag_professor']]
#ProTag=ProTag.groupby('professor_name')
ProTag= ProTag.drop_duplicates()
ProTag=ProTag.dropna(axis=0,how='any')
print(ProTag)
pattern='(\d*)'
