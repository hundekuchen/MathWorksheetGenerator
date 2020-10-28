


import sqlite3
from sqlite3 import Error


def create_connection(db_file):
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


def select_assignment(conn):
    """
    Query assignments
    """
    cur = conn.cursor()
    cur.execute("SELECT assignmentPyString FROM assignment")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"C:\Programmieren\MathWorksheetGenerator\mathWorksheet.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_assignment(conn)


if __name__ == '__main__':
    main()