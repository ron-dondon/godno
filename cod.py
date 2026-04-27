from collections import Counter

with open('ivan-turgenev-mumu.txt', 'r', encoding='utf-8') as f: #открываем файл
    text = f.read() #читаем файл

symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #допускаемые символы

words = text.lower().split() #делаем все буквы строчными и разбиваем на отдельные слова
filtr_words = []#создаём список
for word in words:# Очищаем от пробелов и ненужных знаков
    clean_word = word.strip(" @,.)(&^%$#*_-/[]{}!?\"'0123456789«»—") 
    if len(clean_word) > 0 and all(s in symbols for s in clean_word): #делаем проверку (слово непустое и состоит из допустимых символов)
        filtr_words.append(clean_word) #добавляем в список

word_counts = Counter(filtr_words) #считаем частоту
total_words = len(filtr_words) #считает общее количество слов в очищенном списке

for word, count in word_counts.most_common(): #цикл
    p= (count / total_words) * 100 #чтобы получить процент,делим количество повторов конкретного слова на общее количество слов в тексте и умножаем на 100
    print(word, count, f"{p:.3f}%") #выводим, но в процентах оставляем только 3 знака после запятой
