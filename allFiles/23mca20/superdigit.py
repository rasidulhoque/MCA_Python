num=int(input("enter a number"))

def superDigit(num):
    sum=0
    rem=0
    if(num>=0 & num<=9):
        return num
    else:
        rem=num%10
        sum=rem+sum
        num=num/10
        if(sum>9):
            superDigit(sum)
        print(sum)
