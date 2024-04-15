from besser.BUML.metamodel.structural.rules import *

class Factory:

    def create_property_Call_Expression(self,name, type):
        return PropertyCallExpression(name,type)
    def create_variable_expression(self,name,type):
        var = VariableExp(name,type)
        return var

    def create_boolean_literal_expression(self, name, val):
        return BooleanLiteralExpression(name, val)
    def create_integer_literal_expression(self, name, val):
        return IntegerLiteralExpression(name, val)
        pass

    def create_real_literal_expression(self, name, val):
        return RealLiteralExpression(name, val)
        pass

    def create_if_else_exp(self,name, type):
        return IfExp(name,type)
    def create_set_type(self):
        return SetType("Set")
    def create_ordered_set_type(self):
        return OrderedSetType("OrderedSetType")
    def create_sub_ordered_set_type(self):
        return OrderedSetType("SubOrderedSetType")

    def create_operation_call_expression(self, leftpart = None, rightpart= None, infixOperator= None, inBetweenOp=None,beforeOp = None,isleftNone=False,name = None):
        if inBetweenOp is None and isleftNone is False and name is None:
            if beforeOp is None:
                return OperationCallExpression("Operation", infixOperator.get_infix_operator(),
                                           [leftpart, infixOperator, rightpart])
            else:
                return OperationCallExpression("Operation", infixOperator.get_infix_operator(),
                                           [infixOperator, rightpart])
        elif inBetweenOp is None and isleftNone is True and name is None:
            return OperationCallExpression("Operation", infixOperator.get_infix_operator(),
                                           [infixOperator, rightpart])
        elif inBetweenOp is not None and name is None:
            if beforeOp is None:
                oce = OperationCallExpression("Operation", infixOperator.get_infix_operator(),
                                               [leftpart, infixOperator, rightpart])
                oce.set_referred_operation(inBetweenOp)
                return oce
            else:
                oce = OperationCallExpression("Operation", infixOperator.get_infix_operator(),
                                              [beforeOp,leftpart, infixOperator, rightpart])
                oce.set_referred_operation(inBetweenOp)
                return oce
        else:
            return OperationCallExpression(name=name, operation =name,arguments=[] )

    def create_type_exp(self,classifier):
        return TypeExp(classifier,classifier)

    def create_loop_expression(self,collectionOperator):
        return LoopExp(collectionOperator,None)
        pass
    def create_bag_type(self):
        return BagType("BagType")
    def create_collection_literal_expression(self,name,type):
        return CollectionLiteralExp(name = name,type=type)
    def create_sequence_type(self):
        return SequenceType("SequenceType")
    def create_sub_sequence_type(self):
        return SequenceType("SubSequenceType")
    def create_collection_item(self,name ,item):
        return CollectionItem(name,item)
    def create_iterator_expression(self,name,type):
        return IteratorExp(name,type)
        pass

    def create_infix_operator(self,op):
        return InfixOperator(op)
