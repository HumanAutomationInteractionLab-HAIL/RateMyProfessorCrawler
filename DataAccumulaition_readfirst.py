import pandas as pd
import os
import numpy as np

dir1="F:/文档/临时代码/data/Extract_RateMyProfessor2"
filename='Extract_RateMyProfessor2'
dir2="F:/文档/临时代码/output_version2"
dir=os.listdir(dir1)
k=1
m=1
df=pd.read_csv(dir1+'/'+dir[0])
for inputfile in dir[1:]:
    while k%1000==0:
        df.to_csv(dir2+'/'+filename+'/'+str(m)+'.csv',index=None)
        print(m)
        m=m+1
        df=pd.read_csv(dir1+'/'+inputfile)
        k=k+1
    else:
        tempdf=pd.read_csv(dir1+'/'+inputfile)
        df=pd.concat([df,tempdf])
        k=k+1


    
