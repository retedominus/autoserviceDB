# название таблицы БД
import model_common as mod_c


def view_all(f_name, show_field_names: list = [], divider: str = ' '):
    # читаем файл и помещаем его в объект словарь класса csv.DictReader
    # show_field_names - список полей для отображения, если не задан - [] по умолчанию,
    # то значит отобразить все поля таблицы.
    # divider - строковый разделитель, с помощью которого объединяются поля в единую строку
    # (по умолчанию разделитель равен пробелу)

    # Получаем из файла reader - список словарей
    reader, field_names, status_message = mod_c.read_all_table(f_name)
    if status_message != '':
        print(f'ошибка чтения {f_name}')
        return False
    # в начале выводим заголовок
    # для отображения используем список полей show_field_names, если он задан.
    # А если он пуст - [], то выводим все поля таблицы row.keys()
    tmp = []
    for fld in show_field_names if show_field_names else field_names:
        tmp.append(fld)
    tmp_str = divider.join(tmp)
    print(tmp_str)
    # для каждой строки cписка словарей (таблица читается в виде списка словарей)
    for row in reader:
        # выводим поля через разделитель divider
        tmp = []
        for fld in show_field_names if show_field_names else field_names:
            tmp.append(row[fld])
        tmp_str = divider.join(tmp)
        print(tmp_str)
    return True


# #Вывод всех записей
# show_fields = ['ModelMark', 'Reg_num', 'id_vehicle'] #список поле вывода, если нужно не все вывести
# #view_all(mod_c.vehicles_fname, show_fields, '*****')
# view_all(mod_c.vehicles_fname, divider='*****')
# print()
# view_all(mod_c.personal_fname, divider='  ')



#Добавление записи. В словаре новой записи не обязательно все поля должны быть заполнены
new_rec_dat = {'ModelMark': 'Porsche Cayenne', 'Reg_num': 'В345ТЕ99'}
#список всех полей таблицы
field_names = ['id_vehicle', 'ModelMark', 'Manufact_date', 'Reg_num', 'id_client']
id_name = 'id_vehicle'

status, rec_id = mod_c.create_rec_table(mod_c.vehicles_fname, new_rec_dat, field_names, id_name)
print(status, rec_id)