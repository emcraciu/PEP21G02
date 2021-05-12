# how does for work:

my_data = [1, 2, 3, 4]

gen = my_data.__iter__()
print(type(gen))
gen2 = gen.__iter__()
print(id(gen2), id(gen))

entity1 = next(gen)
print(entity1)
entity2 = next(gen)
print(entity2)
entity3 = next(gen)
print(entity3)
# entity4 = next(gen)
# print(entity4)

my_iter = my_data.__iter__()
for i in my_iter:
    print(i)
    next(my_iter)

# generator using for

my_list = list(range(1, 100))
print(my_list)

my_list = []
for i in range(1, 100):
    my_list.append(i)
print(my_list)

my_list = [i for i in range(1, 100)]
print(my_list)

my_gen = (i for i in range(1, 100))
print(my_gen)
print(type(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

# tuple
my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))

# ex:
a = 10
b = 20

a, b = b, a
print('a=', a, 'b=', b)
print(type((a, b)))

# mutable
a = [1, 2, 3]
b = (1, 2, 3)

print(id(a))
a.append(4)
print(id(a))

print(id(b))
b = b + (1,)
print(b)
print(id(b))

c = 1,
print(type(c))


# generaator cu pas de 3 folosit in for pentru a obtine (0,9,18)

# list process

my_list = [1,2,3,4,5,6,7]
for i in my_list.copy():
    print(i)
    my_list.pop(0)