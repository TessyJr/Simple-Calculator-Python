def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operation = 0;

while operation != '1' and operation != '2' and operation != '3' and operation != '4':
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    operation = input("Enter operation (1/2/3/4): ")
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == '4':
    print(num1, "/", num2, "=", divide(num1, num2))