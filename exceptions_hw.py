'''
Read the following code and change it so that it treats the possible exceptions 
that might arise.
'''

a = 12
s = "hello"

try:
	print("inside try")
	print(a + s) # will raise TypeError
	print("Printed using original data types")
except TypeError: # will handle only TypeError
	print("inside except")
	print(str(a) + s)
	print("Printed using type-casted data types")
except OverflowError:
    print("The given numbers are too large! try changing your inputs")
except MemoryError :
    print("The operation went out of memory ! Try try changing your inputs")
except SystemError:
    print("An error occurred within the system! Python interpreter version is : ",system.version)