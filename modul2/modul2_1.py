name = 'Jhon'
age = 26

print('name: ', name, ', age: ', age)

# print = 'print'
#
# print('name: ', name, ', age: ', age)

# type function

result = type(name)
print(result)

result = type(age)
print(result)

result = id(name)
print(result)

print(8 + 8)
print((8).__add__(8))

print(8 * ' text')
print(' text' * 8)

print(80 * '#')

print((8).__mul__(' text'))
print((' text').__mul__(8))

print(8 - 8)
print((8).__sub__(8))

print(8 / 8)
print((8).__truediv__(8))

print(8**8)
print((8).__pow__(8))
print(pow(8, 8))

# Float
nr = 1.1.__pow__(2)


# Complex

nr1 = 1.0 + 1.0J
nr2 = 3j
print(nr1+nr2)
print(type(nr))



# Strings
my_str1 = 'My String \n no multi line'
print(my_str1)
my_str1 = '''
this
is
a 
multi 
string 
test
'''
print(my_str1)
my_str2 = r"My String \n no multi line"
print(my_str2)

my_str2 = f"""My String {my_str1}"""
print(my_str2)


# dir
info = dir(my_str2)
print(info)

var1 = 'this is my text'
cap = var1.capitalize()
print(cap)
format1 = var1.format('Sparta')
print(format1)

phone = "0747.655.444"
split1 = phone.split("7")
print(split1)

# input
#name = input('Give me your name: ')



# slice
text = "My Text"
first_letter = "My Text"[0]
print(first_letter)
slice1 = text[4:1]
print(slice1)
slice2 = text[0:7:3]
print(slice2)

# negative step
reverse = text[::-1]
print(reverse)


# True, False

my_bool = True
print(type(my_bool))
my_bool = False
print(type(my_bool))

print(id(True))
print(id(False))
print(id(10))

# None
my_none = None
x = print('')
print(x)

# Truth

# 0 -> False
# 'a' > True
# '' > False
# None -> False

print(bool(0+0j))
print(bool(0.0))


