ef print_table(num):
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num}  x  {i:<2} =  {num * i}")


def print_tables_up_to(n):
    for num in range(1, n + 1):
        print_table(num)
        print("-" * 29)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_table(num)

    n = int(input("Enter N (tables from 1 to N): "))
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to(n)
