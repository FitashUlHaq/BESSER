from OCL.OCLExpression.NumericLiteralExp import *
class RealLiteralExp(NumericLiteralExp):
    def __init__(self):
        self.realSymbol = 0.0
    def setVal(self,val):
        self.realSymbol = val
    def getVal(self):
        return self.realSymbol
