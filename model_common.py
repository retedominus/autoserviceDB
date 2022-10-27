# read_csv_file, write_csv_file - базовые методы чтения записи в csv
from model_csv import read_csv_file, write_csv_file, append_to_csv_file

vehicles_fname = 'db/vehicles.csv'
personal_fname = 'db/personal.csv'
clients_fname = 'db/clients.csv'
status_fname = 'db/status.csv'
worklog_fname = 'db/worklog.csv'
counters_fname = 'db/counters.csv'


def create_rec_table(f_name: str, new_rec_dat: dict, tbl_field_names: list, id_name: str):
    # функция создает новую запись в таблице
    # парамерты:
    # new_rec_dat - словарь с данными для создаваемой записи
    # tbl_field_names - список полей таблицы. особенно важно для пустой таблицы БД
    # id_name - название поля идентификатора
    # функция возвращает кортеж:
    # либо True (успешно создана запись), идентификатор новой записи
    # либо False (ошибка создания записи), сообщение об ошибке

    # Создаем пустой словарь для новой записи в таблице БД
    new_rec = {}
    # заполняем ключ-значения нового словаря данными из параметра new_rec_dat
    for k in tbl_field_names:
        if k in new_rec_dat.keys():
            new_rec[k] = new_rec_dat[k]
        else:
            # если такого поля нет в словаре new_rec_dat, то присваиваем значение ''
            new_rec[k] = ''
    # вычисляем максимальное значение поля идентификатора, +1 - новое значение идентификатора
    # считываем значение счетчика из таблицы БД counters, где хранятся счетчики
    cnt_reader, cnt_field_names, message_status = read_csv_file(counters_fname)
    if message_status != '':
        return False, message_status
    # находим значение счетчика первичного ключа для таблицы f_name
    for row in cnt_reader:
        if (row['fname']) == f_name:
            new_id = int(row['cur_cnt'])
            # обновляем значение счетчика в наборе данных cnt_reader. Далее его надо сохранить в БД
            row['cur_cnt'] = new_id + 1
            break
    new_rec[id_name] = new_id

    # добавляем запись в таблицу БД
    bool_status, message_status = append_to_csv_file(f_name, new_rec, tbl_field_names)
    # если была ошибка прекращаем выполнение функции
    if bool_status == False:
        return False, message_status

    # в таблице counters увеличиваем значение счетчика на 1
    bool_status, message_status = write_csv_file(counters_fname, cnt_reader, cnt_field_names)
    if bool_status == False:
        return False, message_status
    # иначе все операции должны успешно выполниться,
    # поэтому вовзращаем True и идентификатор новой записи
    return True, new_id


# старое через полный write
# def create_rec_table(f_name: str, new_rec_dat: dict, tbl_field_names: list, id_name: str):
#     # функция создает новую запись в таблице транспортных средств
#     # парамерты:
#     # new_rec_dat - словарь с данными для создаваемой записи
#     # tbl_field_names - список полей таблицы. особенно важно для пустой таблицы БД
#     # id_name - название поля идентификатора
#     # функция возвращает кортеж:
#     # либо True (успешно создана запись), идентификатор новой записи
#     # либо False (ошибка создания записи), сообщение об ошибке
#
#     # читаем таблицу БД в список словарей - reader
#     reader, fields_names, message_status = read_csv_file(f_name)
#
#     # если таблица reader не пустая, то проверяем список ключей key_names,
#     # чтобы в нем были значения ключей такие же, как в таблице reader
#     # if len(reader) > 0:
#     #     for k in key_names:
#     #         if not (k in reader[0].keys()):
#     #             return False, 'ошибка создания записи в таблице vehicles. неверно указано название поля'
#
#     # Создаем пустой словарь для новой записи в таблице БД
#     new_rec = {}
#     # заполняем ключ-значения нового словаря данными из параметра new_rec_dat
#     for k in tbl_field_names:
#         if k in new_rec_dat.keys():
#             new_rec[k] = new_rec_dat[k]
#         else:
#             # если такого поля нет в словаре new_rec_dat, то присваиваем значение ''
#             new_rec[k] = ''
#     # вычисляем максимальное значение поля идентификатора, +1 - новое значение идентификатора
#     # считываем значение счетчика из таблицы БД counters, где хранятся счетчики
#     cnt_reader, message_status = read_csv_file(counters_fname)
#     if message_status != '':
#         return False, message_status
#         #return False, f'Ошибка чтения таблицы {counters_fname}'
#     # находим значение счетчика для данной таблицы
#     for row in cnt_reader:
#         if (row['fname']) == f_name:
#             new_id = int(row['cur_cnt']) + 1
#             # обновляем значение счетчика в наборе данных cnt_reader. Далее его надо сохранить в БД
#             row['cur_cnt'] = new_id
#             break
#     new_rec[id_name] = new_id
#     # Добавляем новую запись в список словарей
#     reader.append(new_rec)
#     # reader.append(';'.join(tbl_field_names) + ':' + ';'.join(new_rec.values()))
#
#     # перезаписываем таблицу в БД
#     bool_status, message_status = write_csv_file(f_name, reader, tbl_field_names)
#     # если была ошибка прекращаем выполнение функции
#     if bool_status == False:
#         return False, message_status
#
#     # в таблице counters увеличиваем значение счетчика на 1
#     bool_status, message_status = write_csv_file(counters_fname, cnt_reader)
#     if bool_status == False:
#         return False, message_status
#     # иначе все операции должны успешно выполниться,
#     # поэтому вовзращаем True и идентификатор новой записи
#     return True, new_id

