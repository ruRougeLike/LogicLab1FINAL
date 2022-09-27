class tasks():
    
    def task1():
        mas1 = [3, 5, 8, 9, 25, 13, 46, 65]
        print("Задание 1. Написать программу, вычисляющую разницу между максимальным и минимальным элементами массива: " + str(mas1))
        max_number = max(mas1)
        min_number = min(mas1)
        a = int(max_number)-int(min_number)
        print("Разница между максимальным и минимальными элементами массива: " +str(a))

    def task2():
        import random
        mas2 = list(range(15))
        random.shuffle(mas2)
        print("Массив со случайными числами: " +str(mas2[:10]))

    def task3():
        raw = input('Введите последовательность чисел через пробел: ')
        int_array = [int(i) for i in raw.split(' ') if i.isdigit()]
        print(int_array)

    def task4():
        mat1 = [[10, 13, 44],  [11, 2, 3],  [5, 3, 1]] 
        mat2 = [[7, 16, -6], [9, 20, -4],  [-1, 3 , 27]] 
        mat3  = [[0,0,0], [0,0,0], [0,0,0]] 
        matrix_length = len(mat1) 
 
        for i in range(len(mat1)): 
            for k in range(len(mat2)): 
                mat3[i][k] = mat1[i][k] + mat2[i][k] 
 
        print('Сумма матриц: ', mat3)

    def tasklist():
        name1 = ['Джин', 'Джубилли', 'Лора', 'Роуг', 'Китти']
        name2 = ['Грей', 'Ли', 'Кинни', 'Рэйвен', 'Прайд']
        fac1 = ['Слизерин', 'Гриффиндор', 'Когтевран', 'Хаффлпаф']
        numbook = ['S3256', 'G1488', 'K1377', 'H58RUS', 'KITKAT']
        print('============================================================================')
        print('Студент: ' + name1[0] + ' ' + name2[0] + ' ' + fac1[0] + '' + numbook[0])
        print('Студент: ' + name1[1] + ' ' + name2[1] + ' ' + fac1[1] + '' + numbook[1])
        print('Студент: ' + name1[2] + ' ' + name2[2] + ' ' + fac1[2] + '' + numbook[2])
        print('Студент: ' + name1[3] + ' ' + name2[3] + ' ' + fac1[3] + '' + numbook[3])
        print('Студент: ' + name1[-1] + ' ' + name2[-1] + ' ' + fac1[-1] + '' + numbook[-1])
        print('============================================================================')

    def task5():
        name1 = ['Джин', 'Джубилли', 'Лора', 'Роуг', 'Китти']
        name2 = ['Грей', 'Ли', 'Кинни', 'Рэйвен', 'Прайд']
        fac1 = ['Слизерин', 'Гриффиндор', 'Когтевран', 'Хаффлпаф']
        numbook = ['S3256', 'G1488', 'K1377', 'H58RUS', 'KITKAT']
        score = ['S', 'A', 'S+', 'B', 'B']
        homeadress = ['3253 Perkins Lane W, Seattle, WA 98199', '80 S Jackson Street UNIT 408, Seattle, WA 98104', '5046 40th Avenue SW, Seattle, WA 98136', '12726 12th Avenue NE, Seattle, WA 98125', '7523 12th Avenue NW, Seattle, WA 98117']
        mutation = ['Телепатия', 'Вампиризм', 'Регенерация', 'Смертельное касание', 'Нематериальность']
        parents = ['сирота', 'сирота', 'Росомаха', 'Судьба', 'Шторм']
        realitionship = ['свободна', 'в отношениях']
        asks = ['Факультет', 'Оценки', 'Номер зачетной книжки', 'Домашний адрес', 'Мутация', 'Опекун', 'Отношения']
        print ('Введите запрос: ')
        while True:
            search1 = input('Имя: ')
            search2 = input('Введите конкретный запрос. Факультет, номер зачетной книжки, оценки, домашний адрес: ')
            if search1 == name1[0] and search2 == asks[0] or search1 == name2[0] and search2 == asks[0] or search1 == 'Алая Ведьма' and search2 == asks[0]:
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + ' обучается на факультете ' + fac1[0]
            elif search1 == name1[0] and search2 == asks[1] or search1 == name2[0] and search2 == asks[1] or search1 == 'Алая Ведьма' and search2 == asks[1]:
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + ' имеет рейтинг ' + score[0]
            elif search1 == name1[0] and search2 == asks[2] or search1 == name2[0] and search2 == asks[2] or search1 == 'Алая Ведьма' and search2 == asks[2]:
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + ' имеет номер зачетной книжки ' + numbook[0]
            elif search1 == name1[0] and search2 == asks[3] or search1 == name2[0] and search2 == asks[3] or search1 == 'Алая Ведьма' and search2 == asks[3]:
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + ' имеет домашний адрес: ' + homeadress[0]
            elif search1 == name1[0] and search2 == asks[4] or search1 == name2[0] and search2 == asks[4] or search1 == 'Алая Ведьма' and search2 ==asks[4]:
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + ' имеет мутацию: ' + mutation[0]
            elif search1 == name1[0] and search2 == asks[5] or search1 == name2[0] and search2 == asks[5] or search1 == 'Алая Ведьма' and search2 == asks[5]:
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + ' имеет опекуна: ' + parents[0]
            elif search1 == name1[0] and search2 == asks[-1] or search1 == name2[0] and search2 == asks[-1] or search1 == 'Алая Ведьма' and search2 == asks[-1]:
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + '. Статус: ' + realitionship[0]
            elif search1 == name1[1] and search2 == asks[0] or search1 == name2[1] and search2 == asks[0]:
                searchresult = 'Информация по вашему запросу: ' + name1[1] + ' ' + name2[1] + ' обучается на факультете ' + fac1[1]
            elif search1 == name1[1] and search2 == asks[1] or search1 == name2[1] and search2 == asks[1]:
                searchresult = 'Информация по вашему запросу: ' + name1[1] + ' ' + name2[1] + ' имеет рейтинг ' + score[1]
            elif search1 == name1[1] and search2 == asks[2] or search1 == name2[1] and search2 == asks[2]:
                searchresult = 'Информация по вашему запросу: ' + name1[1] + ' ' + name2[1] + ' имеет номер зачетной книжки ' + numbook[1]
            elif search1 == name1[1] and search2 == asks[3] or search1 == name2[1] and search2 == asks[3]:
                searchresult = 'Информация по вашему запросу: ' + name1[1] + ' ' + name2[1] + ' имеет домашний адрес: ' + homeadress[1]
            elif search1 == name1[1] and search2 == asks[4] or search1 == name2[1] and search2 == asks[4]:
                searchresult = 'Информация по вашему запросу: ' + name1[1] + ' ' + name2[1] + ' имеет мутацию: ' + mutation[1]
            elif search1 == name1[1] and search2 == asks[5] or search1 == name2[1] and search2 == asks[5]:
                searchresult = 'Информация по вашему запросу: ' + name1[1] + ' ' + name2[1] + ' имеет опекуна: ' + parents[1]
            elif search1 == name1[1] and search2 == asks[-1] or search1 == name2[1] and search2 == asks[-1]:
                searchresult = 'Информация по вашему запросу: ' + name1[1] + ' ' + name2[1] + '. Статус: ' + realitionship[1]
            elif search1 == name1[2] and search2 == asks[0] or search1 == name2[2] and search2 == asks[0]:
                searchresult = 'Информация по вашему запросу: ' + name1[2] + ' ' + name2[2] + ' обучается на факультете ' + fac1[2]
            elif search1 == name1[2] and search2 == asks[1] or search1 == name2[2] and search2 == asks[1]:
                searchresult = 'Информация по вашему запросу: ' + name1[2] + ' ' + name2[2] + ' имеет рейтинг ' + score[2]
            elif search1 == name1[2] and search2 == asks[2] or search1 == name2[2] and search2 == asks[2]:
                searchresult = 'Информация по вашему запросу: ' + name1[2] + ' ' + name2[2] + ' имеет номер зачетной книжки ' + numbook[2]
            elif search1 == name1[2] and search2 == asks[3] or search1 == name2[2] and search2 == asks[3]:
                searchresult = 'Информация по вашему запросу: ' + name1[2] + ' ' + name2[2] + ' имеет домашний адрес: ' + homeadress[2]
            elif search1 == name1[2] and search2 == asks[4] or search1 == name2[2] and search2 == asks[4]:
                searchresult = 'Информация по вашему запросу: ' + name1[2] + ' ' + name2[2] + ' имеет мутацию: ' + mutation[2]
            elif search1 == name1[2] and search2 == asks[5] or search1 == name2[2] and search2 == asks[5]:
                searchresult = 'Информация по вашему запросу: ' + name1[2] + ' ' + name2[2] + ' имеет опекуна: ' + parents[2]
            elif search1 == name1[2] and search2 == asks[-1] or search1 == name2[2] and search2 == asks[-1]:
                searchresult = 'Информация по вашему запросу: ' + name1[2] + ' ' + name2[2] + '. Статус: ' + realitionship[0]
            elif search1 == name1[3] and search2 == asks[0] or search1 == name2[3] and search2 == asks[0]:
                searchresult = 'Информация по вашему запросу: ' + name1[3] + ' ' + name2[3] + ' обучается на факультете ' + fac1[3]
            elif search1 == name1[3] and search2 == asks[1] or search1 == name2[3] and search2 == asks[1]:
                searchresult = 'Информация по вашему запросу: ' + name1[3] + ' ' + name2[3] + ' имеет рейтинг ' + score[3]
            elif search1 == name1[3] and search2 == asks[2] or search1 == name2[3] and search2 == asks[2]:
                searchresult = 'Информация по вашему запросу: ' + name1[3] + ' ' + name2[3] + ' имеет номер зачетной книжки ' + numbook[3]
            elif search1 == name1[3] and search2 == asks[3] or search1 == name2[3] and search2 == asks[3]:
                searchresult = 'Информация по вашему запросу: ' + name1[3] + ' ' + name2[3] + ' имеет домашний адрес: ' + homeadress[3]
            elif search1 == name1[3] and search2 == asks[4] or search1 == name2[3] and search2 == asks[4]:
                searchresult = 'Информация по вашему запросу: ' + name1[3] + ' ' + name2[3] + ' имеет мутацию: ' + mutation[3]
            elif search1 == name1[3] and search2 == asks[5] or search1 == name2[3] and search2 == asks[5]:
                searchresult = 'Информация по вашему запросу: ' + name1[3] + ' ' + name2[3] + ' имеет опекуна: ' + parents[3]
            elif search1 == name1[3] and search2 == asks[-1] or search1 == name2[3] and search2 == asks[-1]:
                searchresult = 'Информация по вашему запросу: ' + name1[3] + ' ' + name2[3] + '. Статус: ' + realitionship[0]
            elif search1 == name1[-1] and search2 == asks[0] or search1 == name2[-1] and search2 == asks[0]:
                searchresult = 'Информация по вашему запросу: ' + name1[-1] + ' ' + name2[-1] + ' обучается на факультете ' + fac1[-1]
            elif search1 == name1[-1] and search2 == asks[1] or search1 == name2[-1] and search2 == asks[1]:
                searchresult = 'Информация по вашему запросу: ' + name1[-1] + ' ' + name2[-1] + ' имеет рейтинг ' + score[-1]
            elif search1 == name1[-1] and search2 == asks[2] or search1 == name2[-1] and search2 == asks[2]:
                searchresult = 'Информация по вашему запросу: ' + name1[-1] + ' ' + name2[-1] + ' имеет номер зачетной книжки ' + numbook[-1]
            elif search1 == name1[-1] and search2 == asks[3] or search1 == name2[-1] and search2 == asks[3]:
                searchresult = 'Информация по вашему запросу: ' + name1[-1] + ' ' + name2[-1] + ' имеет домашний адрес: ' + homeadress[-1]
            elif search1 == name1[-1] and search2 == asks[4] or search1 == name2[-1] and search2 == asks[4]:
                searchresult = 'Информация по вашему запросу: ' + name1[-1] + ' ' + name2[-1] + ' имеет мутацию: ' + mutation[-1]
            elif search1 == name1[-1] and search2 == asks[5] or search1 == name2[-1] and search2 == asks[5]:
                searchresult = 'Информация по вашему запросу: ' + name1[-1] + ' ' + name2[-1] + ' имеет опекуна: ' + parents[-1]
            elif search1 == name1[-1] and search2 == asks[-1] or search1 == name2[-1] and search2 == asks[-1]:
                searchresult = 'Информация по вашему запросу: ' + name1[-1] + ' ' + name2[-1] + '. Статус: ' + realitionship[1]
                searchresult = 'Информация по вашему запросу: ' + name1[0] + ' ' + name2[0] + '. Краткая  информация: '
                print(searchresult)
            else:
                searchresult = 'Неверный запрос.'
            print(searchresult)