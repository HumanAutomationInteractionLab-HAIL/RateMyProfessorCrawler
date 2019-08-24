import os
import pandas as pd

def DepStat(inputfile,outputfile):
    df=pd.read_csv(inputfile)
    DepName=df['department_name']
    DepUni=DepName.unique()
    #print(DepUni)
    DepGroup=df['department_name'].value_counts()
    DepGroup=DepGroup.append(temp)
    print(DepGroup)
    DepGroup.to_csv(outputfile,header=True)