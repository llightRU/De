import os
from datetime import datetime
import datetime

import openpyxl
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QCheckBox, QMessageBox, QWidget
import sys
import Examination_Screen
import common as cm
import mysql.connector
import Chat_Screen
# mở file excel
import subprocess

# màn hình tạo mới một báo cáo
class Add_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Add New Screen")
        self.resize(350, 200)
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.yes_button = QtWidgets.QPushButton(self)
        self.yes_button.setGeometry(QtCore.QRect(120, 140, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yes_button.setFont(font)
        self.yes_button.setObjectName("yes_button")
        self.text_content = QtWidgets.QLineEdit(self)
        self.text_content.setGeometry(QtCore.QRect(20, 50, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_content.setFont(font)
        self.text_content.setText("")
        # self.text_content.setReadOnly(True)
        self.text_content.setObjectName("text_content")

        # render UI
        self.retranslateUi()

        # nút tạo mới
        self.yes_button.clicked.connect(self.create_new_report)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Delete_Screen", "Delete Screen"))
        self.yes_button.setText(_translate("Delete_Screen", "Tạo mới"))

    def display_screen(self):
        self.show()

    def close_screen(self):
        self.close()

    def create_new_report(self):

        # ẩn form đăng kí
        self.hide()

        try:

            report_name = self.text_content.text().strip()

            # nếu report name trống thì warning
            if not report_name:

                error_dialog = QMessageBox(QMessageBox.Critical, "Field Error",
                'Tên báo cáo không được để trống', QMessageBox.Close)
                error_dialog.setStyleSheet("width: 300px")
                error_dialog.exec()

            else:

                # tạo các trường để lưu vào db
                name = report_name
                status =0
                path = './export_excel_file/'+name.casefold().strip().replace(" ","_")+'.xlsx'
                today = datetime.date.today()
                report_date = f'{today.year}/{today.month}/{today.day}'

                # mở file excel với các header cho trước
                # tạo các header
                columnHeaders = ['encounter_id,patient_id,hospital_id,age,bmi,elective_surgery,ethnicity,gender,height,' \
                'icu_admit_source,icu_id,icu_stay_type,icu_type,pre_icu_los_days,weight,apache_2_diagnosis,' \
                'apache_3j_diagnosis,apache_post_operative,arf_apache,gcs_eyes_apache,gcs_motor_apache,' \
                'gcs_unable_apache,gcs_verbal_apache,heart_rate_apache,intubated_apache,map_apache,' \
                'resprate_apache,temp_apache,ventilated_apache,d1_diasbp_max,d1_diasbp_min,' \
                'd1_diasbp_noninvasive_max,d1_diasbp_noninvasive_min,d1_heartrate_max,' \
                'd1_heartrate_min,d1_mbp_max,d1_mbp_min,d1_mbp_noninvasive_max,d1_mbp_noninvasive_min,' \
                'd1_resprate_max,d1_resprate_min,d1_spo2_max,d1_spo2_min,d1_sysbp_max,' \
                'd1_sysbp_min,d1_sysbp_noninvasive_max,d1_sysbp_noninvasive_min,d1_temp_max,' \
                'd1_temp_min,h1_diasbp_max,h1_diasbp_min,h1_diasbp_noninvasive_max,' \
                'h1_diasbp_noninvasive_min,h1_heartrate_max,h1_heartrate_min,h1_mbp_max,h1_mbp_min,' \
                'h1_mbp_noninvasive_max,h1_mbp_noninvasive_min,h1_resprate_max,h1_resprate_min,' \
                'h1_spo2_max,h1_spo2_min,h1_sysbp_max,h1_sysbp_min,h1_sysbp_noninvasive_max,' \
                'h1_sysbp_noninvasive_min,d1_glucose_max,d1_glucose_min,d1_potassium_max,' \
                'd1_potassium_min,apache_4a_hospital_death_prob,apache_4a_icu_death_prob,' \
                'aids,cirrhosis,diabetes_mellitus,hepatic_failure,immunosuppression,leukemia,' \
                'lymphoma,solid_tumor_with_metastasis,apache_3j_bodysystem,apache_2_bodysystem,hospital_death']

                df = pd.DataFrame(columns=columnHeaders)

                # tạo đường dẫn
                dirname = "export_excel_file"
                if os.path.isdir('./export_excel_file'):

                    df.to_excel(path,index=False)

                else:

                    os.mkdir(dirname)
                    df.to_excel(path,index=False)
                print('Excel file exported')

                # mở file excel với các trường đã nhập
                # đường dẫn tới file excel
                excel_path = 'C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE'
                # đường dẫn tới file cần mở
                file_path = str(path)
                subprocess.call([excel_path, file_path])

                # tạo 1 list data chứa các trường để lưu vào db
                list_data = [name,status,path,1,1,report_date]
                database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
                cnx = mysql.connector.connect(**database_config_setup)
                cursor = cnx.cursor()
                stm = 'INSERT INTO report (report_name,status,report_path,staff_id,goverment_id,report_date) VALUES (%s,%s,%s,%s,%s,%s)'
                cursor.execute(stm,list_data)
                cnx.commit()
                cnx.close()
                print('insert report success')
        except Exception as e:
            print(e)

class Ui_Staff(QMainWindow):

    def __init__(self,parent=None):
        super(Ui_Staff,self).__init__(parent)
    def setupUi(self):
        self.setObjectName("Staff")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 90, 561, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)

        # set từng dòng header trong table
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(77)
        item = QtWidgets.QTableWidgetItem()
        item.setText(' ')
        self.tableWidget.setHorizontalHeaderItem(6, item)

        # tạo -> đặt checkbox ở hàng cuối
        self.checkbox_all = QtWidgets.QCheckBox('All',self)
        self.checkbox_all.setGeometry(QtCore.QRect(550,100,41, 20))

        self.add_new_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_button.setGeometry(QtCore.QRect(540, 50, 71, 31))
        self.add_new_button.setObjectName("add_new_button")
        self.chat_button = QtWidgets.QPushButton(self.centralwidget)
        self.chat_button.setGeometry(QtCore.QRect(650, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chat_button.setFont(font)
        self.chat_button.setObjectName("chat_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(413, 50, 81, 31))
        self.search_button.setObjectName("search_button")
        self.hand_out_button = QtWidgets.QPushButton(self.centralwidget)
        self.hand_out_button.setGeometry(QtCore.QRect(620, 90, 61, 28))
        self.hand_out_button.setObjectName("hand_out_button")
        self.search_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.search_txt.setGeometry(QtCore.QRect(170, 50, 241, 29))
        self.search_txt.setObjectName("search_txt")
        self.check_health_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_health_button.setGeometry(QtCore.QRect(650, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.check_health_button.setFont(font)
        self.check_health_button.setObjectName("check_health_button")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # render UI
        self.retranslateUi()

        # xử lí các button
        self.check_health_button.clicked.connect(self.open_examination_screen)
        self.chat_button.clicked.connect(self.open_chat_screen)
        self.search_button.clicked.connect(self.search_report)
        self.hand_out_button.clicked.connect(self.hand_out_report)
        self.add_new_button.clicked.connect(self.add_new_report)

        # xử lí checkbox chọn tất cả
        self.checkbox_all.stateChanged.connect(self.handel_checkbox)
        self.check_health_button.hide()
        # get db result list
        self.data_list = self.db_get_data_list()

        # binding data to table
        self.init_data(self.data_list)

    def db_get_data_list(self):
        self.database_config_setup=cm.read_json_file(cm.FILE_JSON_PATH)
        self.cnx=mysql.connector.connect(**self.database_config_setup)
        self.cursor=self.cnx.cursor()
        self.cursor.execute('select id, report_date, report_name, status from report')
        data_rs = self.cursor.fetchall()
        self.cnx.commit()
        self.cnx.close()
        return data_rs

    def init_data(self, data_list):

        try:
            self.checkbox_table = QCheckBox('Chọn')
            print(data_list)

            for i in range(0, len(data_list)):

                # binding data theo row i
                self.tableWidget.insertRow(i)
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data_list[i][0])))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data_list[i][1])))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data_list[i][2])))
                if data_list[i][3] == '0':
                    self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem('Chưa nộp'))
                else:
                    self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem('Đã nộp'))
                # tạo nut edit và xóa
                button_edit = QPushButton('Edit', self.tableWidget)
                button_delete = QPushButton('Delete', self.tableWidget)
                self.tableWidget.setCellWidget(i, 4, button_edit)
                self.tableWidget.setCellWidget(i, 5, button_delete)

                # tạo checkbox
                checkbox_table = QCheckBox('Chọn')
                self.tableWidget.setCellWidget(i,6,checkbox_table)

                index_edit = QtCore.QPersistentModelIndex(self.tableWidget.model().index(i, 4))
                index_delete = QtCore.QPersistentModelIndex(self.tableWidget.model().index(i, 5))
                index_checkbox = QtCore.QPersistentModelIndex(self.tableWidget.model().index(1,6))

                # nhấn sửa và xóa
                button_edit.clicked.connect(
                    lambda *arg, index=index_edit: self.handle_button_edit(index)
                )
                button_delete.clicked.connect(
                    lambda *arg, index=index_delete: self.handle_button_delete(index)
                )

        except Exception as e:
            print(e)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Staff", "Staff Screen"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Staff", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Staff", "Ngày"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Staff", "Tên BC"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Staff", "Trạng thái"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Staff", "Chỉnh sửa"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Staff", "Xóa"))
        self.add_new_button.setText(_translate("Staff", "Tạo mới"))
        self.chat_button.setText(_translate("Staff", "CHAT"))
        self.search_button.setText(_translate("Staff", "Tìm kiếm"))
        self.hand_out_button.setText(_translate("Staff", "Nộp"))
        self.check_health_button.setText(_translate("Staff", "KHÁM"))

    # mở màn hình Khám
    def open_examination_screen(self):
        self.examination_screen = Examination_Screen.Ui_Examination()
        self.examination_screen.setupUi()
        self.examination_screen.show()

    # mở màn hình chat
    def open_chat_screen(self):
        try:
            self.chat_screen = Chat_Screen.Messenger()
            self.chat_screen.initUI()
            self.chat_screen.show()
        except Exception as e:
            print(e)

    # hàm checkbox chọn tất cả:
    def handel_checkbox(self):
        try:
            for row in range(self.tableWidget.rowCount()):
                checkbox = self.tableWidget.cellWidget(row, 6)
                checkbox.setChecked(True)
        except Exception as e:
            print(e)

    # tìm kiếm
    def search_report(self):
        try:
            search_name = self.search_txt.text().strip()
            self.database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            self.cnx = mysql.connector.connect(**self.database_config_setup)
            self.cursor = self.cnx.cursor()
            query = '%{}%'.format(search_name)
            self.cursor.execute('select id, report_date,report_name,status from report where report_name like %s',(query,))
            data_rs = self.cursor.fetchall()
            self.cnx.commit()
            self.cnx.close()
            if not data_rs:
                error_dialog = QMessageBox(QMessageBox.Critical, "Field Error", 'Không có tên báo cáo: {}'.format(search_name), QMessageBox.Close)
                error_dialog.setStyleSheet("width: 300px")
                error_dialog.exec()
            else:
                self.tableWidget.setRowCount(0)
                self.init_data(data_rs)
        except Exception as e:
            print(e)

    # nút chỉnh sửa
    def handle_button_edit(self,index):

        # lấy index
        try:

            # print(index.row(),index.column())
            # B1: lấy path
            table_model = self.tableWidget.model()
            id_index = table_model.index(index.row(),0)

            # lấy data
            get_id = table_model.data(id_index)
            get_id = [get_id]

            #gọi database để lấy path
            self.database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            self.cnx = mysql.connector.connect(**self.database_config_setup)
            self.cursor = self.cnx.cursor()
            self.cursor.execute('select report_path from report where id like %s', get_id)

            # lấy path
            path = self.cursor.fetchone()
            self.cnx.commit()
            self.cnx.close()
            self.open_excel_by_path(path)

        except Exception as e:
            print(e)

    def open_excel_by_path(self,path):

        # đường dẫn tới file excel
        excel_path = 'C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE'
        # đường dẫn tới file cần mở
        # file_path='./export_excel_file/test.xlsx'
        file_path = str(path[0])
        # print(file_path)
        subprocess.call([excel_path, file_path])

    # nút nộp
    def hand_out_report(self):

        try:

            list_id=[]
            for row in range(self.tableWidget.rowCount()):

                # truy cập đến ô tại hàng i cột 6
                cell_widget = self.tableWidget.cellWidget(row, 6)

                # Kiểm tra xem ô đó có phải là QCheckBox hay không
                if isinstance(cell_widget, QCheckBox):
                    # Lấy giá trị của checkbox
                    checkbox_value = cell_widget.checkState()
                    # Kiểm tra giá trị của checkbox và xử lý tương ứng
                    if checkbox_value == Qt.Checked:
                        # truy cập đến ô tại hàng row, cột 1
                        item = self.tableWidget.item(row, 0)
                        # lấy giá trị của ô đó
                        id_value = item.text()
                        list_id.append(id_value)

            #B2: update bảng report theo report_id thành status = 1
            # db_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            # cnx = mysql.connector.connect(**db_setup)
            # cursor = cnx.cursor()
            data_update = list_id
            for i in range(len(data_update)):
                db_setup = cm.read_json_file(cm.FILE_JSON_PATH)
                cnx = mysql.connector.connect(**db_setup)
                cursor = cnx.cursor()
                data_update = list_id
                id = int(data_update[i])
                update_stm = "UPDATE report SET status = 1 WHERE id = %s;"
                cursor.execute(update_stm, [id,])
                cnx.commit()
                cnx.close()
            print('update success')
            #B3: hiển thị lại table
            self.tableWidget.setRowCount(0)
            data_list = self.db_get_data_list()
            self.init_data(data_list)

        except Exception as e:
            print(e)

    # tạo mới report
    def add_new_report(self):

        # mở màn hình để nhập tên báo cáo
        self.add_new_screen = Add_Window()
        self.add_new_screen.display_screen()


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  # manages the GUI application’s control flow and main settings, It handles widget specific initialization, finalization,It initializes the application with the user’s desktop settings
    ui = Ui_Staff()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

