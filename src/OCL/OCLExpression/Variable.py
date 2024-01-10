from OCL.OCLExpression.OCLExpression import OCLExpression
from OCL.OCLExpression.Parameter import Parameter
class Variable(OCLExpression):
    def set_val(self,val):
        self.representatedParameter = Parameter(val)
    def getVal(self):
        return self.representatedParameter.getVal()
