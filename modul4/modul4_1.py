# dict

empty_dict = {}

my_dict = {1: 'one', 'two': 2, 3: [], 4: {}}
print(my_dict)

# hash

print('one'.__hash__())
# print([1,2,3].__hash__())

# get value
print(my_dict[1])
#print(my_dict[2])
print(my_dict.get(1))
print(my_dict.get(2, 'Not a value'))



nr = 754343223
print(id(nr))
nr = nr + 1
print(id(nr))

nr = [7, 5, 4, 3]
print(id(nr))
nr.append(1)
print(id(nr))

# dict methods

print(my_dict.keys())
print(type(my_dict.keys()))
for key in my_dict.keys():
    print(key)

print(80 * '#')

for value in my_dict.values():
    print(value)

print(80 * '#')

for item in my_dict.items():
    print(item)

print(80 * '#')

for key, value in my_dict.items():
    print('key:', key, 'value:', value)
