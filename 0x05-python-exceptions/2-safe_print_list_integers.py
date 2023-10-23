def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a count variable to keep track of printed integers

    for i in range(x):  # Iterate over the first x elements in the list
        try:
            print("{:d}".format(my_list[i]), end="")  # Print the integer without a newline
            count += 1  # Increment the count for each successfully printed integer
        except (ValueError, TypeError):
            continue  # Skip non-integer values

    print()  # Add a newline after all integers are printed
    return count  # Return the count of printed integers
