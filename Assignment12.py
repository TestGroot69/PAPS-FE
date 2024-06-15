
n=int(input("Enter the count of numbers: "))

numlist=[]
even=[]
odd=[]

for i in range(n):
    num=int(input("Enter the numbers: "))
    numlist.append(num)
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)

print("List of numbers: ", numlist)
print("List of even numbers: ", even)
print("List of odd numbers: ", odd)

numlist.extend([10,20,30])
print(numlist)



