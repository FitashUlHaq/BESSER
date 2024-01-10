class NamedElement:
    def __init__(self,name):
        self.name = name
        self.attributes = {}
        self.referenceto=[]
    def printAllAttributes(self):
        for attrib in self.attributes:
            print (attrib, end =" ")
            print(self.attributes[attrib])
    def addAttribtues (self,name,val):
        name = name.replace(" ","")
        self.attributes[name] = val
    def add_reference (self,obj):
        self.referenceto.append(obj)
    def getName(self):
        return self.name
    def getAttributeValue(self,attrib):
        return self.attributes[attrib]
