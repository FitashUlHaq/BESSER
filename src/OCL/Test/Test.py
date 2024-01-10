from OCL.OCLEvaluator.OCLParser import *
from OCL.OCLEvaluator.OCLHandler import OCLHandler
from OCL.OCLEvaluator.EnvironmentHandler import *
if __name__ == '__main__':
    print("hello and welcome")
    path = "OCL/Test/libraryObjectDiagram.plantuml"

    OCLConstraint = "context Book inv: self.pages < 40"
    oclHandler = OCLHandler()
    oclHandler.handleOCL(OCLConstraint)

    envHandler = EnvironmentHandler()
    envHandler.populateEnvironment(open(path).read())
    # envHandler.print()

    results = oclHandler.evaluate(envHandler)

    print("The result of OCL Constraint"+OCLConstraint +" is "+ str(results))



    # envHandler.print()


