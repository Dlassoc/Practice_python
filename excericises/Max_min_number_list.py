import random
def max_min(l):
    max_num = (max(l))
    min_num = (min(l))
    print (f"El numero mayor de la lista es {max_num}, y el menor es {min_num}")


n = 5
l = []
for i in range (n):
    l.append(random.randint(0,10))
print (f"la lista es {l}")
max_min(l)


