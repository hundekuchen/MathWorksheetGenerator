from SQLiteHandler import SQLiteHandler
from AssignmentHandler import AssignmentHandler
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import *
from io import BytesIO
import sympy as sp
from PIL import Image, ImageTk
  
#=============TESTING========================
sqlh = SQLiteHandler('mathWorksheet.db')

top = tkinter.Tk()

svar = IntVar()
cvar = IntVar()
student_buttons=[]
class_buttons=[]

current_class = '0'
current_student= '0'

ass_box = Listbox(top, width = 70)
ass_box_available = Listbox(top, width = 70)

def remove_assignment(event):
    global current_class
    print("class", current_class, "    student", current_student)

def add_assignment(event):
    print("ass = ", ass_box_available.get(ass_box_available.curselection()))
    global sqlh
    #DIRTY FIX
    ab = ass_box_available.curselection()
    a_index = ab[0]+5
    print("ass dirty ", a_index) 
    assignment_index = ass_box
    sqlh.add_assignment_individual(current_student, str(a_index))
    print("class", current_class, "    student", current_student)
    


ass_box.bind('<Double-1>', remove_assignment)
ass_box_available.bind('<Double-1>', add_assignment)

classes = sqlh.select_all_classes()
print(classes)


    


def select_class():
    global current_class
    current_class=str(cvar.get())
    for sbutton in student_buttons:
        sbutton.destroy()
    student_buttons.clear()
    update_students(int(current_class))
    print("class", current_class, "    student", current_student)

def select_student():
    global current_student
    current_student=str(svar.get())
    update_assignment_list(current_student)

def update_students(class_id):
    student_buttons.clear()
    students = sqlh.select_students_from_class(class_id)
    for student in students:
        student_buttons.append(Radiobutton(top, text = str(student[0]) + ' ' + str(student[1])+' ' + str(student[2]), variable = svar, value = student[0], command = select_student))
    current_row = 0
    for button in student_buttons:
        button.grid(row = current_row, column = 1, sticky = W)
        current_row+=1
        
def update_assignment_list(current_student):
    ass_box.delete(0,'end')
    assignments = sqlh.select_assignments_individual(current_student)
    ah=AssignmentHandler()
    i=0
    for assignment in assignments:
        ah.add_assignment(assignment)
        ass_box.insert(i, assignment[2])
        i+=0
    ass_box.grid(row=0, column=5)
           
def on_latex(event):
    cs=listbox.curselection()
    latex_string = listbox.get(cs)
    print(latex_string)
    expr = "$\displaystyle " + latex_string + "$"

    #This creates a ByteIO stream and saves there the output of sympy.preview
    f = BytesIO()
    the_color = "{" + top.cget('bg')[1:].upper()+"}"
    sp.preview(expr, euler = False, preamble = r"\documentclass{standalone}"
                   r"\begin{document}",
                   viewer = "BytesIO", output = "ps", outputbuffer=f)
    f.seek(0)
        #Open the image as if it were a file. This works only for .ps!
    img = Image.open(f)
        #See note at the bottom
    img.load(scale = 10)
    img = img.resize((int(img.size[0]/4),int(img.size[1]/4)),Image.BILINEAR)
    photo = ImageTk.PhotoImage(img)
    label.config(image = photo)
    label.image = photo
    f.close()

#update_students(1)
#GUI
#class ui
for sclass in classes:
    class_buttons.append(Radiobutton(top, text = str(sclass[0]) + ' '+ str(sclass[1]), variable = cvar, value = sclass[0],
                  command = select_class, width=50))

current_row=0
for button in class_buttons:
    button.grid(row = current_row, column = 0, sticky = W)
    current_row+=1
    

assign = sqlh.select_assignments_topic(2)
print(assign)
i=0
for a in assign:
    ass_box_available.insert(i, a[2])
    i+=1

ass_box_available.grid(row=0, column=9)

#label for latex
label = Label(top)
label.grid(row=0, column=11)

top.mainloop()