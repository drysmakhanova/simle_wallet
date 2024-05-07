import argparse
import os.path
import pickle
from helper_classes import Wallet 
from helper_functions import balance, add, redact, find

def main(*args, **kwargs):

    # Получить и парсить аргументы с консольной строки
    parser = argparse.ArgumentParser(usage='wallet.py [options]', description='Кошелек со счетом и транзакциями')
    parser.add_argument('-b', '--balance', action='store_true', help="Вывод текущего баланса")
    parser.add_argument('-n','--new', action='store_true', help="Добавить новую запись в транзакции")
    parser.add_argument('-r','--redact', action='store_true', help="Редактировать запись в транзакциях")
    parser.add_argument('-f','--find', action='store_true', help="Поиск по записям в транзакциях")
    args = parser.parse_args()
    arg = list(vars(args).keys())[list(vars(args).values()).index(True)]
    
    # Данные хранятся в одном файле, кошелек хранится в class объекте и пишется через pickle
    filename = "wallet.txt"
    
    # Если есть существующий файл и он не пустой: открываем его. Если файл не существует: создается новый
    # Файл читается и пишется через байт формат 
    if os.path.isfile(filename) and os.path.getsize(filename) > 0:
        with open(filename, "rb") as file:
            wallet = pickle.load(file)
    else:
        with open(filename, "wb") as file:
            wallet = Wallet()
            pickle.dump(wallet, file)

    # Если аргумент верный, отправляем на функции из helper_functions 
    if arg == "balance":
        balance(wallet)
    elif arg == "new":
        wallet = add(wallet)
    elif arg == "find":
        find(wallet.trans_list)
    elif arg == "redact":
        wallet = redact(wallet)

    # Запись кошелька в файл после манипуляции
    with open(filename, "wb") as file:
        pickle.dump(wallet, file)

if __name__ == '__main__':
    main()

