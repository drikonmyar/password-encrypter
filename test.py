UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"

message="Hello, what's up??"

translated = ""
for character in message:
    if character.isupper():
        transCharIndex = (UPPER_LETTERS.find(character) + 14) % 26
        translated += UPPER_LETTERS[transCharIndex]
    elif character.islower():
        transCharIndex = (LOWER_LETTERS.find(character) + 18) % 26
        translated += LOWER_LETTERS[transCharIndex]
    else:
        translated += character

print(translated)
