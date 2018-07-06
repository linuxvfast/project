import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
import json
from sqlalchemy.orm import sessionmaker
from conf import settings
import create_table
from core import student
from core import teacher

Session_class = sessionmaker(create_table.engine)
session = Session_class()

def student_view():
    """学生视图"""
    qq = input("请输入学生qq号：")
    students = student.Student(qq)
    while True:
        choice = input("1.交作业，2.查成绩，3.看排名")
        if choice == "1":
            grade_name = input("课程名称:")
            grade_date = input("上课日期（2018-02-03）：")
            ret = students.submit_task(grade_name, grade_date)
            print(ret)
        elif choice =="2" :
            grade_name = input("课程名称:")
            ret=students.get_score(grade_name)
            print(ret)
        elif choice == "3":
            grade_name = input("课程名称:")
            ret = students.get_rank(grade_name)
            print(ret)
        else:
            print("请输入正确的选项")
            exit()

def teacher_view():
    """教师视图"""
    teacher_name = input("输入老师姓名:")
    teachers = teacher.Teacher(teacher_name)
    while True:
        choice = input("1.增加课程，2.增加上课记录，3.把学生增加到班级，4.修改学生成绩")
        if choice == "1":
            grade_name = input("课程名称:")
            ret = teachers.add_grade(grade_name)
            print(ret)
        elif choice == "2":
            grade_name = input("课程名称:")
            ret = teachers.add_grade_record(grade_name)
            print(ret)
        elif choice == "3":
            qq = input("请输入学生qq号：")
            grade_name = input("课程名称:")
            ret = teachers.add_student_to_grade(qq, grade_name)
            print(ret)
        elif choice=="4":
            qq = input("请输入学生qq号：")
            grade_name = input("课程名称:")
            date = input("上课时间：")
            score = input("成绩:")
            ret = teachers.modify_score(grade_name, qq, date, score)
            print(ret)
        else:
            print("请输入正确的选项")
            exit()

def register():
    '''注册用户'''
    user = input('请输入用户名>>').strip()
    get_qq = input('请输入qq号码>>').strip()
    stu1 = create_table.Student(name=user,qq=get_qq)

    session.add_all([stu1])
    session.commit()
    session.close()
    print('user [%s] register successfull '%user)

def login():
    '''用户登陆'''
    print('请选择'.center(20,'-'))
    print('1 学生  2 老师')
    choice = input('请选择>>')
    if  choice == '1':
        # print(create_table.list_qq())
        student_view()
    if choice == '2':
        # print(create_table.list_teacher())
        teacher_view()
    else:
        exit()
        print('input error')





def run():
    while True:
        print('欢迎登陆学员管理系统'.center(30,'='))
        msg='''
        1   注册  |   2   登陆'''
        print(msg)
        func = {
            '1':register,
            '2':login,
        }
        choice = input('>>').strip()
        if len(choice) == 0:
            continue
        elif choice == '1' or choice == '2':
            func[choice]()

        else:
            continue

if __name__ == '__main__':
    run()