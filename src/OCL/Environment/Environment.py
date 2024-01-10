from OCL.Environment.NamedElement import *
class Environment:
    allElements = []
    def __init__(self):
        self.allElements = []
    def add_element(self,name):
        self.allElements.append(NamedElement(name))
    def update_element(self,name,attribute_name,val):
        for e in self.allElements:
            if e.getName() == name:
                e.addAttribtues(attribute_name,val)
    def lookUpWithName(self,name):
        for e in self.allElements:
            if e.getName() ==name:
                return e
    def print(self):
        for e in self.allElements:
            print(e.getName())
            e.printAllAttributes()
    def add_reference(self,referenceto,refered):
        obj1 = self.lookUpWithName(referenceto.getName())
        obj2= self.lookUpWithName(refered.getName())
        obj1.add_reference(obj2)

    def getallInstance(self, className):
        to_ret = []
        for e in self.allElements:
            if className in e.getName():
                to_ret.append(e)
        return to_ret
