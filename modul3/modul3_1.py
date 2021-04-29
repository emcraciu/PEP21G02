# functions

# general function construction

def my_func1(arg1, arg2, arg3, kwarg1=' ', kwarg2='\n'):
    print(arg1, arg2, arg3, sep=kwarg1, end=kwarg2)
    return arg1 + arg2 + arg3


my_var1 = my_func1('srt1', 'str2', 'str3', kwarg1='$', kwarg2='$')
print('\n' + 80 * '#')
print(my_var1)

# bit operation

# 01010001 - initial
# 01110011 - key

# 01110011 - OR
# 01010001 - AND
# 00100010 - XOR
#################

# 00100010 - XOR result
# 01110011 - key

# 01010001 - initial value


# numbers in memory
+0  # 00000000000...000
+1  # 00000000000...001
+2  # 00000000000...010
-1  # 11111111111...111

# AND
print(10 & 11)
print((10).__and__(11))

10  # 00000000000...1010
11  # 00000000000...1011
# 00000000000000...1010

# OR
print(10 | 11)
print((10).__or__(11))

10  # 00000000000...1010
11  # 00000000000...1011
# 00000000000000...1011

# XOR
print(10 ^ 11)
print((10).__xor__(11))
10  # 00000000000...1010
11  # 00000000000...1011
# 00000000000000...0001


# XOR negative number
print(-1 ^ 3)
print((-1).__xor__(3))
10  # 11111111111...1111 -1
11  # 00000000000...0011
#    11111111111...1100
