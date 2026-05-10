a = "Адрес среда !сосна насос кот тоК) лодка177"
symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' 
def anagram(a):
    words = a.lower().split()
    filtr_words = []
    b = {}

    for word in words:
        clean_word = word.strip(" @,.)(&^%$#*_-/[]{}!?\"'0123456789«»—")
        if len(clean_word) > 0 and all(s in symbols for s in clean_word): 
            filtr_words.append(clean_word)

        for clean_word in filtr_words:
            l_count = {}

        for i in clean_word:
            if i in l_count:
                l_count[i] += 1
            else:
                l_count[i] = 1
        
        c = tuple(sorted(l_count.items()))
        if c in b:
            if clean_word not in b[c]:
                b[c].append(clean_word)
        else:
            b[c] = [clean_word]

    res = []
    for group in b.values():
        if len(group) > 1:
            res.append(group)
            
    return res
print(anagram(a))
