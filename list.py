n = int(input("Введите число: "))
def spisok(n):
    try:
        if n < 1:
            raise ValueError("Число должно быть не меньше 1")
        res = [list(range(1, i + 1)) for i in range(1, n + 1)]
        return res

    except ValueError as e:
        print (e)
print(spisok(n))