def concatenate_list_elements(lst):
    concatenated_string = ""
    for elem in lst:
        concatenated_string += str(elem)
    return concatenated_string

print(concatenate_list_elements([1, 5, 12, 2]))  