# Basic calculator program in python
# Basic functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
# Main
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.EXIT")
    # Give input
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4'):
        new=input("Does Input have Fractional Part(True/False) :")
        if new == "True":
            num1 = float(input("Enter First number: "))
            num2 = float(input("Enter Second number: "))
        elif new == "False":
            num1 = int(input("Enter First number: "))
            num2 = int(input("Enter Second number: "))
        else:
            print("Invalid Input Please enter only True/False");
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            if int(num2)==0:
                print("Divide by zero error enter proper input(non-zero)")
                continue
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print("---------Exiting----------")
        break
    else:
        print("Invalid Input")
        break
