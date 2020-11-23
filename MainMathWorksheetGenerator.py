from LatexHandler import LatexHandler
from AssignmentHandler import AssignmentHandler
from SQLiteHandler import SQLiteHandler
from fractions import Fraction

def select_whole_class(class_id, assignment_topic):
    #================select for the whole class.
    students = sqlh.select_students_from_class(class_id)
    assignments = sqlh.select_assignments_topic(assignment_topic)
    #print(assignments)

    for student in students:
        for a in assignments:
            #print('ass = ', a)
            ah.add_assignment(a)
        lh.generate_test_header(student)
        lh.add_test(ah)
        lh.draw_grid(17,19)
        lh.newpage()
        lh.generate_test_header(student)
        lh.add_solution(ah)
        ah.clear()
    
def select_individual(class_id):
    students = sqlh.select_students_from_class(class_id)
    print(students)
    for student in students:
        ah.clear()
        assignments = sqlh.select_assignments_individual(student[0])
        for a in assignments:
            for x in range(int(a[8])):#9
                ah.add_assignment(a)
        if(len(ah.assignments)>0):
            lh.generate_test_header(student)
            lh.add_test(ah)
            print('student = ', student[0], '   name ', student[2])
            lh.draw_grid(17,19)
            lh.newpage()
            lh.generate_test_header(student)
            lh.add_solution(ah)
        ah.clear()


if __name__ == '__main__': 
    lh = LatexHandler()
    ah = AssignmentHandler()
    sqlh = SQLiteHandler('mathWorksheet.db')
    #class_id
    select_individual('2')
    #class_id, topic_id
    #select_whole_class('1','1')
   #================TESTING DONE==========
    lh.generate_pdf('20201123VAB1')