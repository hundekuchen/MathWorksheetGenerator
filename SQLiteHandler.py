import sqlite3
from sqlite3 import Error

class SQLiteHandler:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)
        #TODO shut connection down when done (conn.close())

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn
    
    def select_assignments(self):
        cur = self.conn.cursor()
        cur.execute("SELECT assignmentPyString FROM assignment")
        assignments_raw = cur.fetchall()
        assignments_usable = []
        for a in assignments_raw:
            assignments_usable.append(a[0])
        return assignments_usable
    
    def select_students_from_class(self, my_class):
        cur = self.conn.cursor()
        cur.execute("SELECT StudentFirstName, StudentLastName FROM students")
        assignments_raw = cur.fetchall()
        assignments_usable = []
        for a in assignments_raw:
            assignments_usable.append(a[0]+ ', ' + a[1])
        return assignments_usable
            
        
        
        
    
#=============TESTING========================
#sqlh = SQLiteHandler('mathWorksheet.db')
#sqlh.select_assignments(sqlh.conn)
    