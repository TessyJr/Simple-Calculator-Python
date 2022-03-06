def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def repeat():
    again = input("Do another calculation? (y/n): ")
    if again == 'y':
        selectOperation();
    elif again == 'n':
        print("Thank you for using my calculator")
    else:
        repeat();

def calculate(num1, num2, operation):
    if operation == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif operation == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif operation == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
    elif operation == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    repeat();
    

def inputNumber(operation):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    calculate(num1, num2, operation);

def selectOperation():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    operation = input("Enter operation (1/2/3/4): ")

    if operation != '1' and operation != '2' and operation != '3' and operation != '4':
        selectOperation();
    else:
        inputNumber(operation);
    

selectOperation();





    


