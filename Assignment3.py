num_list=[]
N=int(input("Enter the count of Numbers:"))

for i in range(N):
    num=int(input("Enter the Numbers:"))
    num_list.append(num)
print(num_list)

max1=max(num_list)
print("Maximum number from list is:",max1)
min1=min(num_list)
print("Minimum number from list:",min1)
print("Sum of numbers from list is:",sum(num_list))

avg=sum(num_list)/len(num_list)       #len(num_list)=length of the list(No. of elements in the list)
print("Average of numbers from list is:",avg)


    