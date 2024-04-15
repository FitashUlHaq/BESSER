import sys
from antlr4 import *
from besser.BUML.notations.ocl.BOCLLexer import BOCLLexer
from besser.BUML.notations.ocl.BOCLParser import BOCLParser
from besser.BUML.notations.ocl.BOCLListener import BOCLListener
from besser.BUML.notations.ocl.RootHandler import Root_Handler
import unittest

class TestOclInterpreter(unittest.TestCase):

    def test_meeting_inv(self):
        ocl = "context meeting inv: self.start < self.end and self.start < 5"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() !=None

    def test_meeting_inv_two(self):
        ocl = "context meeting inv: self.start < self.end and self.start < 5  or self.end > 10"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() !=None
    def test_meeting_inv_three(self):
        ocl = "context meeting inv: self.start < self.end"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() !=None

    def test_invariant_LoyaltyProgram16(self):
        ocl = "context temp inv invariant_LoyaltyProgram16 : self.participants->forAll( i_Customer : Customer | i_Customer.age() <= 70 )"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() !=None

    def test_select(self):
        ocl = "context temp inv invariant_LoyaltyProgram16 : self.employee->select(age > 50)"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None
    def test_select_2(self):
        ocl = "context temp inv invariant_LoyaltyProgram16 : self.employee->select( p | p.age>50 )"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_select_three(self):
        ocl = "context temp inv invariant_LoyaltyProgram16 : self.employee->select( p : Personne | p.age>50)"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_forAll(self):
        ocl = "context temp inv invariant_LoyaltyProgram16 : self.employee->forAll(age<10)"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None
    def test_exists(self):
        ocl = "context temp inv invariant_LoyaltyProgram16 : self.employee->exists(age<10)"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_collect(self):
        ocl = "context temp inv invariant_LoyaltyProgram16 : self.employee->collect(age)  = Bag{10,5,10,7}"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_prepend(self):
        ocl = "context ServiceLevel inv invariant_ServiceLevel19 :	(Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->prepend('X')) = Sequence{'X', 'a', 'b', 'c', 'c', 'd', 'e'}"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_sub_ordered_set(self):
        ocl = "context S inv invariant_ServiceLevel17 :(OrderedSet{'a', 'b', 'c', 'd'}->subOrderedSet(2, 3)) = OrderedSet{'b', 'c'}"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None
    def test_if_else(self):
        ocl = "context S inv invariant_ServiceLevel17 :if durationInHours<40 then durationInHours > 1000 else durationInHours > 2000 endif"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_oclIsTypeOf(self):
        ocl = "context S inv invariant_ServiceLevel17 :durationInHours.oclIsTypeOf(Integer)"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None
    def test_oclIsKindOf(self):
        ocl = "context S inv invariant_ServiceLevel17 :durationInHours.oclIsKindOf(Integer)"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def oclAsType(self):
        ocl = "context S inv invariant_ServiceLevel17 :durationInHours.oclAsType(Integer)"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_boolean(self):
        ocl = "context meeting inv: self.start = True"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_includes(self):
        ocl = "context ServiceLevel inv invariant_ServiceLevel19 :	(Sequence{'a', 'b', 'c', 'c', 'd', 'e'}->includes('X'))"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_exists(self):
        ocl = "context meeting inv: Paper::allInstances()->exists(p | p.studentPaper) and Paper::allInstances()->select(p | p.studentPaper)->size() < 5"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_post(self):
        ocl = "context Meeting::duration():Integer post: result = self.next.start3@pre + self.start - self.start2-self.test2"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None
    def test_body(self):
        ocl = "context Meeting::duration():Integer body: result = self.next.start3@pre + self.start - self.start2-self.test2"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_pre(self):
        ocl = "context Meeting::duration():Integer pre: result = self.next.start3@pre + self.start - self.start2-self.test2"
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None
    def test_isEmpty(self):
        ocl = ("context temp inv invariant_LoyaltyProgram16 : "
               "self.employee->isEmpty()")
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_size(self):
        ocl = ("context temp inv invariant_LoyaltyProgram16 : "
               "self.employee->size()<3")
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_sum(self):
        ocl = ("context temp inv invariant_LoyaltyProgram16 : "
               "self.employee->sum()<3")
        input_stream = InputStream(ocl)
        rootHandler = Root_Handler()
        lexer = BOCLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BOCLParser(stream)
        tree = parser.oclFile()
        listener = BOCLListener(rootHandler)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        assert rootHandler.get_root() != None

    def test_excludes_researcher(self):
            ocl = ("context Researcher inv NoSelfReviews: self.submission -> excludes(self.manuscript")
            input_stream = InputStream(ocl)
            rootHandler = Root_Handler()
            lexer = BOCLLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = BOCLParser(stream)
            tree = parser.oclFile()
            listener = BOCLListener(rootHandler)
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            assert rootHandler.get_root() != None
    def test_excludes_PaperLength(self):
            ocl = ("context Paper inv PaperLength:self.wordCount < 10000")
            input_stream = InputStream(ocl)
            rootHandler = Root_Handler()
            lexer = BOCLLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = BOCLParser(stream)
            tree = parser.oclFile()
            listener = BOCLListener(rootHandler)
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            assert rootHandler.get_root() != None


    def test_AuthorsOfStudentPaper(self):
            ocl = ("context Paper inv AuthorsOfStudentPaper:self.studentPaper = self.author->exists(x | x.isStudent )")
            input_stream = InputStream(ocl)
            rootHandler = Root_Handler()
            lexer = BOCLLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = BOCLParser(stream)
            tree = parser.oclFile()
            listener = BOCLListener(rootHandler)
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            assert rootHandler.get_root() != None

    def test_AuthorsOfStudentPaper(self):
            ocl = ("context Paper inv NoStudentReviewers:self.referee->forAll(r | not r.isStudent)")
            input_stream = InputStream(ocl)
            rootHandler = Root_Handler()
            lexer = BOCLLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = BOCLParser(stream)
            tree = parser.oclFile()
            listener = BOCLListener(rootHandler)
            walker = ParseTreeWalker()
            walker.walk(listener, tree)
            assert rootHandler.get_root() != None
if __name__ == '__main__':
    pass