def show_greetings():
    print("Добро пожаловать в autoserviceDB!")


def input_client_first_name():
    return input("Введите имя клиента\n")

def input_client_family_name():
    return input("Введите фамилию клиента\n")

def input_client_middle_name():
    return input("Введите отчество клиента\n")

def input_client_birth_date():
    return input("Введите дату рождения клиента\n")

def input_client_phones():
    return input("Введите телефон(ы) клиента\n")

def input_id_work():
    return input("Введите id оказанной услуги\n")

def input_pers_id():
    return input("Введите id сотрудника фирмы\n")

def input_pers_first_name():
    return input("Введите имя клиента\n")

def input_pers_family_name():
    return input("Введите фамилию клиента\n")

def input_pers_middle_name():
    return input("Введите отчество клиента\n")

def input_pers_birth_date():
    return input("Введите дату рождения клиента\n")

def input_pers_phones():
    return input("Введите телефон(ы) клиента\n")

def input_pers_position():
    return input("Введите должность клиента\n")

def input_work_description():
    return input("Введите описание оказанной услуги\n")

def input_work_begin_date():
    return input("Введите дату начала оказания услуги\n")

def input_work_end_date():
    return input("Введите дату окончания оказания услуги\n")

def input_work_price():
    return input("Введите стоимость оказываемой услуги\n")

def input_id_status():
    return input("Введите id статуса работ\n")


def input_technician_fio():
    return input("Введите фио слесаря\n")


def input_vehicle_model():
    return input("Введите модель транспортного средства\n")

def input_vehicle_id():
    return input("Введите id транспортного средства\n")


def input_gov_number():
    return input("Введите гос. номер\n")

def input_id_client():
    return input("Введите id клиента\n")


def input_repairs_start():
    return input("Введите время начала ремонта\n")


def input_repairs_end():
    return input("Введите время окончания ремонта\n")


def show_srvice_menu():
    return input(
        "1 - Показать информацию об услуге\n2 - Добавить информацию об услуге\n3 - Удалить информацию об услуге\n4 - Выход\n")


def show_category_menu():
    return input(
        "\n1 - Информация об автомобилях\n2 - Информация о клиентах\n3 - Журнал услуг\n4 - Учет персонала\n5 - Выход\n")


def show_action_menu():
    return input(
        "\n1 - Добавить запись\n2 - Найти запись\n3 - Вывести все записи\n4 - Редактировать запись\n5 - Удалить запись\n6 - Назад\n")


def show_success():
    print("Успешно выполнено")


def show_result(result):
    print(f"Результат операции: {result}")


# Takes list of rows
# Each row is a list of strings
# @param table: List<List<String>>
def show_table(table):
    spans = __count_spans(table)
    __print_row_border(spans)
    __print_table_rows(table, spans)


def show_error(error):
    print(f"Произошла ошибка: {error}")


def show_goodbye():
    print("Вы вышли из программы")


# Takes list of lengths of the columns in symbols
# @ param spans: List<Int>
def __print_row_border(spans):
    print(f"|{'|'.join(list(map(__int_to_span, spans)))}|")


# Takes list of rows
# Each row is a list of strings
# @param table: List<List<String>>
# @param spans: List<Int>
def __print_table_rows(table, spans):
    for row in table:
        __print_table_row(row, spans)
        __print_row_border(spans)


# @param row: List<String>
# @param spans: List<Int>
def __print_table_row(row, spans):
    output_row = "|"
    index = 0
    while index < len(row):
        output_row += row[index]
        output_row += (" " * (spans[index] - len(row[index])))
        output_row += "|"
        index += 1
    print(output_row)


# Takes list of rows
# Each row is a list of strings
# @param table: List<List<String>>
def __count_spans(table):
    spans = list(map(__map_list_to_spans, table))
    spans_rotated = [list(column) for column in zip(*spans)]
    max_spans = list(map(max, spans_rotated))
    return max_spans


def __int_to_span(num):
    return "-" * num


# @param row: List<String>
def __map_list_to_spans(row):
    return list(map(lambda s: len(s), row))
