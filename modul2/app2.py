"""
Get text from input: abcdefg
return : bcdefgh

"""
text = input("Get input: ")
l1 = chr(ord(text[1]) + 1)
l2 = chr(ord(text[2]) + 1)
l3 = chr(ord(text[3]) + 1)
l4 = chr(ord(text[4]) + 1)
l5 = chr(ord(text[5]) + 1)
l6 = chr(ord(text[6]) + 1)
l7 = chr(ord(text[7]) + 1)
print(l1, l2, l3, l4, l5, l6, l7, sep='')
