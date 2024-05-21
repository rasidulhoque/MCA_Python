def superDigit(num):
    if num >= 0 and num <= 9:
        return num
    else:
        sum = 0
        while num > 0:
            digit = num % 10
            sum += digit
            num //= 10
        return superDigit(sum)

num = int(input("Enter a number: "))
result = superDigit(num)
print("Super Digit:", result)
