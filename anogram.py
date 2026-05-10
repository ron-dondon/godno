a = "Адрес среда !сосна насос кот тоК) лодка177"
symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' 
def anagram(a):
    words = a.lower().split() #всю строку к нижнему регистру
    filtr_words = [] #список без знаков препинания
    b = {} #создаём словарь
    res = [] #будет наш итоговый список

    for word in words:
        clean_word = word.strip(" @,.)(&^%$#*_-/[]{}!?\"'0123456789«»—")
        if len(clean_word) > 0 and all(s in symbols for s in clean_word): 
            filtr_words.append(clean_word)

        for clean_word in filtr_words: #берем уже очищенные слова по одному
            l_count = {} #создаем словарь для конкретного слова, чтобы посчитать, сколько в нем каких букв

            for i in clean_word: #идем по каждой букве в слове
                if i in l_count:
                    l_count[i] += 1  #если буква есть в словаре, то увеличиваем
                else:
                    l_count[i] = 1
        
        c = tuple(sorted(l_count.items())) #превращаем список в кортеж,расставляем по алфавиту,словарь делаем кортежем
        if c in b: #проверяем,есть ли группа с таким набором букв
            if clean_word not in b[c]: #докидываем слово в этот список
                b[c].append(clean_word)
        else: #делаем новую запись
            b[c] = [clean_word]

    for group in b.values(): #проходим по всем спискам слов из словаря
        if len(group) > 1:
            res.append(group)
            
    return res
print(anagram(a))
