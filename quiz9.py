def has_pair_with_sum(numbers, target_sum):
    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example usage
input_list = [10, 15, 3, 7]
target = 17
result = has_pair_with_sum(input_list, target)
print(result)  # Output will be True
