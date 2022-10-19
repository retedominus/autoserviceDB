import csv


def read_csv_file(f_name, my_encoding='utf-8'):
    # функция читает csv-файл (по сути таблицу БД).
    # Первая строка в csv-файле должна быть заголовком - это ключи словаря

    # функция возвращает прочитанную из файла таблицу в виде списка словарей и
    # строку пустая строка - успешно считан, иначе текст ошибки.
    # каждый словарь - это строка таблицы БД
    res = []
    try:
        with open(f_name, "r", encoding=my_encoding) as file:
            # метод csv.DictReader(file, delimiter=";") обязательно надо вызывать с параметром delimeter=';'
            # , иначе словарь не разобьется на пары ключ-значение и будет ошибка при обращении row[keyname]
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:  # каждая строка - это словарь
                # добавляем строку - словарь в результирующий список словарей
                res.append(row)
    except:
        return [], f'Ошибка при чтении из файла {f_name}'
    return res, ''


def write_csv_file(f_name, dat, my_encoding='utf-8'):
    # функция записывает список словарей в csv-файл (по сути таблицу БД).
    # Идет полная перезапись файла, поэтому исходные данные должны содержать полную таблицу,
    # а не выборку

    # функция возвращает True в случае успешной записи в файл.
    try:
        with open(f_name, 'w', encoding=my_encoding) as file:
            writer = csv.writer(file)
            writer.writerows(dat)
    except:
        return False, f'Ошибка записи в файл {f_name}'

    return True, ''


# def view_csv_file(f_name, show_field_names: list, divider: str = ' '):
#     # читаем файл и помещаем его в объект словарь класса csv.DictReader
#     # show_field_names - список полей для отображения
#     # divider - строковый разделитель, с помощью которого объединяются поля в единую строку
#     # (по умолчанию разделитель равен пробелу)
#
#     # Получаем из файла reader - список словарей
#     reader = read_csv_file(f_name)
#     # для каждой строки cписка словарей (таблица читается в виде списка словарей)
#     for row in reader:
#         # собираем выбранные поля show_field_names текущей строки row
#         # через разделитель divider
#         tmp = []
#         for fld in show_field_names:
#             tmp.append(row[fld])
#         tmp_str = divider.join(tmp)
#         print(tmp_str)

# data = [['id_vehicle', 'ModelMark', 'Manufact_date', 'Reg_num', 'id_client'],
#         ['4', 'Kia', '19.04.2000', 'Р734РК77', '4'],
#         ['1', 'Toyota Corolla', '01.10.2008', 'А436КТ163', '1'],
#         ['2', 'Nissan Pathfinder', '12.12.2015', 'М451ОВ78', '2'],
#         ['3', 'LADA Priora', '20.05.2020', 'Л542ПР99', '3']]

# write_db('db/vehicles.csv', data)
# print(read_db('db/vehicles.csv', "utf-8"))
