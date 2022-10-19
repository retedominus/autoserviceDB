#read_csv_file, write_csv_file - базовые методы чтения записи в csv
from model_csv import read_csv_file, write_csv_file

# название файлов таблиц БД:
vehicles_fname = 'db/vehicles.csv'
personal_fname = 'db/personal.csv'
clients_fname = 'db/clients.csv'
status_fname = 'db/status.csv'
worklog_fname = 'db/worklog.csv'
counters_fname = 'db/counters.csv'


def create_rec(f_name: str, new_rec_dat: dict, key_names: list, id_name: str):
    # функция создает новую запись в таблице транспортных средств
    # парамерты:
    # new_rec_dat - словарь с данными для создаваемой записи
    # key_names - список ключей для создаваемой записи. важен для пустой таблицы
    # id_name - название поля идентификатора
    # функция возвращает True и идентификатор новой записи или False и сообщение об ошибке

    # читаем таблицу БД по автомобилям в список словарей - reader
    reader, status = read_csv_file(f_name)

    # если таблица reader не пустая, то проверяем список ключей key_names,
    # чтобы в нем были значения ключей такие же, как в таблице reader
    # if len(reader) > 0:
    #     for k in key_names:
    #         if not (k in reader[0].keys()):
    #             return False, 'ошибка создания записи в таблице vehicles. неверно указано название поля'

    # Создаем пустой словарь для новой записи в таблице БД
    new_rec = {}
    # заполняем ключ-значения нового словаря данными из параметра new_rec_dat
    for k in key_names:
        if k in new_rec_dat.keys():
            new_rec[k] = new_rec_dat[k]
        else:
            # если такого поля нет в словаре new_rec_dat, то присваиваем значение ''
            new_rec[k] = ''
    # вычисляем максимальное значение поля идентификатора, +1 - новое значение идентификатора
    max_id = 0
    for row in reader:
        if int(row[id_name]) > max_id:
            max_id = row[id_name]
    new_id = max_id + 1
    print(new_id)
    new_rec[id_name] = max_id + 1
    # Добавляем новую запись в список словарей
    reader.append(';'.join(key_names) + ':' + ';'.join(new_rec.values()))

    # перезаписываем таблицу в БД
    status, message = write_csv_file(f_name, reader)

    return True, new_id

def read_all_table(f_name: str):
    # функция создает новую запись в таблице транспортных средств
    # парамерты:
    # функция возвращает кортеж список словарей записей таблицы и сообщение об ошибке:
    #в случае успеха: строки таблицы (список словарей reader), пустое сообщение об ошибке
    # в случае ошибки None и сообщение об ошибке

    # читаем таблицу БД по автомобилям в список словарей - reader
    reader, status_message = read_csv_file(f_name)
    if status_message != '':
        return None, f'Ошибка чтения данных из таблицы базы данных {f_name}'
    return reader, ''

