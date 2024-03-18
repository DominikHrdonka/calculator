def main():
    print("Welcome to my calculator!")
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
    operation = input()
    return operation



main()