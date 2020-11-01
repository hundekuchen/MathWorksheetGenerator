from LatexHandler import LatexHandler
from AssignmentHandler import AssignmentHandler
from SQLiteHandler import SQLiteHandler

           
if __name__ == '__main__': 
    lh = LatexHandler()
    ah = AssignmentHandler()
    sqlh = SQLiteHandler('mathWorksheet.db')
    assignments = sqlh.select_assignments()
    #print(assignments)
    #for a in assignments:
    #    print('ass = ', a)
    #    ah.add_assignment(a)
    #ah.add_assignment(assignments[0])
    
    
    #TODO import student names database via ERM
    class_id = '2'
    students = sqlh.select_students_from_class(class_id)
    print(students)
    for student in students:
        ah.clear()
        assignments = sqlh.select_assignments_individual(student[0])
        for a in assignments:                
            ah.add_assignment(a)
        lh.generate_test_header(student)
        lh.add_test(ah)
        print('student = ', student[0], '   name ', student[2])
        lh.add_solution(ah)
   
   #=================TESTIN=============
   #================TESTING DONE==========
   
   
    lh.generate_pdf('blub')
    
    
    
            