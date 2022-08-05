
# Используется обработка попытки распечатать несуществующую
# переменную
def process_data():
    try:
        print(x)
    except NameError:
        print("Переменная не определена")
    except:
        print('Другая ошибка', end=' ')


def main():
    
    process_data()
    print("")
    
    
if __name__ == '__main__':
    main()

