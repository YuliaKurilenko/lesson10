try:
    class Digit(Exception):
        pass
    def f(a,b):
        if b == 0:
            raise Digit('делить на ноль нельзя')
        return a / b
except Digit as exc:
    print(f'Ошибка: {exc}')
print(f(7,1))
try:
    class NameError(Exception):
        pass
    def f(name):
        if name == "Кира":
            raise Exception('Добрый день,Кира')
        print(f'Добрый вечер,{name}')
except NameError as exc:
    print(f'Ошибка {exc}')
f("Оля")
