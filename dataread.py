import pandas as pd
import os


#读入csv数据，并写入到同一csv文件中(数据样例用)
inputfile_dir='F:/datasample'
outputfile='datasample.csv'
dir=os.listdir(inputfile_dir)
df=pd.read_csv(inputfile_dir+'/'+dir[0])
df.to_csv(inputfile_dir+'/'+outputfile,mode='a',index=False)
for inputfile in dir[1:]:
    print(inputfile_dir+'/'+inputfile)
    df=pd.read_csv(inputfile_dir+'/'+inputfile)
    df.to_csv(inputfile_dir+'/'+outputfile,mode='a',header=None,index=False)
