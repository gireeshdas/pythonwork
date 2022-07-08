class Course:
    course_name:str
    status:bool

    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("active_status")

    def __str__(self):
        return self.course_name


class Batch:

    course:Course
    batch_code:str
    start_date:str

    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date = kwargs.get("start_date")

    def __str__(self):

        return self.batch_code

class Student:

    student_name:str
    gender:str
    rol:str
    batch:Batch

    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.phone= kwargs.get("gender")
        self.gender= kwargs.get("rol")
        self.batch = kwargs.get("batch")

    def __str__(self):
        return self.student_name


django=Course()
django.add_course(course_name="django",active_status=True)

bigdat=Course()
bigdat.add_course(course_name="bigdata",active_status=True)

db1=Batch()
db1.add_batch(course=django,batch_code="djmay2022 ",start_date="5.6.2022")

bd1=Batch()
bd1.add_batch(course=bigdat,batch_code="djmay2022 ",start_date="5.6.2022")

rahul=Student()
rahul.add_student(student_name="rahul",gender="male",rol="2345",batch=db1)

# nikil=Student()
# nikil.add_student(student_name="nikil",gender="male",rol="2345",batch=db1)
#
# umer=Student()
# umer.add_student(student_name="umer",gender="male",rol="2345",batch=db1)
print(rahul.batch.course.course_name)
