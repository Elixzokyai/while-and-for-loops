def print_even_value_keys(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(key)

# Example usage
input_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(input_dict)
