# FizzBuzz print numbers from 1 to 100. 
# for multiples of :
#3 ,print "Fizz"
#5 ,print "buzz"
# both 3 and 5 print "FizzBuzz"
# otherwise ,,print the number itself.


for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        

# Table 
a=int(input("Enter the number"))
for i in range(1,a+1):
    print("----num---")
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
print()




