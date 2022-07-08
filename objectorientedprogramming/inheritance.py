class parent:
    def phone(self):
        print("i phone Xs")
    def car(self):
        print("mini cooper")

class child(parent):
    pass
ch=child()
ch.phone()
ch.car()