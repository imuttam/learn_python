word = input("Enter any word: ")
reverse = ""
for w in word:
    reverse = w + reverse

print(f"The reverse of {word} is : {reverse}")
