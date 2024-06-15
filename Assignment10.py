b_num=input("Enter a binary number : ")
r_num=b_num[::-1]
dec=0
for i in range(len(r_num)):
    dec=dec+int(r_num[i])*2**i
print(dec)