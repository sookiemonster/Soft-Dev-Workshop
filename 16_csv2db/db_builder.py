# Cameron Nelson
# SoftDev
# K16 - All About Database
# 2021-10-20

import sqlite3,csv

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

command = """CREATE TABLE COURSES (
    ROWID INTEGER PRIMARY KEY NOT NULL,
    NAME              TEXT  NOT NULL,
    MARK              INT   NOT NULL,
    ID                INT   NOT NULL 
);
"""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

courses = open('courses.csv')
reader = csv.reader(courses)
array = [];
for i in reader:
    array.append(i);
    
array.pop(0); # Remove first line "code,mark,id" 
c.executemany("""INSERT INTO COURSES (NAME,MARK,ID)
VALUES (?,?,?); """,array);

db.commit() #save changes

c.execute("""CREATE TABLE STUDENTS (
NAME  TEXT NOT NULL,
AGE INT NOT NULL,
ID INTEGER PRIMARY KEY NOT NULL); 
""");

students = open('students.csv')
reader = csv.reader(students)
array = [];
for i in reader:
    array.append(i);
    
array.pop(0); # Remove first line "code,mark,id" 
c.executemany("""INSERT INTO STUDENTS (NAME,AGE,ID)
VALUES (?,?,?); """,array);

db.commit() 
db.close()  #close database
