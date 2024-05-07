import datetime
from helper_classes import Transaction

# Вывести баланс на экран
def balance(wallet):
    print(wallet)

    # Дополнительо вывести на экран транзакии
    ans = input("Желаете ли вы увидеть транзакции?: ").strip()
    if ans.lower() in ["да", "0"]:
        deposits = "\nДоходы:\n\n"
        withdrawals = "Расходы:\n\n"
        for trans in wallet.trans_list:
            if trans.category == "Доход":
                deposits = deposits + trans.print_out() + "\n"
            else:
                withdrawals = withdrawals + trans.print_out() + "\n"
        print(f"{deposits}\n{withdrawals}")

# Добавить новую транзакцию в кошелек
def add(wallet):
    date = add_date()
    category = add_category()
    val = add_val()
    desc = input("Описание: ").strip().capitalize()

    transaction = Transaction(date, category, val, desc)
    if category == "Расход":
        wallet.withdraw(val)
    else:
        wallet.deposit(val)
    wallet.add_trans(transaction)
    print(wallet)
    return wallet

# Найти транзакции в кошельке
# Выводит на экран найденные транзакции
# return: список транзакции
def find(list):
    while True:
        type = input("По какому типу хотите найти транзакцию?: ").strip().lower()
        if type in ["дата", "1","категория","2","сумма","3"]:
            break
        else:
            print("Некорректный тип")
    date, category, val = None, "", -1
    if type in ["дата", "1"]:
        date = add_date()
    elif type in ["категория", "2"]:
        category = add_category()
    else:
        val = add_val()
    transactions = []
    print()
    for trans in list:
        if trans.date == date or trans.category == category or trans.val == val:
            print(trans.print_out())
            transactions.append(trans)
    if len(transactions) == 0:
        print("Записей не найдено")
    return transactions

# Изменить транзакцию в кошельке
def redact(wallet):

    # Найти транзакцию для редактирования
    transactions = find(wallet.trans_list)
    iter = 0
    while len(transactions) > 1:
        if iter == 5:
            print("Too many loops")
            break
        iter += 1
        transactions = find(transactions)
    
    # Редактировать транзакцию при нахождении одной записи
    if len(transactions) == 1:
        transactions = transactions[0]
        for i, trans in enumerate(wallet.trans_list):
            if transactions.date == trans.date and transactions.category == trans.category and transactions.val == trans.val:
                index = i

        # Редактировать по типу записи
        dmod = input("Хотите ли изменить дату?: ").strip()
        if dmod.lower() in ["да", "0"]:
            date = add_date()
            wallet.trans_list[index].date = date
        cmod = input("Хотите ли изменить категорию?: ").strip()
        if cmod.lower() in ["да", "0"]:
            cat = add_category
            wallet.trans_list[index].category = cat
        vmod = input("Хотите ли изменить сумму?: ").strip()
        if vmod.lower() in ["да", "0"]:
            value = add_val()
            wallet.trans_list[index].val = value
        wallet.calc_current()

    return wallet

### Функции для add ###
# Добавить корректную дату: проверяет через datetime 
def add_date():
    while True:
        user = input("Введите дату или 0 для сегодняшней даты: ").strip()

        # Проверить особый случай: 0 вместо даты для сегоднешней даты
        if user == '0':
            date = datetime.date.today()   
            break
        # Проверить формат даты
        try:
            date = datetime.date.fromisoformat(user)
            break
        except:
            print("Дата должна быть в формате ГГГГ-ММ-ДД")
    return date

# Добавить корректную категорию транзакции: Доход или Расход
def add_category():
    while True:
        category = input("Категория транзакции: ").strip()
        if category.lower() in ["доход", "расход"]:
            break
        else:
            print("Доход или Расход")
    return category.capitalize()

# Добавить корректную сумму: Больше нуля
def add_val():
    while True:
        try:
            val = int(input("Введите сумму: ").strip())
            if val > 0:
                break
        except:
            print("Введите положительное число")
    return val