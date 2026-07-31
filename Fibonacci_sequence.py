def print_fibonacci_terms(n):
    a, b = 0, 1
    terms = []
    for _ in range(n):
        terms.append(a)
        a, b = b, a + b
    print("Fibonacci sequence:", " ".join(str(t) for t in terms))


def is_fibonacci_number(num):
    a, b = 0, 1
    if num < 0:
        return False
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


if __name__ == "__main__":
    n = int(input("How many terms? "))
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_fibonacci_terms(n)

    num = int(input("Enter a number to check: "))
    if is_fibonacci_number(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")
