import csv
import shutil

# для файлов UTF-8 with BOM (это где есть русский текст) в python задавать кодировку
# encoding='utf-8-sig'
# если задать my_encoding='utf-8' то в каждой считанной строке появляется '\ufeff'

def read_csv_file(f_name, my_encoding='utf-8-sig'):
    # функция читает csv-файл (по сути таблицу БД).
    # Первая строка в csv-файле должна быть заголовком - это ключи словаря

    # функция возвращает: res - прочитанный из файла набор данных в виде списка словарей
    # (каждый словарь - это строка таблицы БД)
    # field_names - список названий полей таблицы (читает из первой строки)
    # и статус операции пустая строка - успешно считан, иначе текст ошибки.

    res = []
    field_names = []
    try:
        with open(f_name, "r", encoding=my_encoding) as file:
            # метод csv.DictReader(file, delimiter=";") обязательно надо вызывать с параметром delimeter=';'
            # , иначе словарь не разобьется на пары ключ-значение и будет ошибка при обращении row[keyname]
            reader = csv.DictReader(file, delimiter=';')
            # список названий полей таблицы
            field_names = reader.fieldnames
            # формируем список словарей (строк) таблицы
            for row in reader:  # каждая строка - это словарь
                # добавляем строку - словарь в результирующий список словарей
                res.append(row)
    except Exception as e:
        return [], field_names, f'Ошибка при чтении из файла {f_name}. {e}'
    return res, field_names, ''


def write_csv_file(f_name, dat, fldnames: list, my_encoding='utf-8-sig'):
    # функция записывает список словарей dat в csv-файл (по сути таблицу БД).
    # Идет полная перезапись файла, поэтому исходные данные должны содержать полную таблицу,
    # а не выборку
    # параметры:
    # f_name - название файла, включая подкаталог
    # dat - набор записываемых данных - список словарей
    # fldnames - список названий полей
    # Результат - функция возвращает кортеж:
    # либо True  и ''
    # либо False и сообщение об ошибке
    try:
        shutil.copy(f_name, f_name.replace('.csv','.bak'))
    except Exception as e:
        return False, f'Ошибка создания резервной копии файла {f_name}. {e}'

    try:
        with open(f_name, 'w', encoding=my_encoding, newline='') as file:
            dict_writer = csv.DictWriter(file, delimiter=';', fieldnames=fldnames)
            dict_writer.writeheader()
            dict_writer.writerows(dat)
    except Exception as e:
        return False, f'Ошибка записи в файл {f_name}. {e}'
    return True, ''


def append_to_csv_file(f_name, dat, fldnames: list, my_encoding='utf-8-sig'):
    # функция добавляет список словарей dat в csv-файл f_name
    # параметры:
    # f_name - название файла, включая подкаталог
    # dat - набор записываемых данных - список словарей
    # fldnames - список названий полей
    # Результат - функция возвращает кортеж:
    # либо True  и ''
    # либо False и сообщение об ошибке
    try:
        with open(f_name, 'a', encoding=my_encoding, newline='') as file:
            dict_writer = csv.DictWriter(file, delimiter=';', fieldnames=fldnames)
            dict_writer.writerow(dat)
    except Exception as e:
        return False, f'Ошибка записи в файл {f_name}. {e}'
    return True, ''
