import re
from datetime import date


def data_change(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False


def reg_num_change(reg_num):
    s_num = str(reg_num)

    return 10 > len(s_num) > 7 and not re.search('[a-zA-Zйцгшщзфыплджэячьъбю]', s_num) and s_num[:1].isalpha()\
           and s_num[1:4].isdigit() and s_num[4:6].isalpha() and s_num[6:].isdigit()

