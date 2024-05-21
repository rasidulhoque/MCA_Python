while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
  
    choice = int(input("Enter choice (1-5): "))
  
    if choice == 5:
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1+num2
        print("Result:", result)
    elif choice == 2:
        result = num1-num2
        print("Result:", result)
    elif choice == 3:
        result = num1*num2
        print("Result:", result)
    elif choice == 4:
        result = num1/num2
        print("Result:", result)
    else:
        print("invalid choice:")
