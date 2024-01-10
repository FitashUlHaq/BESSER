from OCL.OCLEvaluator.OCLParser import *
class OCLHandler:
    def __init__(self):
        self.logical_exp =""
        self.orig_ocl_exp =""
        self.oclParser = OCLParser()
    def handleOCL(self,ocl):
        self.OCLparts = self.oclParser.parseOCL(ocl)



    def evaluate(self, envHandler):
        results = []
        for oclPart in self.OCLparts:
            logicalExpTemplate = self.createLogicalExpTemplate(oclPart)
            logicalExpIstance = self.createLogicalExpInstance(logicalExpTemplate,oclPart,envHandler)
            results.append(eval(logicalExpIstance))
        return results

    def createLogicalExpTemplate(self, oclPart):
        localExp = ""
        if not isinstance(oclPart.get_left(), IntegerLiteralExp) and not isinstance(oclPart.get_left(), RealLiteralExp):
            localExp =" #LeftVal#"
        else:
            localExp = str(oclPart.get_left().getVal())

        localExp = localExp+" " + oclPart.get_operator()

        if not isinstance(oclPart.get_right(), IntegerLiteralExp) and not isinstance(oclPart.get_right(), RealLiteralExp):
            localExp =localExp+ "#RightVal#"
        else:
            localExp = localExp+" "+str(oclPart.get_right().getVal())

        return localExp

    def createLogicalExpInstance(self, logicalExpTemplate, oclPart, envHandler):
        finalLogicalExp = ""
        allInstances = envHandler.getAllInstances (oclPart.get_context())
        # allInstances[0].printAllAttributes()
        if "#LeftVal#" in logicalExpTemplate and not "#RightVal#" in logicalExpTemplate:
            attribute_from_env = oclPart.get_left().getVal()
            for i in range(len(allInstances)):
                instance = allInstances[i]
                valueFromEnv = instance.getAttributeValue(attribute_from_env)
                finalLogicalExp = finalLogicalExp + logicalExpTemplate.replace("#LeftVal#", valueFromEnv)
                if i < len(allInstances)-1:
                    finalLogicalExp = finalLogicalExp+" and "

        if "#RightVal#" in logicalExpTemplate and not "#LeftVal#" in logicalExpTemplate:
            attribute_from_env = oclPart.get_left().getVal()
            for i in range(len(allInstances)):
                instance = allInstances[i]
                valueFromEnv = instance.getAttributeValue(attribute_from_env)
                finalLogicalExp = finalLogicalExp + logicalExpTemplate.replace("#LeftVal#", valueFromEnv)
                if i < len(allInstances)-1:
                    finalLogicalExp = finalLogicalExp+" and "


        return finalLogicalExp

