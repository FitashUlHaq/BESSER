# Generated from OCLs.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .OCLsParser import OCLsParser
else:
    from OCLsParser import OCLsParser
import inspect


# This class defines a complete listener for a parse tree produced by OCLsParser.
class OCLsListener(ParseTreeListener):
    operator = None

    def __init__(self, rh):
        self.rootHandler = rh
        self.forAllBody = False
        self.operator = []
        self.coll_data = []
        self.debug = True
        self.all_if_else = []

    # Enter a parse tree produced by OCLsParser#oclFile.
    def enterOclFile(self, ctx: OCLsParser.OclFileContext):
        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#oclFile.
    def exitOclFile(self, ctx: OCLsParser.OclFileContext):
        pass

    # Enter a parse tree produced by OCLsParser#ContextExp.
    def enterContextExp(self, ctx: OCLsParser.ContextExpContext):
        self.context = (ctx.getText())
        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#ContextExp.
    def exitContextExp(self, ctx: OCLsParser.ContextExpContext):
        # print(inspect.stack()[0][3])

        pass

    # Enter a parse tree produced by OCLsParser#constraint.
    def enterConstraint(self, ctx: OCLsParser.ConstraintContext):
        self.context_name = (self.context.split(ctx.getText()))[0].replace('context', '')
        self.rootHandler.set_context_name(self.context_name)

    # Exit a parse tree produced by OCLsParser#constraint.
    def exitConstraint(self, ctx: OCLsParser.ConstraintContext):
        pass

    # Enter a parse tree produced by OCLsParser#functionCall.
    def enterFunctionCall(self, ctx: OCLsParser.FunctionCallContext):

        # print(inspect.stack()[0][3])
        # print(ctx.getText())
        pass

    # Exit a parse tree produced by OCLsParser#functionCall.
    def exitFunctionCall(self, ctx: OCLsParser.FunctionCallContext):
        # print(inspect.stack()[0][3])
        pass

    # Enter a parse tree produced by OCLsParser#type.
    def enterType(self, ctx: OCLsParser.TypeContext):
        if self.debug:
            print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#type.
    def exitType(self, ctx: OCLsParser.TypeContext):
        pass

    # Enter a parse tree produced by OCLsParser#collectionType.
    def enterCollectionType(self, ctx: OCLsParser.CollectionTypeContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#collectionType.
    def exitCollectionType(self, ctx: OCLsParser.CollectionTypeContext):
        pass

    # Enter a parse tree produced by OCLsParser#userDefinedType.
    def enterUserDefinedType(self, ctx: OCLsParser.UserDefinedTypeContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#userDefinedType.
    def exitUserDefinedType(self, ctx: OCLsParser.UserDefinedTypeContext):
        pass

    # Enter a parse tree produced by OCLsParser#binary.
    def enterBinary(self, ctx: OCLsParser.BinaryContext):
        # print(inspect.stack()[0][3])
        self.binary = ctx.getText()
        if self.debug:
            print(inspect.stack()[0][3])

        # print(ctx.getText())
        pass

    # Exit a parse tree produced by OCLsParser#binary.
    def exitBinary(self, ctx: OCLsParser.BinaryContext):

        pass

    # Enter a parse tree produced by OCLsParser#unary.
    def enterUnary(self, ctx: OCLsParser.UnaryContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#unary.
    def exitUnary(self, ctx: OCLsParser.UnaryContext):
        pass

    # Enter a parse tree produced by OCLsParser#if.
    # def enterIf(self, ctx: OCLsParser.IfContext):
    #     # print(inspect.stack()[0][3])
    #     print(ctx.getText())
    #     if self.debug:
    #         print(inspect.stack()[0][3])
    #
    #     pass
    #
    # # Exit a parse tree produced by OCLsParser#if.
    # def exitIf(self, ctx: OCLsParser.IfContext):
    #     pass

    # Enter a parse tree produced by OCLsParser#OCLISTYPEOF.
    def enterOCLISTYPEOF(self, ctx: OCLsParser.OCLISTYPEOFContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#OCLISTYPEOF.
    def exitOCLISTYPEOF(self, ctx: OCLsParser.OCLISTYPEOFContext):
        pass

    # Enter a parse tree produced by OCLsParser#OCLASTYPE.
    def enterOCLASTYPE(self, ctx: OCLsParser.OCLASTYPEContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#OCLASTYPE.
    def exitOCLASTYPE(self, ctx: OCLsParser.OCLASTYPEContext):
        pass

    # Enter a parse tree produced by OCLsParser#OCLISKINDOF.
    def enterOCLISKINDOF(self, ctx: OCLsParser.OCLISKINDOFContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#OCLISKINDOF.
    def exitOCLISKINDOF(self, ctx: OCLsParser.OCLISKINDOFContext):
        pass

    # Enter a parse tree produced by OCLsParser#ISEMPTY.
    def enterISEMPTY(self, ctx: OCLsParser.ISEMPTYContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        op_call_exp = self.rootHandler.create_operation_call_exp('IsEmpty')
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.rootHandler.handle_adding_to_root(op_call_exp)

        pass

    # Exit a parse tree produced by OCLsParser#ISEMPTY.
    def exitISEMPTY(self, ctx: OCLsParser.ISEMPTYContext):
        pass

    # Enter a parse tree produced by OCLsParser#SUM.
    def enterSUM(self, ctx: OCLsParser.SUMContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])
        op_call_exp = self.rootHandler.create_operation_call_exp('Sum')
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.rootHandler.handle_adding_to_root(op_call_exp)

        pass

    # Exit a parse tree produced by OCLsParser#SUM.
    def exitSUM(self, ctx: OCLsParser.SUMContext):
        pass

    # Enter a parse tree produced by OCLsParser#SIZE.
    def enterSIZE(self, ctx: OCLsParser.SIZEContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])
        op_call_exp = self.rootHandler.create_operation_call_exp('Size')
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.rootHandler.handle_adding_to_root(op_call_exp)

        pass

    # Exit a parse tree produced by OCLsParser#SIZE.
    def exitSIZE(self, ctx: OCLsParser.SIZEContext):
        pass

    # Enter a parse tree produced by OCLsParser#INCLUDES.
    def enterINCLUDES(self, ctx: OCLsParser.INCLUDESContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#INCLUDES.
    def exitINCLUDES(self, ctx: OCLsParser.INCLUDESContext):
        pass

    # Enter a parse tree produced by OCLsParser#EXCLUDES.
    def enterEXCLUDES(self, ctx: OCLsParser.EXCLUDESContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#EXCLUDES.
    def exitEXCLUDES(self, ctx: OCLsParser.EXCLUDESContext):
        pass

    # Enter a parse tree produced by OCLsParser#SEQUENCE.
    def enterSEQUENCE(self, ctx: OCLsParser.SEQUENCEContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        self.coll_data.append(self.rootHandler.create_sequence())

        pass

    # Exit a parse tree produced by OCLsParser#SEQUENCE.
    def exitSEQUENCE(self, ctx: OCLsParser.SEQUENCEContext):
        op = None
        print(ctx.getText())
        if len(self.operator) != 0:
            op = self.operator.pop()
            if len(self.coll_data) > 0:
                self.rootHandler.handle_adding_to_root(self.coll_data.pop(), op)

        pass

    # Enter a parse tree produced by OCLsParser#SUBSEQUENCE.
    def enterSUBSEQUENCE(self, ctx: OCLsParser.SUBSEQUENCEContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#SUBSEQUENCE.
    def exitSUBSEQUENCE(self, ctx: OCLsParser.SUBSEQUENCEContext):
        pass

    # Enter a parse tree produced by OCLsParser#ALLINSTANCES.
    def enterALLINSTANCES(self, ctx: OCLsParser.ALLINSTANCESContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#ALLINSTANCES.
    def exitALLINSTANCES(self, ctx: OCLsParser.ALLINSTANCESContext):
        pass

    # Enter a parse tree produced by OCLsParser#ORDEREDSET.
    def enterORDEREDSET(self, ctx: OCLsParser.ORDEREDSETContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])
        txt = ctx.getText()
        self.coll_data.append(self.rootHandler.create_ordered_set())

        pass

    # Exit a parse tree produced by OCLsParser#ORDEREDSET.
    def exitORDEREDSET(self, ctx: OCLsParser.ORDEREDSETContext):
        op = None
        if len(self.operator) != 0:
            op = self.operator.pop()
        if len(self.coll_data) > 0:
            self.rootHandler.handle_adding_to_root(self.coll_data.pop(), op)
        pass

    # Enter a parse tree produced by OCLsParser#SUBORDEREDSET.
    def enterSUBORDEREDSET(self, ctx: OCLsParser.SUBORDEREDSETContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.coll_data.append(self.rootHandler.create_sub_ordered_set())
        pass

    # Exit a parse tree produced by OCLsParser#SUBORDEREDSET.
    def exitSUBORDEREDSET(self, ctx: OCLsParser.SUBORDEREDSETContext):
        op = None
        if len(self.operator) != 0:
            op = self.operator.pop()
        if len(self.coll_data) > 0:
            self.rootHandler.handle_adding_to_root(self.coll_data.pop(), op)
        pass

    # Enter a parse tree produced by OCLsParser#SET.
    def enterSET(self, ctx: OCLsParser.SETContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])
        if len(self.coll_data) > 0:
            self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.coll_data.append(self.rootHandler.create_set())

        pass

    # Exit a parse tree produced by OCLsParser#SET.
    def exitSET(self, ctx: OCLsParser.SETContext):
        op = None
        if len(self.operator) != 0:
            op = self.operator.pop()
        if len(self.coll_data) > 0:
            self.rootHandler.handle_adding_to_root(self.coll_data.pop(), op)
        pass

    # Enter a parse tree produced by OCLsParser#BAG.
    def enterBAG(self, ctx: OCLsParser.BAGContext):
        if self.debug:
            print(inspect.stack()[0][3])

        self.coll_data.append(self.rootHandler.create_bag())
        pass

    # Exit a parse tree produced by OCLsParser#BAG.
    def exitBAG(self, ctx: OCLsParser.BAGContext):
        op = None
        if len(self.operator) != 0:
            op = self.operator.pop()
        self.rootHandler.handle_bag(self.coll_data.pop(), op)

        pass

    # Enter a parse tree produced by OCLsParser#PREPEND.
    def enterPREPEND(self, ctx: OCLsParser.PREPENDContext):
        if self.debug:
            print(inspect.stack()[0][3])
        op_call_exp = self.rootHandler.create_operation_call_exp('PREPEND')
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.coll_data.append(op_call_exp)

        pass

    # Exit a parse tree produced by OCLsParser#PREPEND.
    def exitPREPEND(self, ctx: OCLsParser.PREPENDContext):

        self.rootHandler.add_to_root(self.coll_data.pop())
        pass

    # Enter a parse tree produced by OCLsParser#LAST.
    def enterLAST(self, ctx: OCLsParser.LASTContext):
        if self.debug:
            print(inspect.stack()[0][3])
        op_call_exp = self.rootHandler.create_operation_call_exp('Last')
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.rootHandler.handle_adding_to_root(op_call_exp)

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#LAST.
    def exitLAST(self, ctx: OCLsParser.LASTContext):
        pass

    # Enter a parse tree produced by OCLsParser#APPEND.
    def enterAPPEND(self, ctx: OCLsParser.APPENDContext):
        if self.debug:
            print(inspect.stack()[0][3])
        op_call_exp = self.rootHandler.create_operation_call_exp('APPEND')
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.coll_data.append(op_call_exp)

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#APPEND.
    def exitAPPEND(self, ctx: OCLsParser.APPENDContext):
        self.rootHandler.add_to_root(self.coll_data.pop())
        pass

    # Enter a parse tree produced by OCLsParser#COLLECTION.
    def enterCOLLECTION(self, ctx: OCLsParser.COLLECTIONContext):

        if self.debug:
            print(inspect.stack()[0][3])

        self.rootHandler.handle_collection(ctx.getText())
        # print(inspect.stack()[0][3])

    # Exit a parse tree produced by OCLsParser#COLLECTION.
    def exitCOLLECTION(self, ctx: OCLsParser.COLLECTIONContext):
        # print("exitCOLLECTION")
        self.rootHandler.pop()
        pass

    # Enter a parse tree produced by OCLsParser#CollectionExpressionVariable.
    def enterCollectionExpressionVariable(self, ctx: OCLsParser.CollectionExpressionVariableContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        self.rootHandler.handle_collection(ctx.getText())
        pass

    # Exit a parse tree produced by OCLsParser#CollectionExpressionVariable.
    def exitCollectionExpressionVariable(self, ctx: OCLsParser.CollectionExpressionVariableContext):
        # print("exitCollectionExpressionVariable")
        self.rootHandler.pop()
        pass

    # Enter a parse tree produced by OCLsParser#SYMMETRICDIFFERENCE.
    def enterSYMMETRICDIFFERENCE(self, ctx: OCLsParser.SYMMETRICDIFFERENCEContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#SYMMETRICDIFFERENCE.
    def exitSYMMETRICDIFFERENCE(self, ctx: OCLsParser.SYMMETRICDIFFERENCEContext):
        pass

    # Enter a parse tree produced by OCLsParser#FIRST.
    def enterFIRST(self, ctx: OCLsParser.FIRSTContext):
        if self.debug:
            print(inspect.stack()[0][3])
        op_call_exp = self.rootHandler.create_operation_call_exp('First')
        self.rootHandler.handle_adding_to_root(self.coll_data.pop())
        self.rootHandler.handle_adding_to_root(op_call_exp)

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#FIRST.
    def exitFIRST(self, ctx: OCLsParser.FIRSTContext):
        pass

    # Enter a parse tree produced by OCLsParser#DERIVE.
    def enterDERIVE(self, ctx: OCLsParser.DERIVEContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#DERIVE.
    def exitDERIVE(self, ctx: OCLsParser.DERIVEContext):
        pass

    # Enter a parse tree produced by OCLsParser#UNION.
    def enterUNION(self, ctx: OCLsParser.UNIONContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#UNION.
    def exitUNION(self, ctx: OCLsParser.UNIONContext):
        pass

    # Enter a parse tree produced by OCLsParser#defExp.
    def enterDefExp(self, ctx: OCLsParser.DefExpContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#defExp.
    def exitDefExp(self, ctx: OCLsParser.DefExpContext):
        pass

    # Enter a parse tree produced by OCLsParser#defIDAssignmentexpression.
    def enterDefIDAssignmentexpression(self, ctx: OCLsParser.DefIDAssignmentexpressionContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#defIDAssignmentexpression.
    def exitDefIDAssignmentexpression(self, ctx: OCLsParser.DefIDAssignmentexpressionContext):
        pass

    # Enter a parse tree produced by OCLsParser#PrimaryExp.
    def enterPrimaryExp(self, ctx: OCLsParser.PrimaryExpContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        # print(ctx.getText())

        pass

    # Exit a parse tree produced by OCLsParser#PrimaryExp.
    def exitPrimaryExp(self, ctx: OCLsParser.PrimaryExpContext):
        # #print("exitPrimaryExp")
        # #print(ctx.getText())
        # input()
        # if len(self.operator) !=0 and self.operator[-1] in ctx.getText():
        #
        #     self.rootHandler.handlePrimaryExp(ctx.getText(),self.operator[-1])
        pass

    # Enter a parse tree produced by OCLsParser#funcCall.
    def enterFuncCall(self, ctx: OCLsParser.FuncCallContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#funcCall.
    def exitFuncCall(self, ctx: OCLsParser.FuncCallContext):
        pass

    # Enter a parse tree produced by OCLsParser#op.
    def enterOp(self, ctx: OCLsParser.OpContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # self.operator.append(ctx.getText())
        pass

    # Exit a parse tree produced by OCLsParser#op.
    def exitOp(self, ctx: OCLsParser.OpContext):
        pass

    # Enter a parse tree produced by OCLsParser#arrowexp.
    def enterArrowexp(self, ctx: OCLsParser.ArrowexpContext):
        if self.debug:
            print(inspect.stack()[0][3])

        # print(inspect.stack()[0][3])
        pass

    # Exit a parse tree produced by OCLsParser#arrowexp.
    def exitArrowexp(self, ctx: OCLsParser.ArrowexpContext):
        pass

    # Enter a parse tree produced by OCLsParser#number.
    def enterNumber(self, ctx: OCLsParser.NumberContext):
        if self.debug:
            print(inspect.stack()[0][3])
        item = self.rootHandler.get_factory().create_collection_item("item", ctx.getText())
        self.coll_data[-1].add(item)
        pass

    # Exit a parse tree produced by OCLsParser#number.
    def exitNumber(self, ctx: OCLsParser.NumberContext):
        pass

    # Enter a parse tree produced by OCLsParser#PredefinedfunctionCall.
    def enterPredefinedfunctionCall(self, ctx: OCLsParser.PredefinedfunctionCallContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#PredefinedfunctionCall.
    def exitPredefinedfunctionCall(self, ctx: OCLsParser.PredefinedfunctionCallContext):
        pass

    # Enter a parse tree produced by OCLsParser#ID.
    def enterID(self, ctx: OCLsParser.IDContext):
        # print(inspect.stack()[0][3])
        print(ctx.getText())
        txt = ctx.getText()
        if self.debug:
            print(inspect.stack()[0][3])
        if len(self.coll_data) != 0:
            item = self.rootHandler.get_factory().create_collection_item("item", ctx.getText())
            self.coll_data[-1].add(item)
        else:
            self.rootHandler.handle_ID(ctx.getText())
        pass

    # Exit a parse tree produced by OCLsParser#ID.
    def exitID(self, ctx: OCLsParser.IDContext):
        pass

    # Enter a parse tree produced by OCLsParser#SingleQuoteExp.
    def enterSingleQuoteExp(self, ctx: OCLsParser.SingleQuoteExpContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#SingleQuoteExp.
    def exitSingleQuoteExp(self, ctx: OCLsParser.SingleQuoteExpContext):
        pass

    # Enter a parse tree produced by OCLsParser#doubleDots.
    def enterDoubleDots(self, ctx: OCLsParser.DoubleDotsContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#doubleDots.
    def exitDoubleDots(self, ctx: OCLsParser.DoubleDotsContext):
        pass

    # Enter a parse tree produced by OCLsParser#binaryExpression.
    def enterBinaryExpression(self, ctx: OCLsParser.BinaryExpressionContext):

        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#binaryExpression.
    def exitBinaryExpression(self, ctx: OCLsParser.BinaryExpressionContext):
        # print(inspect.stack()[0][3])

        and_or = self.binary.split(ctx.getText())[0]
        # print(and_or)
        inBetween_op = None
        if "and" or "or" in and_or:
            inBetween_op = and_or
        if len(self.operator) != 0:
            text_to_process = ctx.getText()
            if "()" in text_to_process:
                text_to_process = ctx.parentCtx.parentCtx.getText()
            self.rootHandler.handle_binary_expression(text_to_process, self.operator.pop(), inBetween_op)
            # self.operator.pop()

        pass

    # Enter a parse tree produced by OCLsParser#unaryExpression.
    def enterUnaryExpression(self, ctx: OCLsParser.UnaryExpressionContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#unaryExpression.
    def exitUnaryExpression(self, ctx: OCLsParser.UnaryExpressionContext):
        pass

    # Enter a parse tree produced by OCLsParser#operator.
    def enterOperator(self, ctx: OCLsParser.OperatorContext):
        if self.debug:
            print(inspect.stack()[0][3])

        self.operator.append(ctx.getText())

        pass

    # Exit a parse tree produced by OCLsParser#operator.
    def exitOperator(self, ctx: OCLsParser.OperatorContext):
        pass

    # Enter a parse tree produced by OCLsParser#numberORUserDefined.
    def enterNumberORUserDefined(self, ctx: OCLsParser.NumberORUserDefinedContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#numberORUserDefined.
    def exitNumberORUserDefined(self, ctx: OCLsParser.NumberORUserDefinedContext):
        pass

    # Enter a parse tree produced by OCLsParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: OCLsParser.PrimaryExpressionContext):
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: OCLsParser.PrimaryExpressionContext):
        # if len(self.operator) != 0:
        #     self.rootHandler.handlePrimaryExp(ctx.getText(),self.operator[-1])
        #     self.operator.pop()
        pass

    # Enter a parse tree produced by OCLsParser#literal.
    def enterLiteral(self, ctx: OCLsParser.LiteralContext):
        # print(inspect.stack()[0][3])
        if self.debug:
            print(inspect.stack()[0][3])

        pass

    # Exit a parse tree produced by OCLsParser#literal.
    def exitLiteral(self, ctx: OCLsParser.LiteralContext):
        pass

    def print(self):
        self.rootHandler.print()

    def enterIfExp(self, ctx: OCLsParser.IfExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        self.all_if_else.append(self.rootHandler.create_if_else_exp('if', 'IfExpression'))

        pass

    # Exit a parse tree produced by OCLsParser#ifExp.
    def exitIfExp(self, ctx: OCLsParser.IfExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        pass

    # Enter a parse tree produced by OCLsParser#thenExp.
    def enterThenExp(self, ctx: OCLsParser.ThenExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        pass
        top = self.rootHandler.getTop()
        self.all_if_else[-1].ifCondition=top

    # Exit a parse tree produced by OCLsParser#thenExp.
    def exitThenExp(self, ctx: OCLsParser.ThenExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        pass

    # Enter a parse tree produced by OCLsParser#elseExp.
    def enterElseExp(self, ctx: OCLsParser.ElseExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        self.all_if_else[-1].thenCondition=self.rootHandler.getTop()
        pass

    # Exit a parse tree produced by OCLsParser#elseExp.
    def exitElseExp(self, ctx: OCLsParser.ElseExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        pass

    # Enter a parse tree produced by OCLsParser#endIfExp.
    def enterEndIfExp(self, ctx: OCLsParser.EndIfExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        pass

        self.all_if_else[-1].elseCondition = self.rootHandler.getTop(True)
        self.rootHandler.add_to_root(self.all_if_else.pop())

    # Exit a parse tree produced by OCLsParser#endIfExp.
    def exitEndIfExp(self, ctx: OCLsParser.EndIfExpContext):
        if self.debug:
            print(inspect.stack()[0][3])
        pass


del OCLsParser