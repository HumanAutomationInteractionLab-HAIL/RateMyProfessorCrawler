
# -*- coding: utf-8 -*-
# @Time    : 2019/2/3 下午12:29
# @Author  : mingchun liu
# @Email   : psymingchun@gmail.com
# @File    : RateMypro_HTML_Parsing.py
# @Software: PyCharm
# @description：从原始网页数据中提取有效信息，保存为csv格式

#++++++++++原始数据集+++++++++++++++#
# 1.【01dataset】原始网页数据是322713个
# 2.【02dataset】原始网页数据是707618个
# 3.【03dataset】原始网页数据是622610个
# 4.【04dataset】原始网页数据是200969个
#原始数据共计1853910

#++++++++++网页解析后数据集++++++++++#
#提取时间：2019年2月3日12:00 - 2019年2月4日15:00
# 1.【Extract_RateMyProfessor1】提取01dataset有效数据189602个
# 2.【Extract_RateMyProfessor2】提取02dataset有效数据440990个
# 3.【Extract_RateMyProfessor3】提取03dataset有效数据432344个
# 4.【Extract_RateMyProfessor4】提取04dataset有效数据114804个
# 有效数据共计1177740

#++++++++++数据集维度++++++++#
#professor_name
#school_name
#department_name
#local_name
#state_name
#year_since_first_review
#star_rating
#take_again
#diff_index
#tag_professor
#num_student
#post_date
#name_onlines
#student_star
#student_difficult
#attence for_credits
#would_take_agains
#grades
#stu_tags
#help_useful
#help_not_useful
#comments
#共计22个特征


import pandas as pd
from pyquery import PyQuery as PQ
import re
import os

path ='I:\DownloadedRateMyProfessorData-01dataset'
res_path = r'C:\Users\Administrator\Desktop\RMP1\data'

