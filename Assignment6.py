#to simulate simple calculator that performs basic tasks such as addition, subtraction,
#multiplication and division with special operations like computing x^y and x!

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

def exp(x,y):
    return x**y

def fact(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    return fac

n1=int(input("enter the first no. : "))
n2=int(input("enter the second no. : "))
print("Enter your choice : ")
print("1.Additon\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponential\n6.Factorial")
ch=int(input())
print()
if(ch==1):
    ans=add(n1,n2)
    print("Addition is : ",ans)
elif(ch==2):
    ans = sub(n1, n2)
    print("Subtraction is : ", ans)
elif(ch==3):
    ans = mult(n1, n2)
    print("Multiplication is : ", ans)
elif(ch==4):
    ans = div(n1, n2)
    print("Division is : ", ans)
elif(ch==5):
    ans = exp(n1, n2)
    print("Exponential is : ", ans)
elif(ch==6):
    ans = fact(n1)
    print("Factorial is : ", ans)
else:
    print("Invalid input")
