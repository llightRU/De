import os
import json
import datetime
from datetime import datetime as dt
from os import path
import mysql.connector
from mysql.connector import errorcode
import re
import pandas as pd
import validate as v
import common as cm

FILE_JSON_PATH = './database_config.json'


def check_file_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False


def read_json_file(path):
    dict_list = dict()
    if check_file_exist(path):
        with open(path, encoding='utf-8', errors='None') as f:
            dict_list = json.load(f)
    return dict_list


def connect_sql(config):
    try:
        cnx = mysql.connector.connect(user=config['user'], password=config['password'],
                                      host=config['host'])
        return cnx
    except mysql.connector.errorcode as err:
        print(err)
        return False


def connect_database(cnx, config):
    cursor = cnx.cursor()
    db = config['database']
    try:
        cursor.execute('USE {}'.format(db))
    except mysql.connector.Error as err:
        print('Database {} does not exists.'.format(db))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, db)
            print("Database {} create successfully.".format(db))
            cnx.database = db
        else:
            print(err)
            exit(1)


def create_database(cur, db_name):
    try:
        cur.execute("CREATE DATABASE {}".format(db_name))
    except mysql.connector.Error as err1:
        print("Failed creating database: {}".format(err1))
        exit(1)


def create_table(cur, name, info):
    try:
        print("Creating table {} ".format(name))
        cur.execute(info)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table is already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def update_data_by_id(cnx, table, label, value, id):
    try:
        sql = "UPDATE {} SET {} = '{}'".format(table, label[0], value[0])
        s_label = ''
        for i in range(1, len(label)):
            s_label += ", {} = '{}'".format(label[i], value[i])
        sql = sql + s_label + ' WHERE id = {}'.format(id)
        print(sql)
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def get_from_id(cursor, table_name, id):
    try:
        id = int(id)
        cursor.execute('select * from {} where id = {}'.format(table_name, id))
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0


def delete_from_id(cnx, table_name, id):
    try:
        cursor = cnx.cursor()
        cursor.execute('delete from {} where id = {}'.format(table_name, id))
        cnx.commit()
        return 1
    except mysql.connector.Error as err:
        print(err)
        return 0


def insert_to_table(cnx, table, labels, values):
    try:
        sql = 'INSERT INTO {} '.format(table)
        s_label = '(' + labels[0]
        s = '(' + '%s'
        for i in range(1, len(labels)):
            s_label += ',' + labels[i]
            s += ',%s'
        s_label += ')'
        s += ')'
        sql += s_label + ' VALUES ' + s
        print(sql)
        cursor = cnx.cursor()
        cursor.execute(sql, values)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def show_table(cursor, table):
    try:
        cursor.execute('select * from {}'.format(table))
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def search_name(cursor, table, name):
    try:
        cursor.execute('select * from {} where hos_name like \'%{}%\''.format(table, name))
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def search_address(cursor, table, address):
    try:
        cursor.execute('select * from {} where address like \'%{}%\''.format(table, address))
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def check_foreign_id(cursor, table_foreign, id):
    try:
        cursor.execute('select id from {}'.format(table_foreign))
        results = cursor.fetchall()
        id = int(id)
        for result in results:
            if id in result:
                return True
        return False
    except mysql.connector.Error as err:
        print(err)
    except:
        print('ID must be number: {}'.format(id))
    return False


def check_name(cursor, table, name):
    try:
        cursor.execute('select * from {} where name = \'{}\''.format(table, name))
        results = cursor.fetchone()
        return results
    except mysql.connector.Error as err:
        print(err)
        return False


def update_farmer(cnx, values):
    try:
        cursor = cnx.cursor()
        print(values)
        sql = 'update farmer set ' \
              'user_name = %s, ' \
              'id_card = %s,' \
              'dob = %s, ' \
              'country = %s,' \
              'sex = %s' \
              ' where id = %s'
        val = (values[0], values[1], values[2], values[3], values[4], values[5])
        cursor.execute(sql, val)
        cnx.commit()
    except mysql.connector.Error as err:
        print(err)
        return False


def check_health_from_farmerId(cursor, id):
    try:
        id = str(id)
        sql = 'select * from check_health where farmer_id = {}'.format(id)
        cursor.execute(sql)
        return cursor.fetchone()
    except mysql.connector.Error as err:
        print(err)
        return False


def get_account_by_id(cursor, id):
    try:
        id = int(id)
        cursor.execute('select * from account where acc_id = {}'.format(id))
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0


def update_password(cnx, password, id):
    try:
        cursor = cnx.cursor()
        sql = 'update account set password = %s where acc_id = %s'
        args = (password, id)
        cursor.execute(sql, args)
        cnx.commit()
        return 1
    except mysql.connector.Error as err:
        print(err)
        return 0


