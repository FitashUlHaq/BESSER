class OclIndividual:

    def __init__(self):
        self.context = ""
        self.orig_ocl_exp = ""
        self.operator = None
        self.left = None
        self.right = None
    def get_operator (self):
        return self.operator

    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def get_context(self):
        return self.context
    def set_context(self,con):
        self.context = con
    def set_left(self,left):
        self.left = left
    def set_right(self,right):
        self.right = right
    def set_operator(self, op):
        self.operator = op