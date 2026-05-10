a = "Адрес среда !сосна насос кот тоК) лодка177"
symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' 

def clean(word):
    res = []
    word = word.lower()
    for i in word:
        if i in symbols:
            res.append(i)
    return "".join(res) 

def anagram(text):
    words = text.split()
    b = {} 
    
    for word in words:
        clean_word = clean(word)
        if len(clean_word) > 0:
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