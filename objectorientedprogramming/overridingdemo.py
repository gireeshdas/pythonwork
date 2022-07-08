class parent:
    def properties(self):
        self.props={"mobile":"nokia","bike":"passion pro"}
        return self.props


class child(parent):
    def properties(self):
        props=super().properties()
        props["car"]="benz"
        return props

ch=child()
print(ch.properties())

list.append()