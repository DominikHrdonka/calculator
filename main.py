def main():
    print("---Welcome to my calculator!---")
    print("-------------------------------")
    numbers = get_input()
    a = int(numbers[0])
    b = int(numbers[1])
    option = choose_op()
    if int(option) == 1:
        addition(a, b)
    elif int(option) == 2:
        subtraction(a, b)
    

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
    
main()