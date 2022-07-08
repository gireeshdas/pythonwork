class course:
    name: str
    duration:str
    fees: str
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.duration=kwargs.get("duration")
        self.fees=kwargs.get("fees")
    def print_details(self):
        print(self.name,self.duration,self.fees)

crs=course(name="python",duration=" 4months",fees=" 29500rs/-")
crs.print_details()

