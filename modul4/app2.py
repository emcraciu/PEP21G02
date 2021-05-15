multi_dimensional_list = [[1, [2, [3]]], [4, [5, [6]]], [7, [8, [9]]]]


# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# no recursion

# attempt resolving using nested for loops - will not dynamically adjust to object depth
def flatten_list(data: list):
    fin_list = []
    for i in data:
        if type(i) == int:
            fin_list.append(i)
            continue
        print('level 1:', i)
        for j in i:
            if type(j) == int:
                fin_list.append(j)
                continue
            print('level 2:', j)
            for m in j:
                if type(m) == int:
                    fin_list.append(m)
                    continue
                print('level 3:', m)
                for n in m:
                    if type(n) == int:
                        fin_list.append(n)
                        continue
                    print('level 4:', n)
    return fin_list


result = flatten_list(multi_dimensional_list)
print(result)


# attempt resolving using recursive function calls - this will work for any (max ~255) object depth
def flatten_list(data: list):
    fin_list = []
    for i in data:
        if type(i) == int:
            fin_list.append(i)
            continue
        fin_list.extend(flatten_list(i))
    return fin_list


result = flatten_list(multi_dimensional_list)
print(result)
