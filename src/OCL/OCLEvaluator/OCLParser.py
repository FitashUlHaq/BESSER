from OCL.OCLEvaluator.OCLIndividual import *
from OCL.OCLEvaluator.OCLExpressionFactory import *
class OCLParser:
    def __init__(self):
        pass
    def parseOCL(self,ocl):
        toReturn = []

        individualOCL = OclIndividual()
        oclexpFactory = OCLExpressionFactory()

        ocl = " ".join(ocl.split())
        oclParts = ocl.split(" ")
        operatorset = False
        for i in range (len(oclParts)):
            part = oclParts[i]
            if part == "context" or part == "context":
                individualOCL.set_context(oclParts[i+1])
            elif part == ">" or part == "<":
                individualOCL.set_operator(part)
                operatorset = True
            elif part == "=":
                individualOCL.set_operator("==")
                operatorset = True
            elif part == "<>":
                individualOCL.set_operator(part)
                operatorset = True
            else:
                if operatorset:
                    individualOCL.set_right(oclexpFactory.create(part))
                else:
                    individualOCL.set_left(oclexpFactory.create(part))
        toReturn.append(individualOCL)
        return toReturn