import os
import pandas as pd
import splittag
import numpy as np
import re

#在原csv文件中增加线下线上课程的标识符和不同tag的统计数据栏
def isonline(df):
   onlines=df['name_onlines']
   offlines=df['name_not_onlines']
   tags=['online','offline']
   df1=pd.DataFrame(np.zeros((len(df),2),dtype=np.int),columns=tags)
   for index1,value1 in enumerate(onlines):
       if not value1=='NAN':
           df1.iat[index1, 0]=1          
   for index1,value1 in enumerate(offlines):
       if not value1=='NAN':
           df1.iat[index1, 1]=1 
   for i in range(35,37):
         df.insert(i,tags[i-35],df1[tags[i-35]])

   return df

def tagadd(inputfile,outputfile):
    df1=pd.read_csv(inputfile)
    tags=['Gives good feedback','Respected','Lots of homework','Accessible outside class','Get ready to read','Participation matters',"Skip class?",'Inspirational','Graded by few things', 'Test heavy','Group projects','Clear grading criteria','Hilarious','Beaware of pop quizzes','Amazing lectures','Lecture heavy','Caring','Extra credit','So many papers','Tough grader']
    ProTagName=['pro_feedback','pro_respected','pro_homework','pro_accessible','pro_ready','pro_participation','pro_skip','pro_inspirational','pro_graded','pro_teheavy','pro_group','pro_criteria','pro_hilarious','pro_quizzes','pro_amazing','pro_leheavy','pro_caring','pro_credit','pro_papers','pro_tough']    
    StuTagName=['stu_feedback','stu_respected','stu_homework','stu_accessible','stu_ready','stu_participation','stu_skip','stu_inspirational','stu_graded','stu_teheavy','stu_group','stu_criteria','stu_hilarious','stu_quizzes','stu_amazing','stu_leheavy','stu_caring','stu_credit','stu_papers','stu_tough']
    protags=df1['tag_professor']
    stutags=df1['stu_tags']
    df2=pd.DataFrame(np.zeros((len(df1),len(ProTagName)),dtype=np.int),columns=ProTagName)
    df3=pd.DataFrame(np.zeros((len(df1),len(StuTagName)),dtype=np.int),columns=StuTagName)
    for index1,value1 in enumerate(protags):
        if pd.isna(value1):
            continue
        templist,tempnumber=splittag.splittag(value1)
        for index2,value2 in enumerate(templist):
            for index3,value3 in enumerate(tags):
                if re.search(value3,value2,re.I)!=None:
                    df2.iat[index1, index3] = tempnumber[index2]

    for i in range(10,30):
        df1.insert(i,ProTagName[i-10],df2[ProTagName[i-10]])


    for index1,tag1 in enumerate(stutags):
        for index2,tag2 in enumerate(tags):
            if pd.isna(tag1):
                continue
            if re.search(tag2,tag1,re.I)!=None:
                df3.iat[index1, index2] =1
    for i in range(41,61):
         df1.insert(i,StuTagName[i-41],df3[StuTagName[i-41]])

    df1=isonline(df1)
    df1.to_csv(outputfile,index=False)
    return