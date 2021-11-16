"""
Дан словарь слов с переводом их на разные языки. Например,
d = {'hello':['bonjour','ciao','shalom'], 'bye':['auf wiedersehen','cheerio','au revoir']}.
Пользователь вводит любое слова. На экран выводим всевозможные переводы для этого слова из словаря
"""
d = {'hello':['bonjour','ciao','shalom'],
'bye':['auf wiedersehen','cheeno','au revoir']}
word = input("Введите любое слово - ")
try:
    print(" ".join( d[word] ))
except:
    for key in d:
        if word in d[key]:
            print(key , end=" ")
            for item in d[key]:
                if item != word:
                    print(item, end=" ")
print("\n")
