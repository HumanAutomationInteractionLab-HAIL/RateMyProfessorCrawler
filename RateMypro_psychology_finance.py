#从数据集文件夹3-4中提取心理学教授信息，并将教授信息补全.文件夹3提取到第202060文件.最后筛选了4903条数据
#从数据集文件夹3-4提取金融专业教授信息，金融学院 Finance 文件夹3提取到64857。 最后筛选出3211条数据
#
import pandas as pd
import os
src='K:\RateMyProfessor3'
filelist = os.listdir(src)


num = 193
for i in range(1,len(filelist)):
    newsrc =src +'\\'+ filelist[i]
    df = pd.read_csv(newsrc)
    try:
        if 'Finance' in df['department_name'][0]:
            print(df['department_name'][0],'第'+str(num)+'文件','文件地址：'+ newsrc)
            num += 1
            # 填充信息
            df.professor_name.ffill(inplace=True)
            df.school_name.ffill(inplace=True)
            df.department_name.ffill(inplace=True)
            df.local_name.ffill(inplace=True)
            df.state_name.ffill(inplace=True)
            df.star_rating.ffill(inplace=True)
            df.take_again.ffill(inplace=True)
            df.diff_index.ffill(inplace=True)
            df.tag_professor.ffill(inplace=True)
            df.num_student.ffill(inplace=True)
            df.to_csv('pro-'+str(num)+'.csv',index=False)

    except:
        pass
