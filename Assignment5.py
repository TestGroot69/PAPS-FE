def cube(n):
    return n**3

def check(num):
    s_num=str(num)
    sum=0
    for d in s_num:             #d is for digit
        sum=sum+cube(int(d))

    if(sum==num):
        return True

    return False

print(check())