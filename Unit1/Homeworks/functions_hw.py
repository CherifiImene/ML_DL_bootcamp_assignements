'''
    1\ Write a Python function that checks whether a passed string is palindrome or not. A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

    2\ Write a Python function that takes a number as a parameter and checks if the number is prime or not. A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

    3\ Write a Python function to check whether a number is in a given range.

    4\ Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

    5\ Write a Python program to reverse a string.

    6\ Write a Python function to sum all the numbers in a list.

    7\ Write a Python function to find the Max of three numbers.

'''

# 1\ Write a Python function that checks whether 
# a passed string is palindrome or not. 
# A palindrome is a word, phrase, or sequence that reads the same backward 
# as forward, e.g., madam or nurses run.

def isPalindrome(word):
    length = len(word)
    if (length %2 == 0):
        half1 = word[:length//2].lower()
        half2 = word[length//2:].lower()
        return  half1 == half2[::-1]
    else:
        half1 = word[:length//2].lower()
        half2 = word[length//2+1:].lower()
        return  half1 == half2[::-1]
#print(isPalindrome("kayak"))

# 2\ Write a Python function that takes a number as a parameter 
# and checks if the number is prime or not. 
# A prime number (or a prime) is a natural number 
# greater than 1 and that has no positive divisors other than 1 and itself.

def isPrime(n):
    if (n<1) :
        return False
    else:
        for i in range(2,n//2):
            if n%i == 0 :
                return False
        else:
            return True
#print(isPrime(3))

# 3\ Write a Python function to check whether 
# a number is in a given range.

def isInRange(n , b, a=0):
    return n in range(a,b)
#print(isInRange(5,20))

#4\ Write a Python function to calculate the factorial of a number 
# (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if(n<0):
        print ("The number must be a non-negative integer")
        return
    else:
        if(n == 0) | (n==1):
            return 1
        else:
            return n * factorial(n-1)
#print(factorial(5))

#5\ Write a Python program to reverse a string.
def reverseString(s):
    return s[::-1]

#6\ Write a Python function to sum all the numbers in a list.
def sumList(numbers):
    s = 0
    for n in numbers:
        s = s + n
    return s

#7\ Write a Python function to find the Max of three numbers.
def max_3(n1,n2,n3):
    maximum = n1
    difference = -1
    for n in (n2,n3):
        if maximum < n:
            maximum = n
    return maximum
#print(max_3(3,2,3))