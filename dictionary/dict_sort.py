import csv

math_dict = {}
with open("./score.csv") as file:
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        math_dict[row[1]] = row[-4]
    print(headers)

print(math_dict)
sorted_key = sorted(math_dict, key=lambda s: s)
sorted_value = sorted(math_dict, key=lambda s: math_dict[s])# will be value list
print()
print(sorted_key)

# Sort the dictionary by the values (converting values to integers for sorting if needed)
sorted_tup = sorted(math_dict.items(), key=lambda item: item[1])#tuple
sorted_dict = dict(sorted(math_dict.items(), key=lambda item: item[1]))#dictionary

print("\nSorted Dictionary:")
print(sorted_dict)
print(sorted_tup)

list_of_tup = []

for k,v in math_dict.items():
    list_of_tup.append((v,k))

print(sorted(list_of_tup))


