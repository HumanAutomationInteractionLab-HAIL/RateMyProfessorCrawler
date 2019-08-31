import os 
import pandas as pd
import numpy as np
import tagadd

#dir1="F:/文档/临时代码/data/Extract_RateMyProfessor"
#dir2="F:/文档/临时代码/output/Extract_RateMyProfessor"
#for i in range(1,5):
#    inputfile_dir=dir1+str(i)
#    outputfile_dir=dir2+str(i)
#    dir=os.listdir(inputfile_dir)
#    for inputfile in dir:
#        outputfile = outputfile_dir + '/' + inputfile
#        print(outputfile)
#        tagadd.tagadd(inputfile_dir + '/' + inputfile,outputfile)

inputfile='F:/文档/临时代码/final/RMPData.csv'
outputfile='F:/文档/临时代码/final/RMPData_Tagadd.csv'
tagadd.tagadd(inputfile,outputfile)