"""
Напишите шифр простой замены, который генерирует для букв английского алфавита 26
неповторяющихся чисел в виде слова и шифрует слово, сопоставляя каждой букве число из словаря.
"""
Alif = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
Aa = []

f = 8
while len(Aa) != len(Alif):
    f += 3
    Aa.append(f)
    print(Aa)

#dict = {Alif[i] : Aa[i] for i in range(len(Alif))}
dict = {}
for i in range(len(Alif)):
    dict[Alif[i]] = Aa[i]

print("Cписок: \n\n", dict, "\n")
word = input("Введите слово - ").upper()

print("\n\nЗашифрованное слово - ", end='')
for key in word:
    print(dict.get(key, ""), end=' ')
    #dict.get(key[, default]) - возвращает значение ключа, но если его нет,
    #не бросает исключение, а возвращает default (по умолчанию None).

print("\n\n")
