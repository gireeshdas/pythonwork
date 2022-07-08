# class staff(object):
#     id:int
#     name:str
#     role:str
#
#     def __init__(self,*args,**kwargs):
#         self.id=kwargs.get("id")
#         self.name = kwargs.get("name")
#         self.role = kwargs.get("role")
#
#     def __str__(self):
#         return self.name
#
#
# user=staff(id=100,name="gireesh",role="HR")
# print(user)
# #
def admin_only(fn):
    def wrapper(**kwargs):
        user=kwargs.get("user")
        if user.role!="admin":
            print("admin permission required")
        else:
            fn(kwargs)
    return wrapper()



class Employee:
    def __init__(self,**kwargs):
        self.emp_id=kwargs.get("emp_id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")
    def __str__(self):
        return self.name

class Department():

    def __init__(self,**kwargs):
        user=kwargs.get("user")
        if user.role=="admin":

            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("no access")

    def __str__(self):
        return self.dept_name

empl=Employee(emp_id=1002,name="rahul",role="admin")
print(empl)
dept=Department(dept_name="accounting",user=empl)
print(dept)
# print(dept.user)
