#  String and Lists Homework
# Homework

#  1  Create a list that contains all the even numbers between 1 and 299.
even_list = []
for nb in range(1,300,1):
    if (nb % 2 == 0):
        even_list.append(nb)

#  2  Iterate through the previously created list and print first the length 
# of the list then all the squared values of the list.
print("The length of the list is : ",len(even_list))

for nb in even_list:
    print("Squared element is : ", nb**2)

#    In one line check if 57 is in the list using one line of python
print("57 is in the list ? ", 57 in even_list)