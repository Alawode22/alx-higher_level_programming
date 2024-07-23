#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list.copy()
    # Check if index is valid
    if 0 <= idx < len(my_list):
        new_list[idx] = element  # Replace the element in the copied list 
    return new_list  # Return the modified or copied list
