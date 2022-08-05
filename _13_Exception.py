
# Используется обработка попытки распечатать несуществующую
# переменную
def process_data():
    try:
        print(x)
    except NameError:
        print("Переменная не определена")
    except:
        print('Другая ошибка', end=' ')

# Используется обработка ошибки преобразования
def process_data2(inputs):
    numbers3 = []
    for my_input in inputs:
        try:
            my_num = int(my_input)
            if int(my_input):
                print(my_num, end=' ')
        except:
            print("Не число", end=' ')
        else:
            numbers3.append(my_num)
    print("")
    print("")
    for my_numbers3 in numbers3:
        print(my_numbers3, end=' ')

# Используется обработка попытки записи в файл
# открытый на чтение
def process_data3():
    try:
        f = open("demo.txt", "r", encoding='utf-8')
        f.write("Привет")
    except:
        print("Ошибка при записи в файл")
    finally:
        f.close()

def main():
    process_data()
    print("")

    numbers2 = ['2', '3', 'Hello', '7', '11', '16']
    process_data2(numbers2)
    print("")
    print("")

    process_data3()
    print("")
    return 0

if __name__ == '__main__':
    main()

