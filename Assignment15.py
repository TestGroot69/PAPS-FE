#def substr(s,sub):
#   index=s.find(sub)
#    if index!=1:
#        return True
#    return False

str1=str(input())
str2=str(input())

print("Enter Your Choice:")
print("1. Length of the string\n2. Reversal of the String\n3. Check Equality Of the 2 Strings\n4. Check Palindrome\n5. Check Substring\n")
ch=int(input())
print()

if(ch==1):
    print("Length of str1: ",len(str1))
    print("Length of str2: ",len(str2))
elif(ch==2):
    print("Reversal of str1: ",str1[::-1])
    print("Reversal of str2: ",str2[::-1])
elif(ch==3):
    if (str1 == str2):
        print("Strings are Equal")
    else:
        print("Strings are not not Equal")
elif(ch==4):
    ch1=int(input())
    if(ch1==1):      #for checking Str1
        if(str1==str1[::-1]):
            print("Str1 is Palindrome")
        else:
            print("Str1  is not Palindrome")
    elif(ch==2):     #for checking str2
        if(str2==str2[::-1]):
            print("Str2 is Palindrome")
        else:
            print("Str2 is not Palindrome")
elif(ch==5):
    #if (substr(str1,str2)==True):
    #    print("Str2 is substring of Str1")
    #else:
    #    print("Str2 is not substring of str2")

    #if (substr(str2,str1)==True):
    #    print("Str1 is substring of Str1")
    #else:
    #    print("Str1 is not substring of str2")
    if(str1 in str2):
        print("str1 is substring of str2")
    else:
        print("str1 is not substring of str2")

    if(str2 in str1):
        print("str2 is substring of str1")
    else:
        print("str2 is not substring of str1")
