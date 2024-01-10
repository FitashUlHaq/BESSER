from OCL.OCLExpression.OCLExpression import OCLExpression
from typing import List
from OCL.OCLExpression.Variable import Variable
class VariableExp(OCLExpression):
    def __init__(self):
        self.variable = Variable()
    def set_refferred_variable (self,val):
        if "." in val:
            val = val.split(".")[1]
        self.variable.set_val(val)
    def getVal(self):
        return self.variable.getVal()
