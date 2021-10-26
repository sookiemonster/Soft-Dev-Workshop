# Daniel Sooknanan, Cameron Nelson, Sophie Liu
# SoftDev
# K16 - All About Database
# 2021-10-20

import sqlite3
from csv import DictReader

# Define file names & table names
DB_FILE = "discobandit.db"
COURSE_FILE = "courses.csv"
STUDENTS_FILE = "students.csv"

COURSE_TABLE = 'COURSES'
STUDENT_TABLE = 'STUDENTS'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def tableExists(table_name):
    """Returns a boolean representative of whether a table exists on """
    # Select all tables with table_name within the database file
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='%s' ''' % (table_name))
    return (c.fetchone()[0]==1)

def makeList(filename):
    """Returns a list given a .csv file, structured as [FIELD_1, FIELD_2, FIELD_3] for each row"""
    result = []

    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile, fieldnames = ['FIELD_1', 'FIELD_2', 'FIELD_3'])
            row_counter = 0

            for row in reader: 
                if row_counter != 0:
                    # Fill in the dictionary with Job Classes as keys & a list of Percentages & Links as values
                    result.append([row['FIELD_1'], int(row['FIELD_2']), int(row['FIELD_3'])])

                row_counter+=1

    except FileNotFoundError: 
        print("File %s does not exist" % (filename))
    
    return result

if not(tableExists(COURSE_TABLE)):
    course_list = makeList(COURSE_FILE)

    create_courses = """CREATE TABLE %s (
        ROWID INTEGER PRIMARY KEY NOT NULL,
        NAME              TEXT  NOT NULL,
        MARK              INT   NOT NULL,
        ID                INT   NOT NULL 
    );""" % (COURSE_TABLE)        # test SQL stmt in sqlite3 shell, save as string

    c.execute(create_courses)    # run SQL statement

    # Propogate course table upon creation
    c.executemany("""INSERT INTO %s (NAME,MARK,ID)
    VALUES (?,?,?); """ % (COURSE_TABLE), course_list)

    db.commit() #save changes

if not(tableExists(STUDENT_TABLE)):
    student_list = makeList(STUDENTS_FILE)

    create_students = """CREATE TABLE %s (
    NAME  TEXT NOT NULL,
    AGE INT NOT NULL,
    ID INTEGER PRIMARY KEY NOT NULL); 
    """ % (STUDENT_TABLE)

    c.execute(create_students)

    # Propogate students table upon creation 
    c.executemany("""INSERT INTO %s (NAME,AGE,ID)
    VALUES (?,?,?); """ % (STUDENT_TABLE), student_list)

db.commit() 
db.close()  #close database
