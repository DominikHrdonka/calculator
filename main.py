def main():
    print("---Welcome to my calculator!---")
    print("-------------------------------")
    get_input()
    choose_op()
    

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



main()