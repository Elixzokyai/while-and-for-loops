def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = remove_duplicates(input_list)
print(output_list)  # Output will be [1, 2, 3, 4, 5]
