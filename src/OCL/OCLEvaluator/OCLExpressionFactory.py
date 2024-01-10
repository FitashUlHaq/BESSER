from OCL.OCLExpression.VariableExp import *
from OCL.OCLExpression.IntegerLiteralExp import IntegerLiteralExp
from OCL.OCLExpression.RealLiteralExp import RealLiteralExp
class OCLExpressionFactory:
    def __init__(self):
        pass

    def isInt(self,num):
        try:
            int(num)
        except ValueError:
            return False
        return True

    def create(self,part):
        if part.isnumeric():
            if self.isInt(part):
                return self.createIntegerLiteralExp(part)
            else:
               return  self.createRealLiteralExp(part)
        elif "self" in part or "." in part:
            return self.create_variable_exp(part)

    def create_variable_exp(self,part):
        var = VariableExp()
        var.set_refferred_variable(part)
        return var

    def createRealLiteralExp(self, part):
        var = RealLiteralExp()
        var.setVal(float(part))
        return var

    def createIntegerLiteralExp(self, part):
        var = IntegerLiteralExp()
        var.setVal(int(part))
        return var
