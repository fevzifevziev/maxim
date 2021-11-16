"""
Реализовать шифр Полибия (буквы случайно вписываются в матрицу)
"""
import random
A = [ ["А", "Б","В","Г","Д","Е","Ё","Ж","З","И","r"],
[ "Й","К","Л","М","Н","О","П","Р","С","Т","s"],
[ "У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","t"],
[ "Э","Ю","Я"," ","а","б","в","г","д","е","u"],
[ "ё","ж","з","и","й","к","л","м","н","о","v"],
[ "п","р","с","т","у","ф","х","ц","ч","ш","w"],
[ "щ","ъ","ы","ь","э","ю","я","0","1","2","x"],
[ "3","4","5","6","7","8","9","A","B","C","y"],
[ "D","E","F","G","H","I","J","K","L","M","z"],
[ "N","O","P","Q","R","S","T","U","V","W","."],
[ "X","Y","Z","a","b","c","d","e","f","g",","],
[ "h","i","j","k","l","m","n","o","p","q","-"]]
KORTE = ()
L = 0
K = 0
spisok = []
KK = {}
KK2 = {}

for i in range(len(A)):                 #вывод первоночального списка
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print("")
print("\n")

str1=input("Введите слово - ")
spisok = list(str1)
length = len(spisok)
print("\n")

for i in range(len(A)):
    for j in range(len(A[i])):
        for g in range(length):
            if spisok[g] == A[i][j]:
                KK[g] = i,j
    print(end = "")
print(KK)
random.shuffle(A)

for sublist in A:
    random.shuffle(sublist)

for i in range(len(A)):                  #вывод измененного списка
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print("")

list_keys = list(KK.keys())
list_keys.sort()
for i in list_keys:
    KK2[i] = KK[i]
print(KK2)
print("\n-------------------------------")
print("ЗАШИФРОВАННОЕ СЛОВО - ",end="")
for g in range(length):
    for i in range(len(A)):
        for j in range(len(A[i])):
            KORTE = KK2.get(g)
            (L,K) = KORTE
            if L == i and K == j:
                print(A[i][j],end="")
print("\n-------------------------------")
