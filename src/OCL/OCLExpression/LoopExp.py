from OCL.OCLExpression.CallExp import *
from OCL.OCLExpression.OCLExpression import OCLExpression
from OCL.OCLExpression.Variable import *
class LoopExp(CallExp):
    def __init__(self):
        self.body = OCLExpression()
        self.iterator = Variable()
