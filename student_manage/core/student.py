"""
学员视图，实现具体工功能
    提交作业
    查看作业成绩
    一个学员可以同时属于多个班级，就像报了Linux的同时也可以报名Python一样，
     所以提交作业时需先选择班级，再选择具体上课的节数
    附加：学员可以查看自己的班级成绩排名
"""
import sys
import os
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BaseDir)

from core import create_table
from core import common
from create_table import session
from create_table import GradeRecord

class Student(object):
    def __init__(self, qq):
        self.qq = qq

    def get_qq(self):
        return create_table.get_qq()

    def submit_task(self, grade_name, grade_date):
        # 提交作业
        grade_record = common.get_grade_record(grade_name, self.qq, grade_date)
        if grade_record != None:
            grade_record.task_status = 1
            session.commit()
            return True
        else:
            return False

    def get_score(self, grade_name):
        # 查看成绩
        grade = common.get_grade(grade_name)
        student = common.get_student_by_qq(self.qq)
        if grade != None and student != None:
            grade_record = session.query(create_table.GradeRecord).filter(
                create_table.GradeRecord.grade == grade,
                create_table.GradeRecord.student == student,
            ).first()
            if grade_record != None:
                return grade_record.score
        else:
            return None

    def get_rank(self, grade_name):
        # 获取排名
        grade = common.get_grade(grade_name)
        # print(grade)
        student = common.get_student_by_qq(self.qq)
        # print(student)
        if grade != None and student != None:
            grade_records = session.query(GradeRecord).filter(
                GradeRecord.grade == grade
            ).order_by(GradeRecord.score.desc()).all()
            students = list(map(lambda record: record.student, grade_records))
            # print(students) #输出列表
            # print(grade_records)
            if student in students:
                rank = students.index(student)
                return rank+1 # 索引从0开始
        return None

if __name__ == "__main__":
    s = Student("354789")
    # ret = s.get_score("math")
    # print(ret)
    ret=s.get_rank("china")
    print(ret)
    # s = Student()
    # print(s.list_qq())