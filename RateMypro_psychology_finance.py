
#++++++++++金融类教授数据集++++++++++#
#提取说明：以Finance，Business和Economics为关键词筛选

#++++++++++心理学教授数据集++++++++++#
#提取时间：2019年2月7日
# 1.【Extract_RateMyProfessor1】提取有效数据9436个
# 2.【Extract_RateMyProfessor2】提取有效数据21625个
# 3.【Extract_RateMyProfessor3】提取有效数据20897个
# 4.【Extract_RateMyProfessor4】提取有效数据5545个
# 心理学教授有效数据共计36606

import pandas as pd
import shutil

src = r'C:\Users\Administrator\Desktop\Extract_RateMyProfessor1'
save_path = r'C:\Users\Administrator\Desktop\psy1'
save_path1 = r'C:\Users\Administrator\Desktop\Finance1'
save_path2 = r'C:\Users\Administrator\Desktop\Economics1'

filelist = os.listdir(src)

num = 1
for i in range(1,len(filelist)):
    newsrc =src +'\\'+ filelist[i]
    df = pd.read_csv(newsrc)
    try:
        if 'Psychology' in df['department_name'][0]:
            print(df['department_name'][0],'第'+str(num)+'文件','文件地址：'+ newsrc)
            shutil.copy(newsrc,save_path)
            num += 1
        # elif 'Finance1' in df['department_name'][0]:
        #     print(df['department_name'][0], '第' + str(num) + '文件', '文件地址：' + newsrc)
        #     shutil.copy(newsrc, save_path1)
        #     num += 1
        # elif 'Economics' in df['department_name'][0]:
        #     print(df['department_name'][0], '第' + str(num) + '文件', '文件地址：' + newsrc)
        #     shutil.copy(newsrc, save_path2)
        #     num += 1
    except:
        pass
