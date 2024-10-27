def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
nums = (10, 20, 30, 40, 50)
print(find_largest_number(nums))  # Output will be 50
