#      Statement

# it is a unit of code that the Python interpreter can execute. A statement does not return a value,
# but it may have side effects, such as modifying a variable or printing output to the console.  

# 1 Conditional Statements :
# it is used to perform different actions based on different conditions :
# if, elif, else

a=int(input("enter the number :"))
b=int(input("enter the number :"))
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")
    
    

# voting eligibility program using conditional statements :
age=int(input("enter your age :"))
if age>=18:
    print("you are eligible to vote")



# even or odd program using conditional statements :
num=int(input("enter the number :"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")
    

# using conditional statements to check if a number is positive, negative or zero :
num=int(input("enter the number :"))
if num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")
    
    


# 2 Looping Statements :
# it is used to execute a block of code repeatedly until a certain condition is met :
# for, while 

# for loop :

name=input("enter your name :")
for i in name:
    print(i)
    

#run table using for loop :
num=int(input("enter the number :"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)



# for multiple table using for loop :
num=int(input("enter the number :"))
for j in range(1,21):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
    print("\n")
    num+=1
    

# factorial of a number using for loop :
num=int(input("enter the number :"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("the factorial of",num,"is",factorial)



# addition of n numbers using for loop :
n=int(input("enter the number of terms :"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("the sum of first",n,"numbers is",sum)



# addition of odd n  numbers using while loop :
num=int(input("enter the number of terms :"))
sum=0
for i in range(1,num+1,2):
    sum=sum+i
print("the sum of first",num,"odd numbers is",sum)


# addition of even n  numbers using while loop :
num=int(input("enter the number of terms :"))
sum=0
for i in range(2,num+1,2):
    sum=sum+i
print("the sum of first",num,"even numbers is",sum)



# prime series using while loop :
num=int(input("enter the number of terms :"))
for i in range(2,num+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        
        

# prime number using while loop :`
start =int(input("enter the starting number :"))
end =int(input("enter the ending number :"))
for i in range(start, end ):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        
#swapping of two numbers using while loop :
a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("before swapping a =",a)
print("before swapping b =",b)


# swapping of two numbers using third variable :
temp=a
a=b
b=temp
print("after swapping a =",a)

# reversing a string  using while loop :
name=input("enter your name :")
reversed_name=""
i=len(name)-1
while i>=0:
    reversed_name+=name[i]
    i-=1
print("reversed name :",reversed_name)


# revers string using vowels using while loop :

a=input("Enter the string")
vowels="aeiouAEIOU"
count =0
for i in a:
    if i in vowels:
        count+= 1
        print("number of vowels :",count)
        
        
#  reverse text 

text =str(input("enter the name"))
b=""
for i in text:
    b=i+b
    print(b)
    
    
# star pattern 

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
        