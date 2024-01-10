from OCL.OCLExpression.NumericLiteralExp import *
class IntegerLiteralExp(NumericLiteralExp):
    def __init__(self):
        self.IntegerSymbol = 0
    def setVal(self,val):
        self.IntegerSymbol = val
    def getVal(self):
        return self.IntegerSymbol