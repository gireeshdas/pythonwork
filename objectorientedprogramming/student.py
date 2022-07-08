class student:
    name:str
    standrd:int
    rollno:int
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.standrd=kwargs.get("standrd")
        self.rollno=kwargs.get("rollno")
    def print_student(self):
        print(self.name,self.standrd,self.rollno)

s1=student(name="gireesh",standrd="12",rollno="21")
# s2=student()

s1.print_student()