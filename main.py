def main():
    print("---Welcome to my calculator!---")
    print("-------------------------------")
    while True:
        numbers = get_input()
        a = int(numbers[0])
        b = int(numbers[1])
        while True:
            option = choose_op()
            if int(option) == 1:
                addition(a, b)
                break
            elif int(option) == 2:
                subtraction(a, b)
                break
            elif int(option) == 3:
                multiplication(a, b)
                break
            elif int(option) == 4:
                division(a, b)
                if ZeroDivisionError:
                    continue
                else:
                    break
        again = input("Do you want to count something else? ").lower()
        if again == "y" or again == "yes":
            True
        elif again == "n" or again == "no":
            print("---Thank you for using my calculator, BYE!---")
            break


    

def get_input():
    while True:
        a = input("Provide a: ")
        if not a.isdigit():
            print("You need to provide a number.")
        else:
            break
    while True:
        b = input("Provde b: ")
        if not b.isdigit():
            print("You need to provide a number.")
        else:
            break
    return a, b

def choose_op():
    print("Choose operation:")
    print("1 - addition\n2 - subtraction\n3 - multiplication\n4 - division")
    while True:
        operation = input()
        if not operation.isdigit():
            print("You need to provide a number.")
        elif int(operation) > 4:
                print("That is not an option.")
        else:
            break
    return operation

def addition(a, b):
    add = a + b
    print(f"{a} + {b} = {add}")

def subtraction(a, b):
    subtr = a - b
    print(f"{a} - {b} = {subtr}")

def multiplication(a, b):
    mult = a * b
    print(f"{a} * {b} = {mult}")

def division(a, b):
    try:
        div = a / b
        print(f"{a} / {b} = {div}")
    except ZeroDivisionError:
        print("You can't divide by zero.")
                
    
main()