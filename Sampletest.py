#1)Using For loop printing 1 to 10 natural numbers in python

# for i in range(1,11):
#     print(i)
#-----------------------------------------------------------------------------

#2)printing Even numbers from 1 to 20 in python

# for i in range(1,21):

#     if(i%2==0):
#         print(i)
#----------------------------------------------------------------------------

#3)Python program to sum of numbers from 1 to given number

# N = int(input("Enter the Ending number:"))

# sum = N*(N+1)//2

# print("The Sum of numbers from 1 to",N,"is",sum)

#-----------------------------------------------------------------------------

#4)Python program to Add all the odd numbers with in the given range

# Start = int(input("Enter the Starting Number:"))
# Ending = int(input("Enter the Ending Number:"))

# OddTotal = 0

# for i in range(Start,Ending+1):
#     if i%2!=0:
#         OddTotal=OddTotal+1
# print("The Sum of Odd numbers from",Start,"to",Ending ,"is",OddTotal)        

#------------------------------------------------------------------------------

#5)Python program to Multiplication tables of a given number
# Number =int (input("Enter the number for tables:"))
# Start = int(input("Enter the Start Range :"))
# End = int(input("Enter the Ending Range:"))

# for i in range(Start,End+1):

#     print(Number,"X",i,"=",Number*i)

#-------------------------------------------------------------------------------

#6)Python program to count the number of even and odd numbers from a series of numbers

# Start = int(input("Enter the Starting Number:"))
# Ending = int(input("Enter the Ending Number:"))

# Even=0
# Odd=0

# for i in range(Start,Ending+1):
#     if(i%2==0):
#      Even=Even+1

#     else:
#        Odd=Odd+1
# print("The NUmber of Even Number is:",Even)
# print("The NUmber of Odd Number is:",Odd)
#--------------------------------------------------------------------------------------------------------

#7) To check the Number or String is a Palindrome

# Value = (input("Enter the Value:"))

# Reverse = Value[::-1]

# if(Value==Reverse):
#     print("The Value Entered is Palindrome")
# else:
#     print("The Entered Value is Not a Palindrome")    

#---------------------------------------------------------------------------------------------------------

#8) To find a factorial of a number
# i=int(input("Enter the Number:"))
# fact=1

# while(i>0):
#     fact=fact*i
#     i=i-1
# print(fact)    
#----------------------------------------------------------------------------------------------------------
#9) Program to print the word in reverse
# word=input("Enter the Word:")

# reverse=""

# for i in word:
#     reverse=i+reverse
# print("The Reverse Word is:",reverse)    
#-----------------------------------------------------------------------------------------------------------------

#10)Write a Python program that iterates the integers from 1 to 25.

# for i in range(1,26):
#     print(i)
#------------------------------------------------------------------------------------------------------------------

#11) Python program to get the Fibonacci series between 0 to 50.

# A=0
# B=1
# print("The Fibonacci series between are 0 to 50 are:")

# while A<=50:

#     print(A,end=",")

#     A,B= B,A+B
#------------------------------------------------------------------------------------------------------------------------

#12 Python program to count the numbers in series of digit

# num = int(input("Enter a number: "))
# num = abs(num)
# count=0
# if num == 0:
#     count = count + 1
# else:
#     count = 0
#     while num > 0:
#         num = num//10
#         count =count + 1

# print("Total number of digits:", count)
#-------------------------------------------------------------------------------------------------------------------------------





