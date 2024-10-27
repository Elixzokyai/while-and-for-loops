def keys_greater_than_n(d, n):
    result = []
    for key, value in d.items():
        if value > n:
            result.append(key)
    return result

# Example usage
input_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
output_list = keys_greater_than_n(input_dict, n)
print(output_list)  # Output will be ['a', 'b']
