multi_dimensional_list = [[1, [2, [3]]], [4, [5, [6]]], [7, [8, [9]]]]


# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# no recursion


def flatten_list(data: list):
    fin_list = []
    for i in data:
        if type(i) == int:
            fin_list.append(i)
            continue
        print(i)
        for j in i:
            if type(j) == int:
                fin_list.append(j)
                continue
            print(j)
            for m in j:
                if type(m) == int:
                    fin_list.append(m)
                    continue
                print(m)
                for n in m:
                    if type(n) == int:
                        fin_list.append(n)
                        continue
                    print(n)
    return fin_list


result = flatten_list(multi_dimensional_list)
print(result)
