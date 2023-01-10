print('I')
def unique_nums(num):
    uq = []
    for i in num:
        if i not in uq:
            uq.append(i)
        else:
            continue
    return (uq)

lst = [1, 2, 4, 2, 3, 3, 1, 5, 5]
print(unique_nums(lst))


print('II')
def square_digits(num):
    uq = ''
    for i in str(num):
        uq += str(int(i) ** 2)
    return (int(uq))

lst = 9119
print(square_digits(lst))


print('III')
class MyError(Exception):
    def __init__(self, text):
        self.text = text

a = input("Введите число от 1 до 100: ")

try:
    a = int(a)
    if a > 100 or a < 1:
        raise MyError(f"Недопустимое значение: {a}. Число должен быть в диапазоне от 1 до 100" )
    print(a)
except ValueError:
    print("Введены некорректные данные")
except MyError as mr:
    print(mr)


print('IV')
class Order:
    order_status = "Не доставлен"

    def __init__(self, num_order, title, fio, home, status):
        self._num_order = num_order
        self._title = title
        self._fio = fio
        self._home = home
        self._status = status

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, s):
        self._status = s

    def info(self):
        print("Номер заказа: " + str(self._num_order))
        print("Наименование: " + self._title)
        print("ФИО: " + self._fio)
        print("Адрес: " + self._home)
        print("Статус заказа: " + self._status)

o = Order(10, 'qwerty','Петров', 'екб', Order.order_status)
o.info()
o.status = "Доставлен"
o.info()
