# программа по угадыванию загаданного числа программой
import random
num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(n):
    return n.isdigit() and 0 <= int(n) <= 101

flag = False
while flag == False:
    print("Введите число от 1 до 100:")
    n = input()
    if is_valid(n) == True:
        n = int(n)
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif n == num:
            print('Вы угадали, поздравляем!')
            flag == True
            break

    if is_valid(n) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
