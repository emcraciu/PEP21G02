"""
Get text from input: abcdefg
return : acegikm

"""

# increment for position
text = input("Get input text: ")
letter1 = chr(ord(text[0]) + 0)
letter2 = chr(ord(text[1]) + 1)
letter3 = chr(ord(text[2]) + 2)
letter4 = chr(ord(text[3]) + 3)
letter5 = chr(ord(text[4]) + 4)
letter6 = chr(ord(text[5]) + 5)
letter7 = chr(ord(text[6]) + 6)
result = f'{letter1}{letter2}{letter3}{letter4}{letter5}{letter6}{letter7}'
print('Increment by position:', result)

# increment for letter
text = input("input=")
letter1 = chr(ord(text[0]) + (ord(text[0]) - ord('a')))
letter2 = chr(ord(text[1]) + (ord(text[1]) - ord('a')))
letter3 = chr(ord(text[2]) + (ord(text[2]) - ord('a')))
letter4 = chr(ord(text[3]) + (ord(text[3]) - ord('a')))
letter5 = chr(ord(text[4]) + (ord(text[4]) - ord('a')))
letter6 = chr(ord(text[5]) + (ord(text[5]) - ord('a')))
letter7 = chr(ord(text[6]) + (ord(text[6]) - ord('a')))
result = f'{letter1}{letter2}{letter3}{letter4}{letter5}{letter6}{letter7}'
print('Increment by difference to letter "a":', result)

# if x[0] == "a" or :
#     z1 = x[0]
# elif x[0] == "b":
#     z1 = chr(ord(x[0]) + 1)
# elif x[0] == "c":
#     z1 = chr(ord(x[0]) + 2)
# elif x[0] == "d":
#     z1 = chr(ord(x[0]) + 3)
# elif x[0] == "e":
#     z1 = chr(ord(x[0]) + 4)
# elif x[0] == "f":
#     z1 = chr(ord(x[0]) + 5)
# elif x[0] == "g":
#     z1 = chr(ord(x[0]) + 6)
#
# if (x[1] == "a"):
#     z2 = x[0]
# elif (x[1] == "b"):
#     z2 = chr(ord(x[1]) + 1)
# elif (x[1] == "c"):
#     z2 = chr(ord(x[1]) + 2)
# elif (x[1] == "d"):
#     z2 = chr(ord(x[1]) + 3)
# elif (x[1] == "e"):
#     z2 = chr(ord(x[1]) + 4)
# elif (x[1] == "f"):
#     z2 = chr(ord(x[1]) + 5)
# elif (x[1] == "g"):
#     z2 = chr(ord(x[1]) + 6)
