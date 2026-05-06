a = [1, 3, 5, 7, 8]
b=len(a)
def mod(a):
    s=0 #cоздаем переменную для суммы
    for i in range(0,b-1):
        d = abs(a[i] - a[i+1])
        s += d  
    return s
print(mod(a))