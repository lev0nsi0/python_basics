"""
Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__floordiv__, __truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток, соответственно.

Сложение. Объединение двух клеток.
   При этом число ячеек общей клетки должно равняться сумме ячеек исходных
   двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять,
   только если разность количества ячеек двух клеток больше нуля,
   иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки
   — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется
   как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр
класса и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""

class Cell:
    def __init__(self, cell):
        self.cell = cell

    # Декоратор проверки аргументов на ноль
    def check_zero(func):
        def tag_wrapper(self, other):
            if self.cell == 0 or other.cell == 0:
                print("Недопустимый аргумент -"
                      " клетка не может содержать ноль ячеек")
            else:
                return func(self, other)
        return tag_wrapper

    @check_zero
    def __add__(self, other):
        return Cell(self.cell + other.cell)

    @check_zero
    def __sub__(self, other):
        if other.cell > self.cell:
            print("Операция невозможна - вторая клетка больше первой")
        else:
            return Cell(self.cell - other.cell)

    @check_zero
    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    @check_zero
    def __floordiv__(self, other):
            return Cell(self.cell // other.cell)

    def __str__(self):
        return str(self.cell)

    def make_order(self, cells_row):
        rows, rest = self.cell // cells_row, self.cell % cells_row
        return '\\n'.join(['*' * cells_row] * rows +
                          (['*' * rest] if rest else []))


if __name__ == '__main__':
    a_cell = Cell(26)
    b_cell = Cell(12)

    print('Количество ячеек в клетке a_cell - ', a_cell)
    print("вывод клетки a_cell с шагом 5:", a_cell.make_order(5))
    print()
    print('Количество ячеек в клетке b_cell - ', b_cell)
    print("вывод клетки b_cell с шагом 4:", b_cell.make_order(4))
    print()
    print('Сложение -  ', a_cell + b_cell)
    print('Вычитание -  ', a_cell - b_cell)
    print('Вычитание (при b>a) -  ', b_cell - a_cell)
    print('Умножение -  ', a_cell * b_cell)
    print('Целочисленное деление -  ', a_cell // b_cell)

# Количество ячеек в клетке a_cell -  26
# вывод клетки a_cell с шагом 5: *****\n*****\n*****\n*****\n*****\n*
#
# Количество ячеек в клетке b_cell -  12
# вывод клетки b_cell с шагом 4: ****\n****\n****
#
# Сложение -   38
# Вычитание -   14
# Операция невозможна - вторая клетка больше первой
# Вычитание (при b>a) -   None
# Умножение -   312
# Целочисленное деление -   2