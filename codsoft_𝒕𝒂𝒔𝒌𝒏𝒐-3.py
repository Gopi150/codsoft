def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zeroS"
    return x / y
def calsi():
    print("Simple Calculator")
    while(True):
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter operation choice (1/2/3/4/5): ")
        def inputs():
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1,num2
        result = None
        if choice == '1':
            num1,num2= inputs()
            result = add(num1, num2)
        elif choice == '2':
            num1,num2= inputs()
            result = subtract(num1, num2)
        elif choice == '3':
            num1,num2= inputs()
            result = multiply(num1, num2)
        elif choice == '4':
            num1,num2= inputs()
            result = divide(num1, num2)
        elif choice == '5':
            print("Loop Ended \nThank You!!")
            break
        
        else:
            print("Invalid operation choice,Please Enter a valid option")
        
        print("Result:", result)
        print("\n")
calsi()
