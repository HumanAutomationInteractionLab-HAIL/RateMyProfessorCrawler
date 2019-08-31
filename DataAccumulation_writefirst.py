import pandas as pd
import os
import numpy as np

dir1="F:/文档/临时代码/output_version2/final"
filename='final'
dir2="F:/文档/临时代码/output_version2"
dir=os.listdir(dir1)
df=pd.read_csv(dir1+'/'+dir[0])
df.to_csv(dir2+'/'+'final.csv',index=None)
for inputfile in dir[1:]:
    df=pd.read_csv(dir1+'/'+inputfile)
    df.to_csv(dir2+'/'+'final.csv',mode='a',header=None,index=None)
    print(inputfile)

    
