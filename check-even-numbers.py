while True:
    print("Options:")
    print("Enter 'even' if you want to check that digit is even")
    print("Enter 'quit' if you want to quit")
    user_input = input(":")

    if user_input == "quit":
     break

    elif user_input == "even":
        num = float(input("Enter a number:"))
        if num % 2 == 0:
            print("Liczba parzysta")
        elif num % 2 != 0:
            print("liczba nie parzysta")
    else:
        print("Unknown input")
