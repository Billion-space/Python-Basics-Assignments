def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def print_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


if __name__ == "__main__":
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in operations:
            symbol, func = operations[choice]
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))
            if choice in ("4", "5") and b == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = func(a, b)
                print(f"Result: {a:g} {symbol} {b:g} = {result:g}")
        else:
            print("Error: Please enter a number between 1 and 7.")
        print()
