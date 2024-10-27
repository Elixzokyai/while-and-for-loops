# calculates the total of the list of nums

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
print(sum_of_numbers(numbers))  # Output will be 15

