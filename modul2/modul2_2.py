# # chr
#
# print(chr(101))
# print(ord('e'))
#
# # if
# a = '1'
# if 1 == a:
#     print("1")
# elif 2 == a:
#     print('2')
# else:
#     print('3')
#     print('something else')
#
# print()
# from time import sleep
#
# for letter in 'my text':
#     print(letter, end='')
#     sleep(1)
#
# print(letter)

# True and True

# False or False

# XOR
a = 'a'
b = 'b'


# AND and OR operators for objects
print(a and b)

if a:
    print(b)
else:
    print(a)

a = False
b = True

print(a or b)

if a:
    print(a)
else:
    print(b)

a = 0
b = 1

if a > b or b > a:
    print('somethong')