import random
def sum_list(l = []):
    lenght = len(l)
    sum = 0
    for i in range(lenght):
        sum+=l[i]
    return sum

n = 10
l = []
for i in range (n):
    l.append(random.randint(0,10))
print (f"la lista es {l}")

print(sum_list(l))