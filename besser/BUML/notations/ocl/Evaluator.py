from besser.BUML.notations.ocl.FactoryInstance import Factory
from besser.BUML.metamodel.structural.rules import *
class Evaluator:

    def __init__(self):
        self.debug = True
    def get_value(self,name, obj):
        for slot in obj.slots:
            if "." in name:
                if name.split('.')[-1] == slot.name:
                    # print(slot.value.value)
                    return slot.value.value
    def checkInObj(self,obj,source):
        for s in obj.slots:
            if s.name == source.name:
                return obj
    def checkInLinkEnds(self,obj, source):

        for link in obj.getLinkEnds():
            if link.name == source.name.split('.')[-1]:
                return link.instance
            pass

        pass
    def handleForAll(self, tree, allObjs, logicalExp):
        logicalExp[0] = logicalExp[0] +" ("
        for index in range(len(allObjs)):
            if len(tree.get_body)>0:
                self.update_logical_exp(tree.get_body[0],logicalExp,allObjs[index])
                if index < len(allObjs)-1:
                    logicalExp[0] = logicalExp[0] + " and "
        logicalExp[0] = logicalExp[0] +" )"
        pass
    def handle(self, source, obj, logicalExp,rightSide = False):
        if isinstance(source, PropertyCallExpression):
            if len(source.name.split('.'))==2:
                allObjs = self.checkInObj(obj,source)
                if allObjs is None:
                    allObjs = self.checkInLinkEnds(obj, source)
                for index in range(len(allObjs)):
                    objs = allObjs[index]
                    if len(allObjs) > 1 or rightSide:
                        logicalExp[0] = logicalExp[0] + " [ "
                    for i in range (len(objs.slots)):
                        logicalExp[0] = logicalExp[0] + "\""+str(objs.slots[i].name)+ str(objs.slots[i].value.value) + "\""
                        if i < len(objs.slots)-1:
                            logicalExp[0] = logicalExp[0]+","
                    if not rightSide:
                        if len(allObjs) > 1 and index< len(allObjs)-1:
                            logicalExp[0] = logicalExp[0] + " ], "
                    else:
                        logicalExp[0] = logicalExp[0] + " ] "
                        if len(allObjs) > 1 and index< len(allObjs)-1:
                            logicalExp[0] = logicalExp[0] + " , "


            pass
        pass
    def handleExcludes(self, tree, obj, logicalExp):
        # tempLogicalExp =[""]
        args = tree.arguments
        self.checkAndAdd(logicalExp, " and ")
        logicalExp[0] = logicalExp[0] + " [ "
        self.handle(tree.source, obj, logicalExp)
        logicalExp[0] = logicalExp[0] + " ] not in "
        if len(args)==1: #Property
            logicalExp[0] = logicalExp[0] + " [ "
            self.handle(args[0],obj,logicalExp,True)
            logicalExp[0] = logicalExp[0] + " ]"
        pass

    def handleIncludes(self, tree, obj, logicalExp):
        # tempLogicalExp =[""]
        args = tree.arguments
        self.checkAndAdd(logicalExp, " and ")
        logicalExp[0] = logicalExp[0] + " [ "
        self.handle(tree.source, obj, logicalExp)
        logicalExp[0] = logicalExp[0] + " ] in "
        if len(args)==1: #Property
            logicalExp[0] = logicalExp[0] + " [ "
            self.handle(args[0],obj,logicalExp,True)
            logicalExp[0] = logicalExp[0] + " ]"
        pass
    def handleExists(self,tree,allObjs,logicalExp):
        logicalExp[0] = logicalExp[0] + " ("
        for index in range(len(allObjs)):
            if len(tree.get_body) > 0:
                self.update_logical_exp(tree.get_body[0], logicalExp, allObjs[index])
                if index < len(allObjs) - 1:
                    logicalExp[0] = logicalExp[0] + " or "
        logicalExp[0] = logicalExp[0] + " )"
    def verifyBody (self,tree, obj,logicalExp,source):

        expressionType = tree.name
        allObjs = self.checkInObj(obj,source)
        if allObjs is None:
            allObjs = self.checkInLinkEnds(obj, source)

        if expressionType == "forAll":
                self.handleForAll(tree, allObjs, logicalExp)
        elif expressionType == "exists":
            self.handleExists(tree,allObjs,logicalExp)

        pass
    def getID(self,slots):
        for s in slots:
            if s.get_attribute.is_id:
                return s
    def add_to_exp(self,item,logicalExp):
        if logicalExp[0] == "":
            logicalExp[0] = logicalExp[0] + item
        else:
            logicalExp[0] = logicalExp[0] + " and "+item
    def update_logical_exp(self, tree, logicalExp, obj):
        print("",end ="")
        if isinstance(tree,PropertyCallExpression):
           if tree.source == None:
                pass

        if isinstance(tree, LoopExp):#forAll, select,..etc
            source = tree.source

            if len(source.name.split('.')) == 2 : # same class
                id = self.getID(obj.slots)
                objectName = self.roothandler.get_context_name()
                if id.get_attribute.name == objectName:
                    self.verifyBody(tree,obj,logicalExp,source)
            pass

        if isinstance(tree, OperationCallExpression):

            if tree.name == "EXCLUDES":
                self.handleExcludes(tree, obj, logicalExp)
            elif tree.name == "INCLUDES":
                self.handleIncludes(tree, obj, logicalExp)
            else:
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
            self.update_logical_exp(tree.source, logicalExp, obj)
    def checkAndAdd(self, logicalExpTemplate, toAdd):
        if len(logicalExpTemplate[0])>5:
            if logicalExpTemplate[0][-5:] != " and " or logicalExpTemplate[0][-5:] != " or ":
                logicalExpTemplate[0] = logicalExpTemplate[0]+toAdd
    def valid_object(self,contextName, object):
        idSlot = self.getID(object.slots)
        if idSlot.get_attribute.name == contextName:
            return True
        return False
    def getValidObjects(self,contextName, objs):
        toRet = []
        for obj in objs:
            if self.valid_object(contextName,obj):
                toRet.append(obj)
        return toRet


    def evaluate(self, rootHandler,objects):
        self.roothandler = rootHandler

        objs = self.getValidObjects(self.roothandler.get_context_name(),objects)
        tree = rootHandler.get_root()
        logicalExpTemplate= [""]
        for i in range(len(objs)):
            self.update_logical_exp(tree, logicalExpTemplate, objs[i])
            if len(objects)>1 and i < len(objs) -1:
                self.checkAndAdd(logicalExpTemplate," and ")
                # logicalExpTemplate[0] = logicalExpTemplate[0] +" and "

        if self.debug:
            print(logicalExpTemplate[0])
        return eval(logicalExpTemplate[0].replace('=','=='))