def get_farmer_by_id(cursor, id):
    try:
        id = int(id)
        sql = 'select * from farmer where id = %s'
        args = (id,)
        cursor.execute(sql,args)
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def get_farmer_by_acc_id(cursor, id):
    try:
        id = int(id)
        sql = 'select * from farmer where acc_id = %s'
        args = (id,)
        cursor.execute(sql,args)
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def get_farmer_id_by_name(cursor,name):
    try:
        cursor.execute('select acc_id from farmer where user_name like \'%{}%\''.format(name))
        x = cursor.fetchall()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def get_accId_from_farmer_id(cursor,id):
    try:
        cursor.execute('select acc_id from farmer where id = {}'.format(id))
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def delete_account_from_id(cnx,id):
    try:
        cursor = cnx.cursor()
        cursor.execute('delete from account where acc_id = {}'.format(id))
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False

def data_to_excel(table,df):
    try:
        if not path.exists('export_excel_file'):
            os.mkdir('export_excel_file')
        filename = str(dt.now())
        filename = re.sub("[-\s:]", '_', filename)
        filename = re.findall("[_\d]+", filename)
        filename = 'export_excel_file\\' + table+'_' +filename[0] + '.xlsx'
        print(filename)
        df.to_excel(filename)
        return True
    except:
        print('Error')
        return False

def update_health(cnx,values):
    try:
        cursor = cnx.cursor()
        sql = 'update check_health set ' \
              'pt_hong_cau = %s, ' \
              'hst = %s, ' \
              'hong_cau = %s, ' \
              'tieu_cau = %s, ' \
              'luong_hst_tb_hc = %s, ' \
              'nd_hst_tb_hc = %s, ' \
              'tt_hc_tb = %s ,' \
              'bach_cau_LEUCOCYTE = %s' \
              'where farmer_id = %s'
        cursor.execute(sql,values[:-1])
        cnx.commit()
        sql = 'update farmer set ' \
              'inpatient = %s ' \
              'where id = %s'
        args = (values[-1],values[-2])
        cursor.execute(sql,args)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False

def get_account_by_id(cursor, id):
    try:
        id = int(id)
        cursor.execute('select * from account where acc_id = {}'.format(id))
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0


def get_account(cursor, account, password):
    try:

        query=('select * from account where account = %s and password = %s')
        args = (account, password)
        cursor.execute(query, args)
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def get_user_name(cursor):
    try:
        query=('select account from account')
        cursor.execute(query)
        x = cursor.fetchall()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def insert_account(cursor, cnx, account, password):
    query = "INSERT INTO account " \
            "(`account`, `password`, `role`) " \
            "VALUES(%s,%s,'1');"
    args = (account, password)
    try:
        cursor.execute(query, args)
        cnx.commit()
        return True
    except Exception as error:
        print(error)
        return False

def get_acc_id_account(cursor, account, password):
    try:
        query=('select acc_id from account where account = %s and password = %s')
        args = (account, password)
        cursor.execute(query, args)
        x = cursor.fetchone()[0]
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def insert_famer(cursor, cnx, user_name, id_card, dob, country, acc_id):
    query = "INSERT INTO farmer " \
            "(`user_name`, `id_card`, `dob`, `country`, `acc_id`) " \
            "VALUES(%s,%s,%s,%s,%s);"
    args = (user_name, id_card, dob, country, acc_id)
    try:
        cursor.execute(query, args)
        cnx.commit()
        return True
    except Exception as error:
        print(error)
        return False
def update_password(cnx, password, id):
    try:
        cursor = cnx.cursor()
        sql = 'update account set password = %s where acc_id = %s'
        args = (password, id)
        cursor.execute(sql, args)
        cnx.commit()
        return 1
    except mysql.connector.Error as err:
        print(err)
        return 0

def get_farmer_by_farmerId(cursor,id):
    try:
        id = int(id)
        cursor.execute('select * from farmer where id = {}'.format(id))
        x = cursor.fetchone()
        return x
    except mysql.connector.Error as err:
        print(err)
        return 0

def insert_check_health(cnx,values):
    try:
        cursor = cnx.cursor()
        sql = "insert into check_health (staff_id,farmer_id,pt_hong_cau, hst, hong_cau, tieu_cau, luong_hst_tb_hc, nd_hst_tb_hc, tt_hc_tb,bach_cau_LEUCOCYTE)" \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,values)
        cnx.commit()
        print('insert successfull')
        return 1
    except mysql.connector.Error as err:
        print(err)
        return 0

if __name__ == "__main__":
    filename = './database_config.json'
    if v.check_file_open(filename):
        with open(filename) as f:
            config = json.load(f)
            f.close()
        try:
            cnx = cm.connect_sql(config)
            cm.connect_database(cnx, config)
        except Exception as err:
            print(str(err.args[0]))

