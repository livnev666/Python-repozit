

n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

maximum = 0
i_max = 0
j_max = 0

for i in range(n):
    for j in range(m):
        if a[i][j] > maximum:
            maximum = a[i][j]
            i_max = i
            j_max = j
print(maximum)
print(i_max, j_max)


#Та же задача, только в конце надо посчитать сумму по диагонали
stroka, stolbec = map(int, input().split())
a = []
for i in range(stroka):
    row = list(map(int, input().split()))
    a.append(row)
for i in a:
    print(i)
lst = [a[i][j] for j in range(stroka) for i in range(stroka) if i == j]
avg = sum(lst) // len(lst)
print(f'Диагональ: {lst}')
print('Среднее значение:', avg)


lst = list(range(0, 30 + 1))
a = ['аист']
x = 1
while x < 2:
    people = input('Привет! Как тебя зовут? ')
    print('Окей', people + '!', 'Давай сыграем в игру, где тебе нужно будет решить примеры. \n'
    '\rИ если ты решишь правильно ВСЕ задачки, то увидим, что для тебя сделают смайлики ))')
    x += 1
    #################################################################
    print('Пример N1:')
    user = int(input('2 + 3 = '))
    while lst[2] + lst[3] != user:
        print(people, 'это не верный ответ ))! Подумай еще пожалуйста')
        user = int(input('Введи ответ заново... ))\n\rИ так: 2 + 3 = '))
    print('Мммм.... )) а ты молодец! Так держать!\n \rИ вот тебе первый смайлик )))'
        ' Продолжаем решать примерчики и увидим,\n \rчто у нас получится из смайликов ))')
    count = 1
    while count < 2:
        print('\U0001f600')
        count += 1
    print('#' * 100)
    ###############################################################
    print('Пример N2:')
    user = int(input('5 + 5 = '))
    while lst[5] + lst[5] != user:
        print('Ну', people, 'это не правильно )) Давай думай еще ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 5 + 5 = '))
    print('Ух ты....!!! )) хорошо получется!', people, ', Так держать!\n \rИ вот тебе уже второй смайлик )))'
            '\n \rПродолжаем решать примерчики и увидим,\n \rчто у нас получится из смайликов ))')
    count = 1
    while count < 3:
        print('\U0001f600')
        count += 1
    print('#' * 100)
    ####################################################################
    print('Пример N3:')
    user = int(input('8 + 7 = '))
    while lst[8] + lst[7] != user:
        print('Нееет', people, 'это не правильно )) Давай думай еще ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 8 + 7 = '))
    print('Ай молодец какая....!!! )) хорошо получется!', people, ', КЛАСС!\n \rА вот уже и третий смайлик подоспел )))'
            '\n \rПродолжаем решать примерчики и увидим,\n \rчто у нас получится из смайликов ))')
    count = 1
    while count < 3:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)
    #####################################################################
    print('Пример N4:')
    user = int(input('9 + 5 = '))
    while lst[9] + lst[5] != user:
        print('Ну ты чего, ну не правильно же', people, ')) Давай думай еще ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 9 + 5 = '))
    print('Вот это я понимаю! ....!!! )) Ответ ВЕРНО!', people, ', ВАУ!\n \rПолучай четвертый, пятый и даже ШЕСТОЙ СМАЙЛ )))'
            '\n \rИ так, продолжаем решать примеры и будем ждать,\n \rчто у нас получится из смайликов в итоге))')
    count = 1
    while count < 4:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)
    ########################################################################
    print('Пример N5:')
    user = int(input('10 + 12 = '))
    while lst[10] + lst[12] != user:
        print('Да, знаю', people, 'это сложный пример )) Но давай ты подумаешь еще ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 10 + 12 = '))
    print('ДА, ДА, ДА! ....!!! )) И ты правильно его решила!', people, ', ВАУ!\n \rПолучай плюс еще 4 смайлика )))'
            '\n \rИ так, продолжаем решать примеры и будем ждать,\n \rчто у нас получится из смайликов в итоге))')
    count = 1
    while count < 5:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)
    #########################################################################
    print('Пример N6:')
    user = int(input('12 - 8 = '))
    while lst[12] - lst[8] != user:
        print(people, 'ну это же не сложный пример )) Давай соберись и подумай еще ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 12 - 8 = '))
    print('Ну вот видишь...)) Ты правильно его решила!', people, ', ты молодец!\n \rПолучай заслуженные смайлики )))'
            '\n \rИ так, продолжаем решать примеры и будем ждать,\n \rчто у нас получится из смайликов в итоге))')
    count = 1
    while count < 6:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)
    ################################################################################
    print('Пример N7:')
    user = int(input('14 + 15 = '))
    while lst[14] + lst[15] != user:
        print(people, 'это сложный пример )) Но давай ты подумаешь еще ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 14 + 15 = '))
    print('ДА, ДА, ДА! ....!!! )) И ты правильно его решила!', people, ', ВАУ!'
          '\n \rЕще пачка смайлов прилетела к тебе )))'
            '\n \rИ так, продолжаем решать примеры и будем ждать,\n \rчто у нас получится из смайликов в итоге))')
    count = 1
    while count < 7:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)
    #################################################################################
    print('Пример N8:')
    user = int(input('20 - 7 = '))
    while lst[20] - lst[7] != user:
        print('Эхххх', people, people, 'это сложный пример )) Но надо его решить ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 20 - 7 = '))
    print('Крутяк!!! )) Ты его решила!, ВАУ!\n \rСюда смайлы, КАМОН )))'
            '\n \rИ так, продолжаем решать примеры и будем ждать,\n \rчто у нас получится из смайликов в итоге))')
    count = 1
    while count < 8:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)
    ##################################################################################
    print('Пример N9:')
    user = int(input('13 - 8 = '))
    while lst[13] - lst[8] != user:
        print('Нет', people, 'не правильно )) Думай', people, 'думай ))')
        user = int(input('Введи ответ заново... ))\n\rИ так: 13 - 8 = '))
    print('Ну наконец то! ....!!! )) Ты правильно его решила!!\n \rОтгружаем еще смайлов )))'
            '\n \rИ так, продолжаем решать примеры и будем ждать,\n \rчто у нас получится из смайликов в итоге))')
    count = 1
    while count < 9:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)
    ################################################################################
    print('Пример N10:')
    user = input('Высокий, длинноногий, \n\rЛетать ему не лень - \n\rНа крыше из соломы Устроился... ')
    while user not in a:
        print('Нет', people, 'это не правильно )). Ну какой же это', user, '))')
        user = input('Введи заново ответ на эту загадку. )) \n\r'
                     'Высокий, длинноногий, \n\rЛетать ему не лень - \n\rНа крыше из соломы Устроился... ')
    print('Ну наконец то! ....!!! )) Ты правильно отгадала! Это', *a, ')))')
    print('Ты прошла ВСЕ уровни!!!', people, 'Ты МОЛОДЕЦ! Лови елочку )))')
    count = 1
    while count < 10:
        print('\U0001f600' * count)
        count += 1
    count = 1
    while count < 10:
        print('\U0001f600' * count)
        count += 1
    count = 1
    while count < 10:
        print('\U0001f600' * count)
        count += 1
    print('#' * 100)






































