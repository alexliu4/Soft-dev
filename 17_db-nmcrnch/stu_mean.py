# trackStars -- Alex Liu, William Lu
# SoftDev1 pd7
# K16 -- No Trouble
# 2018-10-05 F

import sqlite3

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

avg_list = []
id_list = []

#looks for each course based on id
for x in range(1,11):
    grades = "SELECT courses.mark FROM courses WHERE " + str(x) + "= courses.id;"
    c.execute(grades)

    #gets all the courses for the durrent "x" id
    mark_list = c.fetchall()

    #finds name of student with specfic id
    students = "SELECT peeps.name FROM peeps WHERE " + str(x) + "= peeps.id;"
    c.execute(students)

    student = c.fetchall()

    ids = "SELECT peeps.id FROM peeps WHERE " + str(x) + "= peeps.id;"
    c.execute(ids)

    id = c.fetchall()

    #makes a list of avgs for each student
    markTuples = ()
    for row in mark_list:
        markTuples += row
        #print (row)

    #adds the tuples in the list for each student
    sum = 0
    num_cor = 0
    for num in markTuples:
        sum += num
        num_cor += 1
        #print (sum)
    #prints sum of grades
    print (str(student[0][0]) + " with id " + str(id[0][0]) + " total : " + str(sum) )

    #prints avg
    print (str(student[0][0]) + " with id " + str(id[0][0]) + " avg : " + str(sum / num_cor ) + "\n" )
    avg_list.append(sum / num_cor)
    id_list.append(id[0][0])

# ==============================Creating New Table==============================

command = "CREATE TABLE peeps_avg ( ID INTEGER, AVERAGE FLOAT )"
c.execute(command)

for x in range(0,10):
    command = "INSERT INTO peeps_avg VALUES " + "(" +  str(id_list[x]) + ", " + str(avg_list[x]) + ");"
    #print(command)
    c.execute(command)


db.commit() #save changes

db.close()  #close database
