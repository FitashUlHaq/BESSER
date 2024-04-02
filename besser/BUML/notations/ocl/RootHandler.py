from besser.BUML.notations.ocl.FactoryInstance import Factory
class Root_Handler:
    def __init__(self):
        self.root = None
        self.factory = Factory()
        self.all =[]

    def get_root(self):
        return self.root
    def set_context_name(self,name):
        self.context_name = name
    def create_if_else_exp(self,name,type):
        return self.factory.create_if_else_exp(name,type)
    def pop(self):
        self.last_coll_exp = self.all.pop()
        self.add_to_root(self.last_coll_exp)
    def checkNumberOrVariable(self, txt):
        if txt.isnumeric():
            if "." in txt:
                return "real"
            else:
                return "int"
        else:
            return "var"

    def add_to_root(self, op):
        if len(self.all) == 0:
            if self.root is None:
                self.root = op
            else:
                op.source = self.root
                self.root = op
        else:
            self.all[-1].add_body(op)
        pass
    def pop_root(self,root):

        if self.root == self.last_coll_exp:
            self.root = None
            return self.last_coll_exp
        if hasattr(root, "arguments"):
            if self.last_coll_exp in root.arguments:
                root.arguments.remove(self.last_coll_exp)
                return self.last_coll_exp
            for args in root.arguments:
                self.pop_root(args)

    def print(self):
        self.handlePrint(self.root)
    def handle_ID(self,id):
        varID =self.factory.create_variable_expression(id,None)
        self.add_to_root(varID)
        # print('\x1b[6;30;42m' + 'handled ID, verify me!!!' + '\x1b[0m')
        pass
    def create_ordered_set(self):
        type = self.factory.create_ordered_set_type()
        return self.factory.create_collection_literal_expression("orderedSet", type)

    def create_set(self):
        type = self.factory.create_set_type()
        return self.factory.create_collection_literal_expression("set", type)

    def create_sub_ordered_set(self):
        type = self.factory.create_ordered_set_type()
        return self.factory.create_collection_literal_expression("subOrderedSet", type)
    def create_sequence(self):
        type = self.factory.create_sequence_type ()
        return self.factory.create_collection_literal_expression("sequence",type)
    def create_bag(self):
        type = self.factory.create_bag_type()
        return self.factory.create_collection_literal_expression("bag",type = type)
    def create_operation_call_exp(self,name):
       return self.factory.create_operation_call_expression(name=name)
    def get_factory(self):
        return self.factory
    def handle_bag(self,  collectionLiteral, operator):
        infixOperator = None
        if operator is not None:
            infixOperator = self.factory.create_infix_operator(operator)

        if infixOperator is not None:
            operationCallExp = self.factory.create_operation_call_expression(None,collectionLiteral,infixOperator,None,True)

        self.add_to_root(operationCallExp)
    def handle_adding_to_root(self, expression, op=None):
        if op is not None:
            expression.set_referred_operation(op)
        self.add_to_root(expression)
        pass
    def handlePrimaryExp(self,primaryExp,operator):
        pass

    def handle_collection(self,oclExp):

        collectionOperator = None
        if "forAll" in oclExp[0:8]:
            collectionOperator = "forAll"
            pass
        elif "exists" in oclExp[0:8]:
            collectionOperator = "exists"
            pass
        elif "collect" in oclExp[0:9]:
            collectionOperator = "collect"
            pass
        elif "select" in oclExp[0:8]:
            collectionOperator = "select"
            pass

        print("Collection Operator: " + collectionOperator)
        self.handleColl(oclExp,collectionOperator)

        pass

    def handleColl(self, forAllExp,collectionOperator):

        self.all.append(self.factory.create_loop_expression(collectionOperator))
        without_arrow = forAllExp.replace("->", '')
        without_collOp = without_arrow.replace(collectionOperator+"(", '')
        if "|" in without_collOp:
            iterator = without_collOp.split("|")[0]
            multiple_variable = iterator.split(',')
            for variable in multiple_variable:
                iteratorParts = variable.split(':')
                iteratorVariableName = iteratorParts[0]
                if ":" in variable:
                    iteratorclass = iteratorParts[1]
                else:
                    iteratorclass = "NotMentioned"
                iteratorExp = self.factory.create_iterator_expression(iteratorVariableName ,iteratorclass)
                self.all[-1].addIterator(iteratorExp)

        pass
    def handle_binary_expression(self, expression, operator,inbetween= None):
        expressionParts = expression.split(operator)

        leftside = self.checkNumberOrVariable(expressionParts[0])
        rightside = self.checkNumberOrVariable(expressionParts[1])

        leftPart = None
        rightPart = None

        if "var" in leftside:
            leftPart = self.factory.create_variable_expression(expressionParts[0], type="NP")
        elif "int" in leftside:
            leftPart = self.factory.create_integer_literal_expression("NP", int(expressionParts[0]))
        elif "real" in leftside:
            leftPart = self.factory.create_real_literal_expression("NP", float(expressionParts[0]))

        if "var" in rightside:
            rightPart = self.factory.create_variable_expression(expressionParts[1], type="NP")
        elif "int" in rightside:
            rightPart = self.factory.create_integer_literal_expression("NP", int(expressionParts[1]))
        elif "real" in rightside:
            rightPart = self.factory.create_real_literal_expression("NP", float(expressionParts[1]))

        infixOperator = self.factory.create_infix_operator(operator)
        inBetweenOp = None
        if inbetween is not None:
            inBetweenOp = self.factory.create_infix_operator(inbetween)


        opeartion_call_exp = self.factory.create_operation_call_expression(leftPart, rightPart, infixOperator,
                                                                           inBetweenOp)
        self.add_to_root(opeartion_call_exp)


        pass

    def handlePrint(self, root):
        if root == None:
            return
        if hasattr(root, 'arguments'):
            print(root.arguments)
            print(root.get_referred_operation())
            self.handlePrint(root.get_source())

        if hasattr(root,'body'):
            print(root.name)
            print(root.iterator)
            for item in root.body:
                print(item)

