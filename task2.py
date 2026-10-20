def count_string_elements(values):
    """Count string elements in a list."""
    count = 0

    for value in values:
        if isinstance(value, str):
            count += 1

    return count


elements = [42, "hello", 3.14, True, "Python", None, [1, 2], "GitHub"]

string_count = count_string_elements(elements)

print(f"Number of string elements: {string_count}")
