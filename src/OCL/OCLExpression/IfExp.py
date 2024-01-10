from OCL.OCLExpression.OCLExpression import OCLExpression
class IfExp(OCLExpression):
    def __init__(self):
        # self.ifOwner = null
        self.ifCondition = None
        self.elseExpression = None
        self.thenExpression = None
