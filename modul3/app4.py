# result : [
# ['Section1', value1, value2], ['Section2', value1, value2], ...
# ]

data = """
_____
Section1
_____

value1
value2

_____
Section2
_____

value1
value2

_____
Section3
_____

value1
value2

"""


def parse_data(data: str):
    section_flag = False
    lines = data.splitlines()
    result = []
    for line in lines:
        if line == "":
            continue
        if "_____" == line and section_flag is False:
            section_flag = True
            print("New section")
        elif "_____" == line and section_flag is True:
            section_flag = False
            print("End new section")
        elif section_flag:
            print("Section name is", line)
            result.append([line])
        elif not section_flag:
            result[-1].append(line)
    return result


var = parse_data(data)
print(var)


def parse_data(data: str):
    result = []
    my_iter = data.splitlines().__iter__()
    for line in my_iter:
        if line == '':
            continue
        if "_____" == line:
            result.append([next(my_iter)])
            next(my_iter)  # we just discard this line
            continue
        result[-1].append(line)
    return result


var = parse_data(data)
print(var)
