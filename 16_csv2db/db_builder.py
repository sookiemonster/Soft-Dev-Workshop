# Daniel Sooknanan, Cameron Nelson, Sophie Liu
# SoftDev
# K16 - All About Database
# 2021-10-20

import sqlite3
from csv import DictReader

DB_FILE = "discobandit.db"
COURSE_FILE = "courses.csv"
STUDENTS_FILE = "students.csv"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def makeList(filename):
    """Returns a list given a .csv file, structured as [KEY, Field_1, Field_2] for each row"""
    result = []

    try:
        with open(filename) as csvfile:
            reader = DictReader(csvfile, fieldnames = ['KEY', 'FIELD_1', 'FIELD_2'])
            row_counter = 0

            for row in reader: 
                if row_counter != 0:
                    # Fill in the dictionary with Job Classes as keys & a list of Percentages & Links as values
                    result.append([row['KEY'], int(row['FIELD_1']), int(row['FIELD_2'])])

                row_counter+=1

    except FileNotFoundError: 
        print("File %s does not exist" % (filename))
    
    return result

course_list = makeList(COURSE_FILE)

create_courses = """CREATE TABLE COURSES (
    ROWID INTEGER PRIMARY KEY NOT NULL,
    NAME              TEXT  NOT NULL,
    MARK              INT   NOT NULL,
    ID                INT   NOT NULL 
);
"""          # test SQL stmt in sqlite3 shell, save as string

c.execute(create_courses)    # run SQL statement

c.executemany("""INSERT INTO COURSES (NAME,MARK,ID)
# VALUES (?,?,?); """, course_list);

db.commit() #save changes

student_list = makeList(STUDENTS_FILE)

create_students = """CREATE TABLE STUDENTS (
NAME  TEXT NOT NULL,
AGE INT NOT NULL,
ID INTEGER PRIMARY KEY NOT NULL); 
""";

c.execute(create_students)

c.executemany("""INSERT INTO STUDENTS (NAME,AGE,ID)
VALUES (?,?,?); """, student_list);

db.commit() 
db.close()  #close database
