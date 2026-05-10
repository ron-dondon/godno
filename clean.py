a=input('введите текст:')
symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ' 
def clean(a):
    res= []
    a= a.lower()
    for i in a:
        if i in symbols:
            res.append(i)

    return "".join(res) #склеиваем буквы в строку

print(clean(a))