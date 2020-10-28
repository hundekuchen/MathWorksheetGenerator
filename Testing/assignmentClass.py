import sympy
from sympy import sympify
from sympy import init_printing
from sympy import *
init_printing()

class assignment:
    def __init__(self, inputString):
        self.sympy_question = sympify(inputString, evaluate = False)
        self.latex_question = latex(self.sympy_question) 
        self.sympy_solution = simplify(self.sympy_question)
        self.latex_solution = (latex(self.sympy_solution))

a = assignment("1/(3*x+2*x)")
print("latex_question", a.latex_question)
print("latex_solution", a.latex_solution)