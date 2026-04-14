def memorize(func): #создаём декоратор
    a={}  #создаём словарь
    def wrapper(n):#внутренняя функция
        if n not in a:
            a[n] = func(n)#вызываем оригинальную функции если нет результата и помещаем в словарь
        return a[n]#возвращаем значение из словаря
    return wrapper

@memorize #вызов декоратора
def fib(n): #создаем функцию
    if n <= 1: #цикл
        return n #возвращаем n
    b= 0 #создаем переменную
    for i in range(n):
        b = b + fib(i) #cкладываем их все
    return b

i = int(input("Введите порядковый номер: "))
print(f"{i} = {fib(i)}")