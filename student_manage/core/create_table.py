from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,String,Column,ForeignKey,Table,DATE
from sqlalchemy.orm import relationship,sessionmaker
import random,string,datetime,time

engine = create_engine("mysql+pymysql://root:123456@localhost/manager?charset=utf8")
Base = declarative_base()

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))

    def __repr__(self):
        return "%s | %s"%(self.id, self.name)


class GradeRecord(Base):
    __tablename__ = "grade_records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    grade_id = Column(Integer, ForeignKey("grades.id"))
    stu_id =  Column(Integer, ForeignKey("students.id"))
    date = Column(DATE)
    task_status = Column(Integer, default=0)
    score = Column(Integer, default=0)

    # 1对多的关系表
    grade = relationship("Grade", foreign_keys=[grade_id], backref="grade_records")
    student = relationship("Student", foreign_keys=[stu_id], backref="grade_records")

    def __repr__(self):
        return "%s | %s | %s | %s | %s | %s"%(
            self.id, self.grade.name, self.student.name,
            self.date, self.task_status, self.score)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    qq = Column(String(32))

    def __repr__(self):
        return "%s | %s | %s" % (self.id, self.name, self.qq)

# 创建关系表，第三张表连接grade和stuent
grade2student = Table("grade2student", Base.metadata,
                    Column("grade_id", Integer, ForeignKey("grades.id")),
                    Column("student_id", Integer, ForeignKey("students.id"))
                    )

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=True)

    # 增加多对多的关系表
    students = relationship("Student", secondary=grade2student, backref="grades")

    def __repr__(self):
        return "%s | %s" % (self.id, self.name)

Base.metadata.create_all(engine)  #创建表结构

#添加测试数据
Session_class = sessionmaker(bind=engine)
session = Session_class()

def get_qq():
    # 随机获取6位qq号
    nums = string.digits  # 0123456789
    qq = "".join(random.sample(nums, 6))  # 获取6位QQ号
    return qq

def get_time():
    # return time.strftime("%Y-%m-%d", time.localtime()) # 不支持
    # return datetime.datetime.now()  # 支持
    return datetime.date.fromtimestamp(time.time())

def get_date_from_str(string):
    # 通过字符串获取日期对象
    return datetime.date(string)

def init_data():
    # 初始化数据库
    student1 =  Student(name="Tom", qq=get_qq())
    student2 =  Student(name="Jack", qq=get_qq())
    student3 =  Student(name="Jimi", qq=get_qq())
    student4 =  Student(name="Ben", qq=get_qq())
    student5 =  Student(name="Jone", qq=get_qq())

    teacher1 =  Teacher(name="Liteach")
    teacher2 =  Teacher(name="Wteach")
    teacher3 =  Teacher(name="Bteach")

    grade1 =  Grade(name="china")
    grade2 =  Grade(name="math")
    grade3 =  Grade(name="english")

    grade_record1 =  GradeRecord(
        grade=grade1, student=student1, date=get_time())
    grade_record2 =  GradeRecord(
        grade=grade1, student=student2, date=get_time())
    grade_record3 =  GradeRecord(
        grade=grade3, student=student3, date=get_time())

    session.add_all([student1, student2, student3, student4, student5])
    session.add_all([teacher1, teacher2, teacher3])
    session.add_all([grade1, grade2, grade3])
    session.add_all([grade_record1, grade_record2, grade_record3])

    session.commit()
    print("数据初始化成功！")
    
    
# s1 = Score(nid=1,score=80)
# s2 = Score(nid=2,score=100)
# s3 = Score(nid=3,score=60)
# s4 = Score(nid=4,score=30)
# s5 = Score(nid=5,score=50)
#
# c1 = Class(nid=1,classes_name='python',classes_record=1)
# c2 = Class(nid=2,classes_name='python',classes_record=2)
# c3 = Class(nid=3,classes_name='python',classes_record=3)
# c4 = Class(nid=4,classes_name='java',classes_record=1)
# c5 = Class(nid=5,classes_name='java',classes_record=2)
# c6 = Class(nid=6,classes_name='php',classes_record=1)
#
# ss1 = Student(nid=1,name='test',qq='21474836',ranking=0,work_status=0)
# ss2 = Student(nid=2,name='tom',qq='23564859',ranking=0,work_status=0)
# ss3 = Student(nid=3,name='jack',qq='3451820',ranking=0,work_status=0)
#
# t1 = Teacher(nid=1,name='zhangsan',classes_id=1,score_id=3,student_id=1)
# t2 = Teacher(nid=2,name='lisi',classes_id=4,score_id=5,student_id=2)
# t3 = Teacher(nid=3,name='wangwu',classes_id=6,score_id=2,student_id=3)
# #
# c1.score = [s1,s2]
# c2.score = [s4,s5]

# c1.student = [ss1,ss2]
# c2.student = [ss3,ss2]

# session.add_all([s1,s2,s3,s4,s5,c1,c2,c3,c4,c5,c6,ss1,ss2,ss3,t1,t2,t3])
# session.add_all([s1,s2,s3,s4,s5,c1,c2,c3,c4,c5,c6,ss1,ss2,ss3])
# session.add_all([s1,s2,s3,s4,s5,c1,c2,c3,c4,c5,c6])

# score_obj = session.query(Score).filter(Score.nid=='1').first()
# session.delete(score_obj)

# session.commit()
# info = session.query(Student).filter(Student.name=='test').first()
# print(info)
# def list_qq():
#     return [item for item in session.query(Student).all()]
#
# def list_teacher():
#     return [item for item in session.query(Teacher).all()]

if __name__ == '__main__':
    # init_data()
    # session.close()
    # print(list_qq())
    print(list_teacher())