def read_all_table(f_name: str):
    # функция создает новую запись в таблице транспортных средств
    # парамерты:
    # функция возвращает кортеж список словарей записей таблицы и сообщение об ошибке:
    # в случае успеха:
    # reader - строки таблицы (список словарей reader),
    # field_names - список названий полей таблицы
    # пустое сообщение об ошибке

    # в случае ошибки возвращается: None, None и сообщение об ошибке

    # читаем таблицу БД по автомобилям в список словарей - reader
    reader, field_names, status_message = read_csv_file(f_name)
    if status_message != '':
        return None, None, f'Ошибка чтения данных из таблицы базы данных {f_name}'
    return reader, field_names, ''


def update_rec_table(f_name: str, upd_rec_dat: dict, id_name: str):
    # функция обновляет запись в таблице f_name
    # парамерты:
    # upd_rec_dat - словарь записи с обновленными данными
    # tbl_field_names - полный список полей таблицы. особенно важно для заполнения пустых полей.
    # id_name - название поля идентификатора
    # функция возвращает кортеж:
    # либо True (успешно создана запись), идентификатор новой записи
    # либо False (ошибка создания записи), сообщение об ошибке

    # читаем таблицу БД в список словарей - reader
    reader, fields_names, message_status = read_csv_file(f_name)

    # если таблица reader не пустая, то проверяем список ключей key_names,
    # чтобы в нем были значения ключей такие же, как в таблице reader
    if len(reader) > 0:
        for k in fields_names:
            if not (k in reader[0].keys()):
                return False, f'В параметре функции update_rec_table неверно указаны названия полей обновляемй записи: {k}'

    upd_rec = []
    isFinded = False
    # находим запись в таблице reader,
    # идентификатор которой соответсвует записи upd_rec_dat[id_name]
    for row in reader:
        if row[id_name] == upd_rec_dat[id_name]:
            # устанавливаем ссылку upd_rec на найденную запись
            upd_rec = row
            isFinded = True
            break
    # если такая запись не была найдена по идентификатору, то прекращаем выполнение функции
    if isFinded == False:
        return False, 'Ошибка. Обновляемая запись не найдена по идентификатору!'

    for k in fields_names:
        if k in upd_rec_dat.keys():
            upd_rec[k] = upd_rec_dat[k]
        else:
            # если такого поля нет в словаре upd_rec_dat, то присваиваем полю значение '',
            # то есть считается что это полю присвоено пустое значение
            upd_rec[k] = ''

    # делаем сначала резервную копию таблицы БД


    # перезаписываем таблицу в БД. Функция write_csv_file содержит код
    # создания резерной копии файла (с расширением .bak), перед полной перезаписью файла
    bool_status, message_status = write_csv_file(f_name, reader, fields_names)
    if bool_status == False:
        return False, message_status

    # иначе все операции должны успешно выполниться, поэтому возвращаем True, ''
    return True, ''
