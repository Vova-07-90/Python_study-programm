import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

count = int(input('Введите количество паролей для генерации:'))
length_pas = int(input('Введите длину одного пароля:'))
digits_pas = input('Включать ли цифры?: да\нет')
upper_pas = input('Включать ли прописные буквы?: да\нет')
lower_pas = input('Включать ли строчные буквы?: да\нет')
punct_pas = input('Включать ли символы (!#$%&*+-=?@^_)?: да\нет')
del_punct_pas = input('Включать ли неоднозначные символы (il1Lo0O)?: да\нет')

if digits_pas.lower() == 'да':
    chars += digits
if upper_pas.lower() == 'да':
    chars += uppercase_letters
if lower_pas.lower() == 'да':
    chars += lowercase_letters
if punct_pas.lower() == 'да':
    chars += punctuation
if del_punct_pas.lower() == 'да':
    for c in 'il1Lo0O':
        chars.replace(c,'')

def generate_password(length, chars):
    password = ''
    for i in range(count):
        for i in range(length):
            password += random.choice(chars)
        print(password)
        password = ''
generate_password(length_pas, chars)