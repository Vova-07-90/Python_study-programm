# мини-программа по предсказаниям. Задаешь вопрос и получаешь рандомный ответ.
import random
answers = ['bessporno', 'predresheno', 'nikakix somneniy', 'bessporno DA',
           'mojesh bit uveren v etom', 'mne kazhetsa DA', 'veroyatnee vsego',
           'horoshie perspectivu', 'znaki govoriyat DA', 'DA', 'poka ne yasno', 
           'poprobyi snova', 'sprosi poszhe', 'luche ne rasskazivat', 
           'seychas nelza predskazat', 'skoncentriryisya i sprosi opat', 
           'dazhe ne dumay', 'moi otvet NET', 'po moim dannim NET',
           'perspektivy ne ochen xoroshii', 'vesma somnitelno']
print('Привет, я магический шар, я знаю ответы на твои вопросы:)')
name = input('Как тебя зовут? (введите Ваше имя) ')
print(f'Привет {name}')

flag = True
while flag == True:
    questions = input('Спроси у меня все что угодно: (введите Ваш вопрос) ')
    print(random.choice(answers))
    questions_2 = input('Хочешь задать еще вопрос?: (введите да или нет) ')
    if questions_2 == 'да':
        flag == True
        continue
    else:
        print('Возвращайся еще:)')
        flag == False
        break
    

