from besser.BUML.notations.ocl.FactoryInstance import Factory
from besser.BUML.metamodel.structural.rules import *
class Evaluator:

    def __init__(self):
        self.debug = True
    def get_value(self,name, obj):
        for slot in obj.slots:
            if "self." in name:
                if name.split('.')[-1] == slot.name:
                    # print(slot.value.value)
                    return slot.value.value
    def checkInObj(self,obj,source):
        for s in obj.slots:
            if s.name == source.name:
                return obj
    def verifyBody (self,tree, obj,logicalExp):
        pass
    def getID(self,slots):
        for s in slots:
            if s.get_attribute.is_id:
                return s
    def get_logical_exp(self,tree,logicalExp,obj):
        print("")
        if isinstance(tree,PropertyCallExpression):
            if tree.source == None:
                pass
        if isinstance(tree, LoopExp):#forAll, select,..etc
            source = tree.source
            allObjs = self.checkInObj(obj,source)
            if allObjs is None:
                if logicalExp[0] =="":
                    logicalExp[0] = logicalExp[0] + " True "
                else:
                    logicalExp[0] = logicalExp[0] +" and True "
            else:
                self.verifyBody (tree, obj,logicalExp)
            id = self.getID(obj.slots)
            pass

        if isinstance(tree, OperationCallExpression):
            args = tree.arguments
            for arg in args:
               if hasattr(arg,'name'):
                   if isinstance(arg,IntegerLiteralExpression) or isinstance(arg,RealLiteralExpression) or isinstance(arg,BooleanLiteralExpression):
                       logicalExp[0] = logicalExp[0] + str(arg.value)
                   else:
                        logicalExp[0]= logicalExp[0] + self.get_value(arg.name,obj)
               else:
                   logicalExp[0] = logicalExp[0] +" " +str(arg)+ " "
            if tree.referredOperation.get_infix_operator() == "and" or tree.referredOperation.get_infix_operator() == "or":
                logicalExp[0] =  " "+logicalExp[0]+" "+tree.referredOperation.get_infix_operator()  +" "
        if tree.source is not None:
            self.get_logical_exp(tree.source,logicalExp,obj)

    def evaluate(self, rootHandler,objects):
        self.roothandler = rootHandler
        tree = rootHandler.get_root()
        logicalExpTemplate= [""]
        for i in range(len(objects)):
            self.get_logical_exp(tree,logicalExpTemplate,objects[i])
            if len(objects)>1 and i<len(objects)-1:
                logicalExpTemplate[0] = logicalExpTemplate[0] +" and "

        if self.debug:
            print(logicalExpTemplate[0])
        print("Evaluation Result: " + str(eval(logicalExpTemplate[0])))