import random


def ip_generator(ip: str):
    my_list = [i for i in range(0, 256)]
    fin_list = []
    ip_part, subnet_part = ip.split(sep='/')
    ip_list = ip_part.split(".")
    # print(ip_list)
    if int(subnet_part) != 24:
        raise Exception
    for k in ip_list:
        if int(k) < 0 or int(k) > 255:
            raise Exception
    new_ip_part = ip_part.rsplit(sep='.', maxsplit=1)
    for _ in range(len(my_list)):
        x = random.randint(0, len(my_list) - 1)
        fin_list.append(new_ip_part[0] + "." + str(my_list.pop(x)))
    return fin_list


print(ip_generator('192.168.0.3/24'))
