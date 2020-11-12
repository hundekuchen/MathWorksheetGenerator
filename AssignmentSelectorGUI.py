from SQLiteHandler import SQLiteHandler
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import *
  
#=============TESTING========================
sqlh = SQLiteHandler('mathWorksheet.db')

top = tkinter.Tk()

svar = IntVar()
cvar = IntVar()
student_buttons=[]
class_buttons=[]

current_class = 0
current_student=0

ass_box = Listbox(top)


classes = sqlh.select_all_classes()
print(classes)

def select_class():
    current_class=str(cvar.get())
    for sbutton in student_buttons:
        sbutton.destroy()
    student_buttons.clear()
    update_students(int(current_class))
    print(current_class)

def select_student():
    current_student=str(svar.get())
    update_assignment_list(current_student)
    #print(current_student)

def update_students(class_id):
    student_buttons.clear()
    students = sqlh.select_students_from_class(class_id)
    print(students)
    for student in students:
        student_buttons.append(Radiobutton(top, text = str(student[0]) + ' ' + str(student[1])+' ' + str(student[2]), variable = svar, value = student[0], command = select_student))
    current_row = 0
    for button in student_buttons:
        button.grid(row = current_row, column = 1, sticky = W)
        current_row+=1
        
def update_assignment_list(current_student):
    ass_box.delete(0,'end')
    print(current_student)
    assignments = sqlh.select_assignments_individual(current_student)
    print(assignments)
    i=1
    for assignment in assignments:
        ass_box.insert(i,assignment[3])
        ass_box.grid(column=5, sticky=W+N)
        i+=1





#update_students(1)

for sclass in classes:
    class_buttons.append(Radiobutton(top, text = str(sclass[0]) + ' '+ str(sclass[1]), variable = cvar, value = sclass[0],
                  command = select_class))



current_row=0
for button in class_buttons:
    button.grid(row = current_row, column = 0, sticky = W)
    current_row+=1




top.mainloop()