#import sympy
from sympy import sympify
from sympy import init_printing
from sympy import *
from RandomHandler import RandomHandler 
init_printing()

class assignment:
    def __init__(self, inputString):
        self.sympy_question = sympify(inputString, evaluate = False)
        self.latex_question = latex(self.sympy_question)
        self.sympy_solution = simplify(self.sympy_question)
        self.latex_solution = (latex(self.sympy_solution))

class AssignmentHandler:
    def __init__(self):
        self.assignments = []
    
    def add_assignment(self, assignment_string):
        rh = RandomHandler()
        print('assignment_string = ', assignment_string)
        parsed_string=rh.parse(assignment_string)
        print('parsed_string = ', parsed_string)
        a = assignment(parsed_string)
        print('Latex_question = ', a.latex_question)
        self.assignments.append(a)
        
#===========TESTING=======================
#ah = AssignmentHandler()
#ah.add_assignment('([SIGNNUM 2 6][SIGN 1 2] [NUM 4 10]*x)*([SIGNNUM 2 6][SIGN 1 2][NUM 4 10]*x)')
#a = assignment('(4+5*x)*(5-9*x)')
#a=simplify('123.123/123')
#print('123.123/123 = ', a)


    