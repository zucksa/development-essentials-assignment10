
elements = [42, "hello", 3.14, True, "Python", None, [1, 2], "GitHub"]

string_count = 0

for element in elements:
    if isinstance(element, str):
        string_count += 1

print(f"Number of string elements: {string_count}")
