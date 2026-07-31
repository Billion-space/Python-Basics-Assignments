def get_numbers(n):
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)


def calculate_max(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest


def calculate_min(numbers):
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest


if __name__ == "__main__":
    n = int(input("How many numbers? "))
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        numbers = get_numbers(n)
        print("\nResults:")
        print(f"Sum:     {calculate_sum(numbers)}")
        print(f"Average: {calculate_average(numbers)}")
        print(f"Maximum: {calculate_max(numbers)}")
        print(f"Minimum: {calculate_min(numbers)}")
