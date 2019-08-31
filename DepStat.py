import os
import pandas as pd

#统计学科种类和不同学科种类的评论数
def DepStat(inputfile,outputfile):
    df=pd.read_csv(inputfile)
    DepName=df['department_name']
    DepUni=DepName.unique()
    #print(DepUni)
    DepGroup=df['department_name'].value_counts()
    DepGroup.to_csv(outputfile,mode='a',header=True,index=True)