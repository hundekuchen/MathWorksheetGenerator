from LatexHandler import LatexHandler
from AssignmentHandler import AssignmentHandler
from SQLiteHandler import SQLiteHandler

           
if __name__ == '__main__': 
    lh = LatexHandler()
    ah = AssignmentHandler()
    sqlh = SQLiteHandler('mathWorksheet.db')
    assignments = sqlh.select_assignments()
    #print(assignments)
    #TODO import assignments from sqlite database
    for a in assignments:
        print('ass = ', a)
        ah.add_assignment(a)
    
    #TODO import student names database via ERM
    students = sqlh.select_students_from_class('blub')
    for student in students:
        lh.generate_test_header(student)
        lh.add_test(ah)
        lh.add_solution(ah)
    lh.generate_pdf('blub')
            