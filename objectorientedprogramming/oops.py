class person:
    name:str
    age:int
    gender:str
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.age=kwargs.get("age")
        self.gender=kwargs.get("gender")
    def print_person(self):
        print(self.name,self.age,self.gender)

p1=person(name="gireesh",age="25",gender="male")
# p2=person()
p1.print_person()