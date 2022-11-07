import view
# import model_csv as cs

import model_common as com
# import check
# import read_write as rw
import test_model_view as tmv


# import view_tests as vt

def split_list(p):
    g = []
    for i in p:
        g.append(i.split())
    return g


# текущая позиция в меню. Нужно для запоминая текущего положения
cur_menu_pos = []
view.show_greetings()
while True:
    match cur_menu_pos:
        # [] - означает отобразить главное меню
        case []:
            ch = view.show_category_menu()
            match ch:
                case ('1' | '2' | '3' | '4' | '5'):
                    if ch == '1':
                        f_name = 'db/vehicles.csv'
                    if ch == '2':
                        f_name = 'db/clients.csv'
                    if ch == '3':
                        f_name = 'db/worklog.csv'
                    if ch == '4':
                        f_name = 'db/personal.csv'
                    if ch == '5':
                        view.show_goodbye()
                        break
                    cur_menu_pos.append(ch)
                    # Выводим таблицу данных после редактирования записи
                    tbl_lists, field_names, status_message = com.read_all_table(f_name)
                    if status_message == '':
                        view.show_table(tbl_lists)
                case _:
                    f_name = ''
                    print('Введите целое число, выберите значение из списка.')

        # Выбор действия после выбора меню первого уровня 1, 2, 3, 4
        case (['1'] | ['2'] | ['3'] | ['4']):
            hc = view.show_action_menu()
            match hc:
                case ('1' | '2' | '3' | '4' | '5' | '6'):
                    cur_menu_pos.append(hc)
                case _:
                    print('Введите целое число, выберите значение из списка.')

        case (['1', '6'] | ['2', '6'] | ['3', '6'] | ['4', '6']):
            # Выбор - Назад, возврат в главное меню
            cur_menu_pos = []

        # ['1', '1'] - ['1', '5'] - Автомобили
        case ['1', '1']:
            f_name = 'db/vehicles.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Создать запись
            new_rec_dat = {'ModelMark': view.input_vehicle_model(), 'Manufact_date': view.input_repairs_start(),
                           'Reg_num': view.input_gov_number(),
                           'id_client': view.input_id_client()}
            field_names = ['id_vehicle', 'ModelMark', 'Manufact_date', 'Reg_num', 'id_client']
            id_name = 'id_vehicle'
            status, new_id = com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            if status:
                # После добавления записи выводим полный список
                tbl_lists, field_names, status_message = com.read_all_table(f_name)
                view.show_table(tbl_lists)
                print(f'Запись с id = {new_id} успешно создана в таблице.')
            else:
                print(f'Ошибка при создании новой записи в таблице.')

        case ['1', '2']:
            # Найти запись
            f_name = 'db/vehicles.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            find_id = view.input_vehicle_id()
            filter_dat = {'id_vehicle': find_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Найденные записи:')
                view.show_table(tbl_lists)
            else:
                print('соотвествующие записи не найдены.')

        case ['1', '3']:
            # Вывести все записи
            f_name = 'db/vehicles.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            divider = ' '
            show_field_names = []
            tbl_lists, field_names, status_message = com.read_all_table(f_name)
            if status_message == '':
                view.show_table(tbl_lists)

        case ['1', '4']:
            # Редактировать запись
            f_name = 'db/vehicles.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Запрашиваем id записи для редактирования
            edit_id = view.input_vehicle_id()
            filter_dat = {'id_vehicle': edit_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Редактирование данных. Текущие значения:')
                view.show_table(tbl_lists)
                print('Введите новые значения полей:')
                # Выводим значения полей для редактирования
                edit_rec_dat = {'id_vehicle': edit_id,
                                'ModelMark': view.input_vehicle_model(),
                                'Manufact_date': view.input_repairs_start(),
                                'Reg_num': view.input_gov_number(),
                                'id_client': view.input_id_client()}
                # Обновляем данные в БД
                status, mes1 = com.update_rec_table(f_name, edit_rec_dat, 'id_vehicle')
                if status:
                    print(f'Редактирование учетной записи выполнено успешно.')
                    # Выводим таблицу данных после редактирования записи
                    tbl_lists, field_names, status_message = com.read_all_table(f_name)
                    if status_message == '':
                        view.show_table(tbl_lists)
                else:
                    print(mes1)
            else:
                print('соответствующая запись не найдена.')

        case ['1', '5']:
            # Удалить запись
            f_name = 'db/vehicles.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            delrec_id = view.input_vehicle_id()
            filter_dat = {'id_vehicle': delrec_id}
            status, tbl_lists = com.delete_rec_table(f_name, filter_dat)
            if status and tbl_lists != []:
                view.show_table(tbl_lists)
                print(f'Запись с id = {delrec_id} успешно удалена в таблице.')
            else:
                print('соотвествующие записи не найдены.')

        # ['2', '1'] - ['2', '5'] - Клиенты
        case ['2', '1']:
            f_name = 'db/clients.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Создать запись
            new_rec_dat = {'first_name': view.input_client_first_name(),
                           'family_name': view.input_client_family_name(),
                           'middle_name': view.input_client_middle_name(),
                           'birth_date': view.input_client_birth_date(),
                           'phones': view.input_client_phones()}
            field_names = ['id_client', 'first_name', 'family_name', 'middle_name',
                           'birth_date', 'phones']
            id_name = 'id_client'
            status, new_id = com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            if status:
                # После добавления записи выводим полный список
                tbl_lists, field_names, status_message = com.read_all_table(f_name)
                view.show_table(tbl_lists)
                print(f'Запись с id = {new_id} успешно создана в таблице.')
            else:
                print(f'Ошибка при создании новой записи в таблице.')

        case ['2', '2']:
            # Найти запись
            f_name = 'db/clients.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            find_id = view.input_id_client()
            filter_dat = {'id_client': find_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Найденные записи:')
                view.show_table(tbl_lists)
            else:
                print('соотвествующие записи не найдены.')

        case ['2', '3']:
            # Вывести все записи
            f_name = 'db/clients.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            divider = ' '
            show_field_names = []
            tbl_lists, field_names, status_message = com.read_all_table(f_name)
            if status_message == '':
                view.show_table(tbl_lists)

        case ['2', '4']:
            # Редактировать запись
            f_name = 'db/clients.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Запрашиваем id записи для редактирования
            edit_id = view.input_id_client()
            filter_dat = {'id_client': edit_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Редактирование данных. Текущие значения:')
                view.show_table(tbl_lists)
                print('Введите новые значения полей:')
                # Выводим значения полей для редактирования
                edit_rec_dat = {'id_client': edit_id,
                                'first_name': view.input_client_first_name(),
                                'family_name': view.input_client_family_name(),
                                'middle_name': view.input_client_middle_name(),
                                'birth_date': view.input_client_birth_date(),
                                'phones': view.input_client_phones()}
                # Обновляем данные в БД
                status, mes1 = com.update_rec_table(f_name, edit_rec_dat, 'id_client')
                if status:
                    print(f'Редактирование учетной записи выполнено успешно.')
                    # Выводим таблицу данных после редактирования записи
                    tbl_lists, field_names, status_message = com.read_all_table(f_name)
                    if status_message == '':
                        view.show_table(tbl_lists)
                else:
                    print(mes1)
            else:
                print('соответствующая запись не найдена.')

        case ['2', '5']:
            # Удалить запись
            f_name = 'db/clients.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            delrec_id = view.input_id_client()
            filter_dat = {'id_client': delrec_id}
            status, tbl_lists = com.delete_rec_table(f_name, filter_dat)
            if status and tbl_lists != []:
                view.show_table(tbl_lists)
                print(f'Запись с id = {delrec_id} успешно удалена в таблице.')
            else:
                print('соотвествующие записи не найдены.')

        # ['3', '1'] - ['3', '5'] - Журнал услуг
        case ['3', '1']:
            f_name = 'db/worklog.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Создать запись
            new_rec_dat = {'id_vehicle': view.input_vehicle_id(),
                           'id_personal': view.input_id_personal(),
                           'Description': view.input_work_description(),
                           'Begin_date': view.input_work_begin_date(),
                           'end_date': view.input_work_end_date(),
                           'Price': view.input_work_price(),
                           'id_status': view.input_id_status()}
            field_names = ['id_work', 'id_vehicle', 'id_personal', 'Description',
                           'Begin_date', 'end_date', 'Price', 'id_status']
            id_name = 'id_work'
            status, new_id = com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            if status:
                # После добавления записи выводим полный список
                tbl_lists, field_names, status_message = com.read_all_table(f_name)
                view.show_table(tbl_lists)
                print(f'Запись с id = {new_id} успешно создана в таблице.')
            else:
                print(f'Ошибка при создании новой записи в таблице.')

        case ['3', '2']:
            # Найти запись
            f_name = 'db/worklog.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            find_id = view.input_id_client()
            filter_dat = {'id_client': find_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Найденные записи:')
                view.show_table(tbl_lists)
            else:
                print('соотвествующие записи не найдены.')

        case ['3', '3']:
            # Вывести все записи
            f_name = 'db/worklog.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            divider = ' '
            show_field_names = []
            tbl_lists, field_names, status_message = com.read_all_table(f_name)
            if status_message == '':
                view.show_table(tbl_lists)

        case ['3', '4']:
            # Редактировать запись
            f_name = 'db/worklog.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Запрашиваем id записи для редактирования
            edit_id = view.input_id_work()
            filter_dat = {'id_work': edit_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Редактирование данных. Текущие значения:')
            view.show_table(tbl_lists)
            print('Введите новые значения полей:')
            # Выводим значения полей для редактирования
            edit_rec_dat = {'id_work': edit_id,
                            'id_vehicle': view.input_vehicle_id(),
                            'id_personal': view.input_id_personal(),
                            'Description': view.input_work_description(),
                            'Begin_date': view.input_work_begin_date(),
                            'end_date': view.input_work_end_date(),
                            'Price': view.input_work_price(),
                            'id_status': view.input_id_status()}
            # Обновляем данные в БД
            status, mes1 = com.update_rec_table(f_name, edit_rec_dat, 'id_work')
            if status:
                print(f'Редактирование учетной записи выполнено успешно.')
                # Выводим таблицу данных после редактирования записи
                tbl_lists, field_names, status_message = com.read_all_table(f_name)
                if status_message == '':
                    view.show_table(tbl_lists)
                else:
                    print(mes1)
            else:
                print('соответствующая запись не найдена.')

        case ['3', '5']:
            # Удалить запись
            f_name = 'db/worklog.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            delrec_id = view.input_id_work()
            filter_dat = {'id_work': delrec_id}
            status, tbl_lists = com.delete_rec_table(f_name, filter_dat)
            if status and tbl_lists != []:
                view.show_table(tbl_lists)
                print(f'Запись с id = {delrec_id} успешно удалена в таблице.')
            else:
                print('соответствующие записи не найдены.')

        # ['4', '1'] - ['4', '5'] - Персонал
        case ['4', '1']:
            f_name = 'db/personal.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Создать запись
            new_rec_dat = {'first_name': view.input_pers_first_name(),
                           'family_name': view.input_pers_family_name(),
                           'middle_name': view.input_pers_middle_name(),
                           'birth_date': view.input_pers_birth_date(),
                           'phones': view.input_pers_phones(),
                           'position': view.input_pers_position()}
            field_names = ['id_personal', 'first_name', 'family_name', 'middle_name',
                           'birth_date', 'phones', 'position']
            id_name = 'id_personal'
            status, new_id = com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            if status:
                # После добавления записи выводим полный список
                tbl_lists, field_names, status_message = com.read_all_table(f_name)
                view.show_table(tbl_lists)
                print(f'Запись с id = {new_id} успешно создана в таблице.')
            else:
                print(f'Ошибка при создании новой записи в таблице.')

        case ['4', '2']:
            # Найти запись
            f_name = 'db/personal.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            find_id = view.input_pers_id()
            filter_dat = {'id_personal': find_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Найденные записи:')
                view.show_table(tbl_lists)
            else:
                print('соотвествующие записи не найдены.')

        case ['4', '3']:
            # Вывести все записи
            f_name = 'db/clients.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            divider = ' '
            show_field_names = []
            tbl_lists, field_names, status_message = com.read_all_table(f_name)
            if status_message == '':
                view.show_table(tbl_lists)

        case ['4', '4']:
            # Редактировать запись
            f_name = 'db/personal.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # Запрашиваем id записи для редактирования
            edit_id = view.input_pers_id()
            filter_dat = {'id_personal': edit_id}
            status, tbl_lists = com.find_recs_in_table(f_name, filter_dat)
            if status and tbl_lists != []:
                print('Редактирование данных. Текущие значения:')
                view.show_table(tbl_lists)
                print('Введите новые значения полей:')
                # Выводим значения полей для редактирования
                edit_rec_dat = {'id_personal': edit_id,
                                'first_name': view.input_pers_first_name(),
                                'family_name': view.input_pers_family_name(),
                                'middle_name': view.input_pers_middle_name(),
                                'birth_date': view.input_pers_birth_date(),
                                'phones': view.input_pers_phones(),
                                'position': view.input_pers_position()}
                # Обновляем данные в БД
                status, mes1 = com.update_rec_table(f_name, edit_rec_dat, 'id_personal')
                if status:
                    print(f'Редактирование учетной записи выполнено успешно.')
                    # Выводим таблицу данных после редактирования записи
                    tbl_lists, field_names, status_message = com.read_all_table(f_name)
                    if status_message == '':
                        view.show_table(tbl_lists)
                else:
                    print(mes1)
            else:
                print('соответствующая запись не найдена.')

        case ['4', '5']:
            # Удалить запись
            f_name = 'db/personal.csv'
            # удаляем последний элемент из списка. для возврата к предыдущему меню
            cur_menu_pos.pop()
            # запрашиваем у пользователя id искомой учетной записи
            delrec_id = view.input_pers_id()
            filter_dat = {'id_personal': delrec_id}
            status, tbl_lists = com.delete_rec_table(f_name, filter_dat)
            if status and tbl_lists != []:
                view.show_table(tbl_lists)
                print(f'Запись с id = {delrec_id} успешно удалена в таблице.')
            else:
                print('соотвествующие записи не найдены.')

        case _:
            print('Введите целое число, выберите значение из списка.')



            # def perform_data():
            #  check.data_check(y, m, d)

            # def perform_reg(reg_num):
            #   check.reg_num_check(reg_num)

            # def perform_phone():
            #  check.phone_check(num)