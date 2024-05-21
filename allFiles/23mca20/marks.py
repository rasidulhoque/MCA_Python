marks= int(input("enter your marks"))
if(marks>=90):
    print("grade = O")
elif(marks >=80 & marks<=89):
    print("grade = A+")
elif(marks >=70 & marks<=79):
    print("grade = A")
elif(marks >=60 & marks<=69):
    print("grade = B")
elif(marks >=50 & marks<=59):
    print("grade = C")
elif(marks >=40 & marks<=49):
    print("grade = D")
else:
    print("grade = F")
