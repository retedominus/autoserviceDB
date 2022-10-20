import csv


def read_db(f_name):
    res = []
    with open(f_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            res.append(row)
        return res


def write_db(f_name, dat):
    if dat:
        with open(f_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)


data = [['id_vehicle',	'ModelMark',	'Manufact_date',	'Reg_num',	'id_client'],
        ['4', 'Kia', '19.04.2000', 'Р734РК77', '4'],
        ['1',	'Toyota Corolla',	'01.10.2008',	'А436КТ163',	'1'],
        ['2',	'Nissan Pathfinder',	'12.12.2015',	'М451ОВ78',	'2'],
        ['3',	'LADA Priora',	'20.05.2020',	'Л542ПР99',	'3']]

# write_db('db/vehicles.csv', data)
print(read_db('db/vehicles.csv'))
