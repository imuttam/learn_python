word = input("Enter any word or sentence: ")
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for w in word:
    if w in vowels:
        count +=1

print(f"There are {count} vowels in '{word}'")