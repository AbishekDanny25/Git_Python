#Nested Loop

# for i in range(1,3):
#     print("Week:",i)
#     for j in range(1,4):
#         print("Day:",j)
#---------------------------------------------------------
#Star pattern

# for i in range(1,5):
#     print() 
#     for j in range(1,i+1):
#         print("*",end="")
#-------------------------------------------------------------------------------------------
#Using while loop Printing 1 to 5 Numbers

# i=1

# while(i<=5):
#     print(i)
#     i=i+1    
#----------------------------------------------------------------------------------------------------
#Using loop to print the series (10,20,30,40,50..............200)

# i=10

# while(i<=200):
#     print(i)
#     i=i+10
#-------------------------------------------------------------------------------------------------------
#program to print first 10 natural numbers in reverse order

# i=10

# while(i>=1):
#     print(i,end=",")
#     i=i-1
#---------------------------------------------------------------------------------------------------------

# To find a factorial of a number
# i=int(input("Enter the Number:"))
# fact=1

# while(i>0):
#     fact=fact*i
#     i=i-1
# print(fact)    
#----------------------------------------------------------------------------------------------------------

#Functions to add, sub , Mult , Div

# A=int(input("Enter the Number:"))
# B=int(input("Enter the Number:"))

# Operations=int(input("Choose the Operation to do:1,2,3,4:"))

# if(Operations==1):
#     def add():
#         print(A+B)
#     add()
# elif(Operations==2):
#     def sub():
#         print(A-B)
#     sub()
# elif(Operations==3):
#     def mult():
#         print(A*B)    
#     mult()    
# elif(Operations==4):
#     def div():
#         print(A//B)
#     div()  
#-------------------------------------------------------------------------------------------------------------------

#Getting a input from user and passing it to function to check the number is even or odd

# def evenorodd(b):
#     if(b%2==0):
#         print("The Number",b,"is Even")
#     else:
#         print("The number",b,"is Odd")

# a= int(input("Enter the Number:"))
# evenorodd(a)
#------------------------------------------------------------------------------------------------------------------------

#Getting a input from user and passing it to function to check the number is even or odd

# a= int(input("Enter the Number:"))

# def evenorodd(a):
#     if(a%2==0):
#         print("The Number is Even")
#     else:
#         print("The Number is Odd")    

# evenorodd(a)       
#-----------------------------------------------------------------------------------------------------------------------------