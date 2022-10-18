import re
from datetime import date


def data_check(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False


def reg_num_check(reg_num):
    s_num = str(reg_num)

    return 10 > len(s_num) > 7 and not re.search('[a-zA-Zйцгшщзфыплджэячьъбю]', s_num) and s_num[:1].isalpha() \
           and s_num[1:4].isdigit() and s_num[4:6].isalpha() and s_num[6:].isdigit()


def phone_check(num):
    s_num = str(num)
    return len(s_num) == 12 and s_num[:2]=='+7' and s_num[1:].isdigit()


print(phone_check('+79221545454'))
