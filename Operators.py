# 1 operator :
#  Relational Operatorrs :
#  it is sed to find Relation Between two variables/ values :
# it returns True or False


a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("a>b",a>b)
print("a<b",a<b)
print("a==b",a==b)
print("a!=b",a!=b)
print("a>=b",a>=b)
print("a<=b",a<=b)
print("a is greater than b :",a>b)
print("a is less than b :",a<b)
print("a is equal to b :",a==b)
print("a is not equal to b :",a!=b)
print("a is greater than or equal to b :",a>=b)
print("a is less than or equal to b :",a<=b)


# 2 logical Operators :
# and, or, not:

a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("a>b and a<b :",a>b and a<b)
print("a>b or a<b :",a>b or a<b)
print("not(a>b) :",not(a>b))
print("not(a<b) :",not(a<b))
print("not(a==b) :",not(a==b))
print("not(a!=b) :",not(a!=b))
print("not(a>=b) :",not(a>=b))
print("not(a<=b) :",not(a<=b))
print("not(a is greater than b) :",not(a>b))
print("not(a is less than b) :",not(a<b))


# 3 Bitwise Operators :
# it is used to perform bitwise operation on binary numbers :

a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("a & b :",a & b)
print("a | b :",a | b)
print("a ^ b :",a ^ b)
print("~a :",~a)
print("~b :",~b)
print("a << 2 :",a << 2)
print("b << 2 :",b << 2)
print("a >> 2 :",a >> 2)
print("b >> 2 :",b >> 2)



# 4 Assignment Operators :
# it is used to assign value to a variable :

a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("a =",a)
print("b =",b)
a+=b
print("a += b :",a)
a-=b
print("a -= b :",a)
a*=b
print("a *= b :",a)
a/=b
print("a /= b :",a)
a%=b
print("a %= b :",a)
a//=b
print("a //= b :",a)


# 5 Membership Operators :
# it is used to test if a sequence is presented in an object :
# in, not in


a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("a in [1, 2, 3] :",a in [1, 2, 3])
print("b in [1, 2, 3] :",b in [1, 2, 3])
print("a not in [1, 2, 3] :",a not in [1, 2, 3])
print("b not in [1, 2, 3] :",b not in [1, 2, 3])


# 6 Identity Operators :
# it is used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is, is not

a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("a is b :",a is b)
print("a is not b :",a is not b)
print("a is a :",a is a)
print("b is b :",b is b)


# 7 Arithmetic Operators :
# it is used to perform mathematical operations on numbers :

a=int(input("enter the number :"))
b=int(input("enter the number :"))
print("a + b =",a + b)
print("a - b =",a - b)
print("a * b =",a * b)
print("a / b =",a / b)
print("a % b =",a % b)
print("a // b =",a // b)
print("a ** b =",a ** b)

# 8 Ternary Operator :
# it is used to assign a value to a variable based on a condition :

a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))
print("a if a>b else b =",a if a>b else b)
print("a if a>c else c =",a if a>c else c)
print("b if b>a else a =",b if b>a else a)
print("b if b>c else c =",b if b>c else c)
print("c if c>a else a =",c if c>a else a)
print("c if c>b else b =",c if c>b else b)