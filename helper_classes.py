import sys

# Класс для хранения транзакции
# vars: дата, категория, сумма, описание
# Описание может быть пустым
class Transaction:
    def __init__(self, date, category, val, desc = ""):
        self.date = date
        self.category = category
        self.val = val
        self.desc = desc

        @property
        def date(self):
            return self._date
        @date.setter
        def date(self, date):
            if not date:
                sys,exit("Введите дату")
            self._date = date

        @property
        def category(self):
            if not category:
                sys.exit("Введите категорию")
            return self._category
        @category.setter
        def category(self, category):
            self._category = category

        @property
        def val(self):
            if not val:
                sys.exit("Введите сумму")
            return self._val
        @val.setter
        def val(self, val):
            self._val = val

    def print_out(self):
        return f"""Дата: {self.date}
Категория: {self.category}
Сумма: {self.val}
Описание: {self.desc}\n"""

# Кошелек
# vars: баланс и список транзакции
class Wallet:
    def __init__(self, current = 0):
        self.current = current
        self.trans_list = []
    
    # Пересчитать баланс при редактировании информации
    def calc_current(self):
        current = 0
        for trans in self.trans_list:
            if trans.category == "Доход":
                current = current + trans.val
            else:
                current = current - trans.val
        self.current = current

    # Добавить транзакцию в список
    def add_trans(self, transaction):
        self.trans_list.append(transaction)

    # Добавить сумму в баланс при доходе
    def deposit(self, val):
        self.current = self.current + val

    # Убрать сумму при расходе
    def withdraw(self, val):
        if self.current - val < 0:
            sys.exit(f"Недостаточно средств\n{self.__str__()}")
        self.current = self.current - val

    def __str__(self):
        return f"Баланс: {self.current}"
    
