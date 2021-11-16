def de_encrypt_text(text, shift = 3):
    new_str = ''
    for c in text:
        if c == ' ':
            new_str = new_str + c
        elif c.isupper():
            new_str = new_str + chr((ord(c) - shift - 65) % 26 + 65)
        else:
            new_str = new_str + chr((ord(c) - shift - 97) % 26 + 97)
    return new_str

print(de_encrypt_text(input("Введите сообщение которое нужно расшифровать - "),int(input("Введите ключ - "))))
