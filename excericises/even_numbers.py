def even():
    l = list(range(100))
    list_aux = []
    lenght = len(l)
    for i in range (lenght):
        if i %2 == 0:
            list_aux.append(i)
    return (list_aux)
print(even())