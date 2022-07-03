UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"

message="Hello, what's upazAZ??"

translated = ""
for character in message:
    if character.isupper():
        transCharIndex = (UPPER_LETTERS.find(character) - 99) % 26
        translated += UPPER_LETTERS[transCharIndex]
    elif character.islower():
        transCharIndex = (LOWER_LETTERS.find(character) - 99) % 26
        translated += LOWER_LETTERS[transCharIndex]
    else:
        translated += character

print(translated)
