import random
def random_list():
    n = 10
    rand_list = []
    for i in range (n):
        rand_list.append(random.randint(0,25))
    return rand_list
print(random_list())


