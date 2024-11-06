import csv

math_dict = {}
with open("./score.csv") as file:
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        math_dict[row[1]] = row[-4]  # Assuming row[1] is the key and row[-4] is the value
    print("Headers:", headers)

# Print the initial math_dict
print("\nOriginal Dictionary:")
print(math_dict)

# Sort the dictionary by values by swapping key and value in each tuple
sorted_swapped = sorted(math_dict.items(), key=lambda item: (item[1], item[0]))

print(sorted_swapped)

# Swap back to original (key, value) format and convert to a dictionary
sorted_dict = {k: v for k, v in sorted_swapped}

print("\nSorted Dictionary by Values (Ascending):")
print(sorted_dict)
