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
   
   #TODO lots of copy paste code below -- :(
   
    def select_assignments(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM assignment")
        assignments_raw = cur.fetchall()
        print(assignments_raw)
        return assignments_raw
    
    def select_students_from_class(self, class_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM students WHERE IDclass_f = ?", (class_id,))
        students_raw = cur.fetchall()
        students_usable = []
        return students_raw
    
    def select_assignments_topic(self, topic_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM assignment WHERE IDtopic_f = ?", (topic_id,))
        assignments_raw = cur.fetchall()
        assignments_usable = []
        return assignments_raw
    
    def select_assignments_individual(self, student):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM assignment a LEFT JOIN studentAssignment sa ON sa.IDassignment_f=a.IDassignment WHERE sa.IDstudent_f = ? ", (student,))
        assignments_raw = cur.fetchall()
        #print("ass raw: ", assignments_raw)
        return assignments_raw
            
        
        
        
    
#=============TESTING========================
#sqlh = SQLiteHandler('mathWorksheet.db')
#sqlh.select_assignments(sqlh.conn)
    