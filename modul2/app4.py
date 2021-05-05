"""
Take text from input: any text
change each letter based on previous letter

I will revert the change
"""

# Code to encrypt
text = input("Write a text: ")
result = ''
previous = ''
for letter in text:
    if previous == '':
        result += letter
    else:
        result += chr(ord(letter) + ord(previous))
    previous = letter
print(result)

# Code to decrypt
previous = result[0]
reverted = previous
for letter in result[1:]:
    previous = chr(ord(letter) - ord(previous))
    reverted += previous
print(reverted)
