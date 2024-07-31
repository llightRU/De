import re
from datetime import datetime, date
from PyQt5.QtWidgets import QMessageBox


def check_file_open(filename):
    try:
        file = open(filename)
        file.close()
        return True
    except:
        return False


def valid_sex(sex):
    try:
        sex = str(sex)
        sex = sex.lower()
        if sex != 'male':
            if sex != 'female':
                return False
        return True
    except:
        return False


def get_date(date1):
    try:
        date1 = re.findall('\d+', date1)
        if len(date1) != 3:
            return False
        date1 = [int(x) for x in date1]
        print(date1)
        date1 = date(date1[0], date1[1], date1[2])
        return date1
    except:
        print('Error')
        return False


def check_date(date):
    try:
        if date.year <= 1990 or date.year >= datetime.today().year:
            return False
        return True
    except:
        return False


def check_id_card(card):
    try:
        int(card)
        if len(card) != 12 or len(card) != 9:
            return True
        return False
    except:
        return False


def check_string(country):
    if len(country) >= 255 or len(country) == 0:
        return False
    if re.match('^\s+$', country):
        return False
    if re.search('\d', country):
        return False
    return True

def check_search_name(txt):
    if len(txt) >= 255:
        return False
    if re.search('\d', txt):
        return False
    return True

def check_pass(pass_w):
    if len(pass_w) >= 255 or len(pass_w) == 0:
        return False
    if re.match('^\s+$', pass_w):
        return False
    return True
def valid_famer_info(win, values):
    if not check_string(values[0]):
        QMessageBox.information(win, 'Error', 'Name is not valid', QMessageBox.Close)
        return False
    if not check_id_card(values[1]):
        QMessageBox.information(win, 'Error', 'Id_card is not valid', QMessageBox.Close)
        return False
    if not check_date(values[2]):
        QMessageBox.information(win, 'Error', 'Id_card is not valid', QMessageBox.Close)
        return False
    if not check_string(values[3]):
        QMessageBox.information(win, 'Error', 'Country is not valid', QMessageBox.Close)
        return False
    return True


def check_id(id):
    try:
        id = int(id)
        if id < 1:
            return False
        return True
    except:
        return False


def check_health(unit):
    try:
        unit = float(unit)
        if unit <= 0 or unit >= 200:
            return False
        return True
    except Exception as err:
        print(str(err.args[0]))
        return False


if __name__ == '__main__':
    print(get_date('2001-01-01'))