file_list = os.listdir(path)
num = 1
for each in file_list:
    # print(path+each)
    file_path = path+'\\'+each
    with open(file_path,'r') as f:
        html = f.read()

    professor_names = []
    school_names = []
    department_names=[]
    local_names = []
    state_names = []

    star_ratings = []
    take_agains = []
    tags_professor = []

    diff_indexs = []
    num_students = []

    post_date=[]
    name_onlines =[]

    stu_stars = []
    stu_diffs = []
    attences = []

    for_credits =[]
    would_take_agains =[]
    grades =[]

    stu_tags = []
    comments = []
    help_useful = []
    help_not_useful = []

    try:
        doc = PQ(html)
    except:
        print(f'{file_path} Document is empty')
    else:
        professor_name = doc('h1.profname')
        if professor_name:
            # professor name
            professor_name = doc('h1.profname').text()
            professor = re.sub(r'\\r\\n', "", professor_name)
            professor_name = professor.strip()
            # print(professor_name)

            # area
            area = doc('h2.schoolname').text()
            school_name = area.split(',')[0][3:]
            depart_name = doc('div.result-title').text().split('\\r\\n')[1]
            department_name = re.search(r'.*department', depart_name).group()[18:]

            local_name = area.split(',')[1]
            state_name = area.split(',')[2]
        else:
            professor_name = '0'
            school_name = '0'
            department_name = '0'
            local_name = '0'
            state_name = '0'

        professor_names.append(professor_name)
        school_names.append(school_name)
        department_names.append(department_name)
        local_names.append(local_name)
        state_names.append(state_name)

        rating_div = doc('div.rating-breakdown')
        if rating_div:
            # star_rating would take again level of difficulty
            grade_divs = doc('div.grade')
            for index, grade in enumerate(grade_divs.items()):
                if index == 0:
                    star_rating = grade.text()
                    star_rating = re.sub(r'\\r\\n', "", star_rating)
                    star_rating = star_rating.strip()
                elif index == 1:
                    take_again = grade.text()
                    take_again = re.sub(r'\\r\\n', "", take_again)
                    take_again = take_again.strip()
                elif index == 2:
                    diff_index = grade.text()
                    # print(f'first:{diff_index}')
                    diff_index = re.sub(r'\\r\\n', "", diff_index)
                    diff_index = diff_index.strip()
                    # print(f'second:{diff_index}')
            star_ratings.append(star_rating)
            take_agains.append(take_again)
            diff_indexs.append(diff_index)

            # tags
            tag = doc('div.tag-box span')
            if tag:
                tag = doc('div.tag-box').text()
                tag = re.sub(r'\\r\\n', "", tag)
                tag = tag.strip()
                tags_professor.append(tag)
            else:
                pass
                # tags_professor.append('NULL')

            # number of students
            num_student = doc('div.table-toggle.rating-count.active').text()
            num_student = re.sub(r'\\r\\n', "", num_student)
            num_student = num_student.strip()
            num_student = num_student.split(' ')[0]
            num_students.append(num_student)

        date = doc('div.date')
        # print(type(date))
        for each in date.items():
            each_date = re.sub(r'\\r\\n', "", each.text()).strip()
            # print(each_date)
            post_date.append(each_date)

        name_online = doc('span.name')
        for each in name_online.items():
            name_onlines.append(each.text().strip())

        for_credit = doc('span.credit')
        for each in for_credit.items():
            credit = each.text().split(' ')[2].strip()
            for_credits.append(credit)

        #学生个人对教授的评分及课程难度评价
        stu_star = doc('div.descriptor-container')
        for each in stu_star.items():
            each_stu_star = re.sub(r'\\r\\n', "", each.text()).strip()
            if 'Overall' in each_stu_star:
                # print(each_stu_star[:3])
                stu_stars.append(each_stu_star[:3])
            elif 'Level of Difficulty' in each_stu_star:
                # print(each_stu_star[:3])
                stu_diffs.append(each_stu_star[:3])
            else:
                pass

        attence = doc('span.attendance')
        for each in attence.items():
            stu_attence = re.sub(r'\\r\\n', "", each.text()).strip()
            # print(stu_attence[12:])
            attences.append(stu_attence[12:])

        take_again = doc('span.would-take-again')
        for each in take_again.items():
            would_tale_again = each.text().split(' ')[3].strip()
            would_take_agains.append(would_tale_again)

        grade = doc('span.grade')
        for each in grade.items():
            recieved_grade = each.text().split(' ')[2].strip()

            grades.append(recieved_grade)

        stu_tag = doc('div.tagbox')
        for each in stu_tag.items():
            tags = re.sub(r'\\r\\n', "", each.text()).strip()
            # print(tags)
            stu_tags.append(tags)

        comment = doc('p.commentsParagraph')
        for each in comment.items():
            each_comment = re.sub(r'\\r\\n',"",each.text()).strip()
            # print(each_comment)
            comments.append(each_comment)

        help_usefuls = doc('div.thumbs')
        for each in help_usefuls.items():
            help = re.sub(r'\\r\\n',"",each.text()).strip()
            num_useful = re.findall('\d',help)
            # print(num)
            help_useful.append(num_useful[0])
            help_not_useful.append(num_useful[1])

        infos = {'professor_name': professor_names, 'school_name': school_names, 'department_name': department_names,
                 'local_name': local_names, 'state_name': state_names, 'star_rating': star_ratings, 'take_again': take_agains,
                 'diff_index': diff_indexs, 'tag_professor': tags_professor, 'num_student': num_students,
                 'post_date': post_date,'name_onlines':name_onlines,'student_star':stu_stars, 'student_difficult' :stu_diffs, 'attence':attences, 'for_credits':for_credits,'would_take_agains':would_take_agains,'grades':grades,'stu_tags':stu_tags, 'help_useful':help_useful,'help_not_useful':help_not_useful,'comments': comments}
        df = pd.DataFrame().from_dict(infos,orient='index')
        df = df.T



        if df['professor_name'][0] == '0':
            pass
        else:
            #填充教授信息
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

            # 计算授课年份
            date = pd.to_datetime(df['post_date']).dt.year
            year_first_review = date.max() - date.min()
            df.insert(loc=5, column='year_since_first_review', value=year_first_review)

            df.to_csv(res_path + str(num) + '.csv', index=False)
            print('第' + str(num) + '文件','名字是'+df['professor_name'][0])

        num += 1