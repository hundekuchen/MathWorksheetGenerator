# Python program creating a 
# small document using pylatex 
  
import numpy as np 
  
# importing from a pylatex module 
from pylatex import Package, Document, Section, Subsection, Tabular, MiniPage 
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat 
from pylatex.utils import italic, NoEscape
import os 

def draw_grid(x,y):
    with doc.create(MiniPage(width=r"0.5\linewidth")):
        doc.append(NoEscape(r' \tikz \draw[step=0.5cm,gray](0,0)grid(14,8);'))
 
if __name__ == '__main__': 
    geometry_options = {"tmargin": "1cm", "lmargin": "1cm"} 
    doc = Document(geometry_options=geometry_options)
    doc.packages.append(Package('tikz'))
    students=['Peter','Hannes', 'Hugo']
    doc.append('blub')
    doc.append(NoEscape(r'\newpage'))
    for student in students:
        with doc.create(Tabular('|p{5cm}|p{5cm}|p{5cm}|')) as table:
            table.add_hline()
            table.add_row('Fach: Mathematik','Test', NoEscape(r'\today'))
            table.add_hline()
            table.add_empty_row()
            table.add_row(('Name: '+ student ,'Punkte: ' ,'Note: '))
            table.add_hline()
        doc.append(NoEscape(r'\newline'))
        draw_grid(5,7)
        doc.append(NoEscape(r'\thispagestyle{empty}'))
        doc.append(NoEscape(r'\newline'))
        doc.append(NoEscape(r'\newpage'))
            
    doc.generate_pdf('full', clean_tex=False) 