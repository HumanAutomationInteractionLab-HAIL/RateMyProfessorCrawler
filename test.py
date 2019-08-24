import pandas as pd
 
tags=['Gives good feedback','Respected','Lots of homework','Accessible outside class','Get ready to read','Participation matters','Skip class? You won\'t pass. ','Inspirational','Graded by few things', 'This heavy','Group projects','Clear grading criteria','Hilarious','Beaware of pop quizzes','Amazing lectures','Lecture heavy','Caring','Extra credit','So many papers','Tough grader']
ProTagName=['pro_feedback','pro_respected','pro_homework','pro_accessible','pro_ready','pro_participation','pro_skip','pro_inspirational','pro_graded','pro_teheavy','pro_group','pro_criteria','pro_hilarious','pro_quizzes','pro_amazing','pro_leheavy','pro_caring','pro_credit','pro_papers','pro_tough']    
StuTagName=['stu_feedback','stu_respected','stu_homework','stu_accessible','stu_ready','stu_participation','stu_skip','stu_inspirational','stu_graded','stu_teheavy','stu_group','stu_criteria','stu_hilarious','stu_quizzes','stu_amazing','stu_leheavy','stu_caring','stu_credit','stu_papers','stu_tough']
outputfile="F:/testsample/test.csv"
df=pd.DataFrame(tags)
df1=pd.DataFrame(ProTagName)
df2=pd.DataFrame(StuTagName)
df.to_csv(outputfile,mode='a',header=None,index=False)
df1.to_csv(outputfile,mode='a',header=None,index=False)
df2.to_csv(outputfile,mode='a',header=None,index=False)