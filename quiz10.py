def tuples_to_dict(tuples_list):
    result_dict = {}
    for string, number in tuples_list:
        result_dict[string] = number
    return result_dict

# Example usage
input_tuples = [("apple", 5), ("banana", 3), ("cherry", 7)]
output_dict = tuples_to_dict(input_tuples)
print(output_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}
