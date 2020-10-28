# Python program creating a 
# small document using pylatex 
  
import numpy as np
import random
  
# importing from a pylatex module 
from pylatex import Package, Document, Section, Subsection, Tabular, MiniPage 
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Enumerate, Itemize
from pylatex.utils import italic, NoEscape
import os 

import random

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

def sign_num(a, b):
    n = random.randint(a, b)
    if random.random() < 0.5:
        return '(-{})'.format(n)
    else:
        return str(n)

def num(a, b):
    return str(random.randint(a,b))

def add(a, b, parens=False):
    n1 = num(a, b)
    n2 = num(a, b)
    if parens:
        return '({} + {})'.format(n1, n2)
    else:
        return '{} + {}'.format(n1, n2)

def sign_add(a, b, parens=False):
    n1 = sign_num(a, b)
    n2 = sign_num(a, b)
    if parens:
        return '({} + {})'.format(n1, n2)
    else:
        return '{} + {}'.format(n1, n2)

dico = {'NUM': num, 'SIGNNUM': sign_num, 'ADD': add, 'SIGN_ADD': sign_add}

def fill_in(txt):
    argv = txt.strip().split()
    return dico[argv[0]](int(argv[1]), int(argv[2]))

def parse(txt):
    if '[' not in txt:
        return txt
    else:
        i = txt.index('[')
        j = txt.index(']')
        return txt[:i] + fill_in(txt[i+1:j])  + parse(txt[j+1:])

 
def draw_grid(x,y):
    with doc.create(MiniPage(width=r"0.5\linewidth")):
        doc.append(NoEscape(r' \tikz \draw[step=0.5cm,gray](0,0)grid(' + str(x) + ', ' + str(y) + ');'))

def add_test():
#  use database approach here.
    assignments = ['[SIGNNUM 3 19]*( + [ADD -3  6])', '1/(3*x+2*x)']
    
    with doc.create(Enumerate()) as enum:
        for a in assignments:
            b= parse(a)
            x = assignment(b)
            print(x.latex_question)
            enum.add_item(NoEscape('$'+x.latex_question + '$'))
            doc.append(NoEscape(r'\newline'))      
            draw_grid(10,4)
            #doc.append(NoEscape(r'\newline'))
            
            
if __name__ == '__main__': 
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"} 
    doc = Document(geometry_options=geometry_options)
    doc.packages.append(Package('tikz'))
    students=['Peter','Hannes', 'Hugo']
    for student in students:
        with doc.create(Tabular('|p{5cm}|p{5cm}|p{5cm}|')) as table:
            table.add_hline()
            table.add_row('Fach: Mathematik','Test', NoEscape(r'\today'))
            table.add_hline()
            table.add_empty_row()
            table.add_row(('Name: '+ student ,'Punkte: ' ,'Note: '))
            table.add_hline()
            #doc.append(NoEscape(r'\newline'))
        add_test()
        doc.append(NoEscape(r'\thispagestyle{empty}'))
        doc.append(NoEscape(r'\newpage'))
            
    doc.generate_pdf('full', clean_tex=False) 