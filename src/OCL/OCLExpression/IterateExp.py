from OCL.OCLExpression.LoopExp import *
from OCL.OCLExpression.Variable import *
class IterateExp(LoopExp):
    def __init__(self):
        self.result=Variable()
