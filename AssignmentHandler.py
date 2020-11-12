#import sympy
from sympy import sympify
from sympy import init_printing
from sympy import *

from enum import Enum

from RandomHandler import RandomHandler 
init_printing()

x, y, z = symbols('x y z')

class assignment:
    #assignment-list: 0 - id, 1 - topic, 2 - description, 3 - pystring, 4 - assignmenttype
    def __init__(self, assign_input):
        self.sympy_question = ''#sympify(assign_input[3], evaluate = False)
        self.latex_question = ''
        self.question_handling(assign_input)
        self.sympy_solution = self.to_sympy_solution(self.sympy_question, assign_input)
        self.latex_solution = self.to_latex_solution(assign_input)
    

    
    #with ':'
    def question_handling(self, assign_input):
        #sympy handling
        rh=RandomHandler()
        parsed_string = rh.parse(assign_input[3])
        sympyq_string =parsed_string.replace(':', '/')
        sympyq_string =sympify(sympyq_string, evaluate = False)
        #print('sympy string ', sympyq_string)
        self.sympy_question = sympyq_string
        
        #latex handling
        split_assign = parsed_string.split(':')
        #print('split assign = ', split_assign)
        latex_string = ''
        #todo - make this work for multiple ":"s.
        if(len(split_assign)==2):
            latex_string= latex(sympify(split_assign[0],evaluate = False)) + ':' + latex(sympify(split_assign[1], evaluate = False))
        else:
            latex_string = latex(sympify(split_assign[0], evaluate = False))
        #print('latex_string = ', latex_string)
        latex_string = latex_string.replace('.',',')
        self.latex_question = latex_string

    def to_latex(self, assign_input):
        parsed_string=self.sympy_question
        #print('parsed string = ', parsed_string)
        split_assign = parsed_string.split(':')
        #print('split assign = ', split_assign)
        latex_string = ''
        #todo - make this work for multiple ":"s.
        if(len(split_assign)==2):
            latex_string= latex(sympify(split_assign[0], evaluate = False)) + ':' + latex(sympify(split_assign[1], evaluate = False))
        else:
            latex_string = latex(sympify(split_assign[0], evaluate = False))
        #print('latex_string = ', latex_string)
        return latex_string
                
    #assign_input 1 - simplify, 2 - evaluate
    def to_sympy_solution(self, sp_q, assign_input):
        if(assign_input[4]==1):
            return expand(simplify(sp_q))
        elif(assign_input[4]==2):
            return simplify(sp_q)
        else :
            return '0000'
        
    def to_latex_solution(self, assign_input):
        if(assign_input[4]==1):
            return latex(self.sympy_solution)
        elif(assign_input[4]==2):
            out_string = (str(latex(self.sympy_solution)) + ' = ' + str(latex(N(self.sympy_solution)))).replace('.',',')
            return out_string
        else :
            return '0000'
                    
                
            
    #assignment types: 1 - simplify, 2 - solve, ...
    #def input_to_sympy(inputString, assignment_type):
        
        
        

class AssignmentHandler:
    def __init__(self):
        self.assignments = []
    
    def add_assignment(self, assign_input):
        rh = RandomHandler()
        a = assignment(assign_input)
        self.assignments.append(a)
        
    def clear(self):
        self.assignments.clear()
    
        
#===========TESTING=======================
#ah = AssignmentHandler()
#ah.add_assignment((1, 1, 'blub', '([SIGNNUM 2 6][SIGN 1 2] [NUM 4 10]*x + [NUM 3 12]*y)*([SIGNNUM 2 6][SIGN 1 2][NUM 4 10]*x+[NUM 5 12]*y)', 1))
#print(expand(ah.assignments[0].sympy_question))
#a=simplify('123.123/123')
#print('123.123/123 = ', a)


    