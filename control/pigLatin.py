word = input('Enter a word\n')

word_new = word[-1] + word[:-1]

vowel = 'aeiou'

for c in vowel:
    if c is word[-1]:
        piglatin = word_new+ 'ay'
    else:
        piglatin = word + 'yay'

print(piglatin)

