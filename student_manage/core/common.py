
# 教师，学生，课程通用的方法

import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

import create_table


def get_student_by_qq(student_qq):
    """通过qq获取学生信息"""
    student = create_table.session.query(create_table.Student).filter(
        create_table.Student.qq == student_qq).first()
    return student


def get_grade(grade_name):  #english
    """通过班级名称获取班级信息"""
    grade = create_table.session.query(create_table.Grade).filter(
        create_table.Grade.name == grade_name).first()
    return grade


def get_grade_record(grade_name, student_qq, date):
    """通过班级名称，学生qq，日期获取班级记录"""
    grade = get_grade(grade_name)
    student = get_student_by_qq(student_qq)
    if grade != None and student != None:
        grade_record = create_table.session.query(create_table.GradeRecord).filter(
            create_table.GradeRecord.grade == grade,
            create_table.GradeRecord.student == student,
            create_table.GradeRecord.date == date
        ).first()
        return grade_record
    else:
        return None

if __name__ == '__main__':
    print(get_student_by_qq('354789'))
    print(get_grade('english'))
    print(get_grade_record('china','354789','2018-07-03'))