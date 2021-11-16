
class Caesar:

    def __init__(self, initial, encrypted = ''):
        self.initial = initial
        self.encrypted = encrypted

    #Шифратор
    def encrypt_text(self, shift):
        new_str = ''
        for c in self.initial:
            if c == ' ':
                new_str = new_str + c
            elif c.isupper():
                new_str = new_str + chr((ord(c) + shift - 65) % 26 + 65)
            else:
                new_str = new_str + chr((ord(c) + shift - 97) % 26 + 97)
        self.encrypted = new_str

    #Де шифратор
    def de_encrypt_text(self, shift):
        new_str = ''
        for c in self.initial:
            if c == ' ':
                new_str = new_str + c
            elif c.isupper():
                new_str = new_str + chr((ord(c) - shift - 65) % 26 + 65)
            else:
                new_str = new_str + chr((ord(c) - shift - 97) % 26 + 97)
        self.encrypted = new_str

    #VZLOM
    def vzlom(self):
        dict_V = {}
        for shift in range(26):
            new_str = ''
            for c in self.initial:
                if c == ' ':
                    new_str = new_str + c
                elif c.isupper():
                    new_str = new_str + chr((ord(c) - shift - 65) % 26 + 65)
                else:
                    new_str = new_str + chr((ord(c) - shift - 97) % 26 + 97)
            dict_V[(shift)] = new_str
        self.encrypted = dict_V

    def get_encrypted(self):
        return self.encrypted

    def breaking_text(self, n):
        c = []
        for i in range(n):
            new_str1 = ''
            new_str2 = ''
            new_str1 += self.get_encrypted()[i]
            new_str2 += self.initial[i]
            c.append(new_str1 - new_str2)
        return c
        self.breaking_text = new_str1 - new_str2

    def get_breaking(self):
        return self.breaking
str1 = "Fevzi"
o1 = Caesar(str1)
print("after encryption: ", o1.get_encrypted())
print("_"*90)
o1.vzlom()

o1.breaking_text(len(str1))
vshift = o1.get_breaking()
print("Смещение = " + str(o1.get_breaking()))
o1.decrypted_text(vshift)
print ("Расшифрованная строка: ", o1.get_decrypted())
