def facto(num):
    if num < 0:
        return "Ingrese numero mayor a 0"
    elif num == 0:
        return "paila"
    else:
        f = 1
        while num > 1:
            f*=num
            num-=1
            print (f)
        return f
facto(5)
