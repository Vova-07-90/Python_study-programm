# программа по шифрованию и дешифрованию паролей

#1 - шифрование

def cipher_rus(txt, k):
    cript_str =''
    for c in txt:
        if 1072 <= ord(c) <= 1103:
            cript = ord(c) + k
            if cript > 1103:
                cript -= 32
            cript_str += chr(cript)
        elif 1040 <= ord(c) <= 1071:
            cript = ord(c) + k
            if cript > 1071:
                cript -= 32
            cript_str += chr(cript)
        else:
            cript_str += c 
    return cript_str

txt = 'привет вова'
k = 3
print(cipher_rus(txt, k))


def cipher_en(txt, k):
    cript_str =''
    for c in txt:
        if 65 <= ord(c) <= 90:
            cript = ord(c) + k
            if cript > 90:
                cript -= 26
            cript_str += chr(cript)
        elif 97 <= ord(c) <= 122:
            cript = ord(c) + k
            if cript > 122:
                cript -= 26
            cript_str += chr(cript)
        else:
            cript_str += c 
    return cript_str

txt = 'To be, or not to be, that is the question!'
k = 17
print(cipher_en(txt, k))


#2 - дешифрование

def decipher_rus(txt, k):
    decript_str =''
    for c in txt:
        if 1072 <= ord(c) <= 1103:
            decript = ord(c) - k
            if decript < 1072:
                decript += 32
            decript_str += chr(decript)
        elif 1040 <= ord(c) <= 1071:
            decript = ord(c) - k
            if decript <1040:
                decript += 32
            decript_str += chr(decript)
        else:
            decript_str += c 
    return decript_str

txt = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
k = 7
print(decipher_rus(txt, k))


def decipher_en(txt, k):
    decript_str =''
    for c in txt:
        if 65 <= ord(c) <= 90:
            decript = ord(c) - k
            if decript < 65:
                decript += 26
            decript_str += chr(decript)
        elif 97 <= ord(c) <= 122:
            decript = ord(c) - k
            if decript < 97:
                decript += 26
            decript_str += chr(decript)
        else:
            decript_str += c 
    return decript_str

txt = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
k = 25
print(decipher_en(txt, k))



