from OCL.OCLExpression.OCLExpression import OCLExpression
from OCL.OCLExpression.Classifier import Classifier
class TypeExp(OCLExpression):
        def __init__(self):
                self.refferedType = Classifier()
