"""Given the file “student_names.txt” do the following:

    1\ Read all of the content of the file in one variable.
    2\ Write a list of random names to your file.
    3\ Read the first n lines of the file.
    4\ Read the last n lines of the file.
    5\ Check if the name x is in the file.
    6\ Write a Python program to generate 26 text files named A.txt, B.txt, 
    and so on up to Z.txt.
"""

import string
#1\ Read all of the content of the file in one variable.
students_file = open("./inputs/i_o_hw/student_names.txt")

students = students_file.read()
print(students)
students_file.close()
#2\ Write a list of random names to your file.

students = students + "\nJohnny Depp"+"\nJohn Fish"+"\nElodie Yung"+"\nRyan Reynolds"

students_file = open("./inputs/i_o_hw/student_names.txt","w")
students_file.write(students)
students_file.close()
#3\ Read the first n lines of the file.
file = open("./inputs/i_o_hw/student_names.txt")
names = file.readlines()
file.close()
n = 4

first_n_students = names[:n]
print("The first ",n," students are :",first_n_students)
#4\ Read the last n lines of the file.

last_n_students = names[-n:]
print("The last ",n," students are :",last_n_students)

#5\ Check if the name x is in the file.
x = "Emilia Clarck"
file = open("./inputs/i_o_hw/student_names.txt")
names = file.readlines()
file.close()
print ("The name ",x," is in the file ? ", x in names)

#6\ Write a Python program to generate 26 text files named A.txt, B.txt, 
#    and so on up to Z.txt.
abc_set = string.ascii_uppercase

for i in range(26):
    open("./outputs/i_o_hw/"+abc_set[i]+".txt","w")