import view
#import model_csv as cs

import model_common as com
#import check
#import read_write as rw
import test_model_view as tmv
#import view_tests as vt

def split_list(p):
    g = []
    for i in p:
      g.append(i.split())
    return g


view.show_greetings()
while True:
  ch=int(view.show_category_menu())
 
  match ch:

    case 1:
        hc=int(view.show_action_menu())
        f_name = 'db/vehicles.csv'
        match hc:
            case 1:
                new_rec_dat = {'ModelMark': view.input_vehicle_model(), 'Manufact_date': view.input_repairs_start(), 'Reg_num': view.input_gov_number(),
                               'id_client': '3'}
                field_names = ['id_vehicle', 'ModelMark', 'Manufact_date', 'Reg_num', 'id_client']
                id_name = 'id_vehicle'
                com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            case 2:
                a=12

            case 3:
                divider = ' '
                show_field_names = []
                #p - список словарей (строк таблицы данных в файле csv
                tbl_dict, field_names, status_message = com.read_all_table(f_name)
                #p = tmv.view_all(f_name, show_field_names, divider)
                #table = split_list(p)
                # print(table)
                if status_message == '':
                    #преобразуем список словарей в список списков, чтобы далее показать таблицу
                    tbl_list = view.convert_listofdicts_to_listoflists(tbl_dict)
                    view.show_table(tbl_list)
            case 4:
                a=12
            case 5:
                view.show_success()
            case _:
                print('Error')          

    case 2:
        hc=int(view.show_action_menu())
        f_name = 'db/clients.csv'
        match hc:
            case 1:

                p=view.input_client_fio()
                k = p.split()
                #k=split_list(p)
                new_rec_dat={'first_name':k[0],'family_name':k[1],'middle_name':k[2],'birth_date':'20.03.2002','phones':'79652364589'}
                field_names = ['id_client','first_name','family_name','middle_name','birth_date','phones']
                id_name = 'id_client'
                com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            case 2:
                a=12

            case 3:


                divider = ' '
                show_field_names = []
                p = tmv.view_all(f_name, show_field_names, divider)
                table = split_list(p)
                view.show_table(table)
            case 4:
                a=12
            case 5:
                view.show_success()
            case _:
                print('Error')

    case 3:
        hc=int(view.show_action_menu())
        f_name = 'db/worklog.csv'
        match hc:

            case 1:

                new_rec_dat = {'id_vehicle':'2','id_personal':'2','Description':'замена_всех_стоек','Begin_date':view.input_repairs_start(),
                               'end_date':view.input_repairs_end(),'Price':'1000','id_status':'1'}
                field_names = ['id_work','id_vehicle','id_personal','Description','Begin_date','end_date','Price','id_status']
                id_name = 'id_work'
                com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            case 2:
                a=12

            case 3:

                divider = ' '
                show_field_names = []
                p = tmv.view_all(f_name, show_field_names, divider)
                table = split_list(p)
                view.show_table(table)
            case 4:
                a=12
            case 5:
                view.show_success()
            case _:
                print('Error')

    case 4:
        hc=int(view.show_action_menu())
        f_name = 'db/personal.csv'
        match hc:
            case 1:
                p = view.input_technician_fio()
                k = split_list(p)
                new_rec_dat = {'first_name':k[0],'family_name':k[1],'middle_name':k[2],'birth_date':'12.03.1987',
                               'phones':'79524563678','position':'мастер'}
                field_names = ['id_personal','first_name','family_name','middle_name','birth_date','phones','position']
                id_name = 'id_personal'
                com.create_rec_table(f_name, new_rec_dat, field_names, id_name)
            case 2:
                a=12

            case 3:

                divider = ' '
                show_field_names = []
                p = tmv.view_all(f_name, show_field_names, divider)
                table = split_list(p)
                view.show_table(table)
            case 4:
                a=12
            case 5:
                view.show_success()
            case _:
                print('Error')
    case 5:
      view.show_goodbye()
      break
    case _:
        print('Error')


#def perform_data():
#  check.data_check(y, m, d)

#def perform_reg(reg_num):
#   check.reg_num_check(reg_num)

#def perform_phone():
#  check.phone_check(num)




