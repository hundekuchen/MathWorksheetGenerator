# importing from a pylatex module 
#from pylatex import Package, Document, Tabular, MiniPage 
#from pylatex import TikZ, Axis, Plot, Figure, Matrix, Alignat, Enumerate, Itemize
from pylatex import *
from pylatex.utils import NoEscape
#from AssignmentHandler import AssignmentHandler

class LatexHandler:
    def __init__(self):
        self.geometry_options = {"tmargin": "1cm", "lmargin": "1cm"} 
        self.doc = Document(geometry_options=self.geometry_options)
        self.doc.packages.append(Package('tikz'))
        #Ziffer package for german , Notation( 1,2 vs 1, 3  )
        self.doc.packages.append(Package('ziffer'))
        self.doc.append(NoEscape(r'\pagestyle{empty}'))
        #self.doc.append('blub')
        
        
    def draw_grid(self,x,y):
        with self.doc.create(MiniPage(width=r"0.5\linewidth")):
            self.doc.append(NoEscape(r' \tikz \draw[step=0.5cm,gray](0,0)grid(' + str(x) + ', ' + str(y) + ');'))
    
    #student: 0 - id, 1 - first, 2 - last,  3 - class 
    def generate_test_header(self, student):
        with self.doc.create(Tabular('|p{5cm}|p{5cm}|p{5cm}|')) as table:
            table.add_hline()
            table.add_row('Fach: Mathematik','Test', NoEscape(r'\today'))
            table.add_hline()
            table.add_empty_row()
            student_string = str(student[1])+ ' ' + str(student[2])
            table.add_row(('Name: '+ student_string ,'Punkte: ' ,'Note: '))
            table.add_hline()
              
    def generate_pdf(self,pdf_name):
        self.doc.generate_pdf(pdf_name, clean_tex=False) 

    def add_test(self, ah):
        with self.doc.create(Enumerate()) as enum:
            for a in ah.assignments:
                enum.add_item(NoEscape('$'+a.latex_question + '$'))
                self.doc.append(NoEscape(r'\newline'))      
                #self.draw_grid(15,4)
        #self.doc.append(NoEscape(r'\newpage'))
        
    def add_solution(self, ah):
        #  use database approach here.
        with self. doc.create(Section('Lösungen', numbering = False, label = False)):
            with self.doc.create(Enumerate()) as enum:
                for a in ah.assignments:
                    enum.add_item(NoEscape('$'+a.latex_solution + '$'))
                    #self.doc.append(NoEscape(r'\newline'))      
                    #self.draw_grid(10,4)
            self.doc.append(NoEscape(r'\newpage'))
