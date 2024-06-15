def fibo(n):
    a=1
    b=0
    fs=[]
    for i in range(n):
        t=b
        b=b+a
        a=t
        fs.append(b)
    print("Fibo Series is : ", fs)

n=int(input("Enter the number of terms : "))
fibo(n)