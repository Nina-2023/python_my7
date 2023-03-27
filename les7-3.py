class Cell:
    # Класс
    def __init__(self, num_cells):
        self.num_cells = num_cells

    # Операторы:
    # Сложение
    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

    # Вычитание
    def __sub__(self, other):
        # Проверка условия
        if self.num_cells - other.num_cells < 0:
            return "Разность количества ячеек двух клеток меньше нуля"
        else:
            return Cell(self.num_cells - other.num_cells)

    # Умножение
    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    # Деление
    def __truediv__(self, other):
        return Cell(self.num_cells // other.num_cells)

    # Метод make_order для формирования рядов
    def make_order(self, num_cells_in_row):
        # Определение количества рядов
        num_rows = self.num_cells // num_cells_in_row
        # Определение количества ячеек в последнем ряду
        num_cells_in_last_row = self.num_cells % num_cells_in_row
        # Формирование строки
        row_string = '*' * num_cells_in_row + '\n'
        row_string *= num_rows
        row_string += '*' * num_cells_in_last_row
        return row_string

# Пример: Инициализация двух экземпляров класса
cell_1 = Cell(12)
cell_2 = Cell(15)

# Сложение
result_1 = cell_1 + cell_2
print(f"Количество ячеек после сложения: {result_1.num_cells}")

# Вычитание
result_2 = cell_1 - cell_2
print(result_2)

# Умножение
result_3 = cell_1 * cell_2
print(f"Количество ячеек после умножения: {result_3.num_cells}")

# Деление
result_4 = cell_1 / cell_2
print(f"Количество ячеек после деления: {result_4.num_cells}")

# Формирование рядов
print(cell_1.make_order(5))