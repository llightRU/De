import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QPushButton, QMessageBox
import sys
import mysql.connector
import common as cm
import os
import shutil
from QtDesigner import Chat
import Machine
import Dead_Heart


class Ui_Goverment(QMainWindow):


    def __init__(self,parent=None):
        super(Ui_Goverment,self).__init__(parent)


    def setupUi(self):
        self.setObjectName("Goverment")
        self.resize(800, 565)
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 80, 571, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small Semilig")
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoScrollMargin(15)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)

        # thêm table chat
        self.table_chat = QtWidgets.QTableWidget(self.centralwidget)
        self.table_chat.setGeometry(QtCore.QRect(50, 80, 571, 431))
        self.table_chat.setObjectName("table_chat")
        self.table_chat.setColumnCount(5)
        self.table_chat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(4, item)
        self.table_chat.horizontalHeader().setDefaultSectionSize(108)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.choose_many_button = QtWidgets.QPushButton(self.centralwidget)
        self.choose_many_button.setGeometry(QtCore.QRect(50, 50, 81, 28))
        self.choose_many_button.setObjectName("choose_many_button")
        self.delete_many_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_many_button.setGeometry(QtCore.QRect(620, 440, 81, 28))
        self.delete_many_button.setObjectName("delete_many_button")
        self.get_many_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_many_button.setGeometry(QtCore.QRect(620, 480, 81, 28))
        self.get_many_button.setObjectName("get_many_button")
        self.chat_button = QtWidgets.QPushButton(self.centralwidget)
        self.chat_button.setGeometry(QtCore.QRect(642, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chat_button.setFont(font)
        self.chat_button.setObjectName("chat_button")
        self.statistic_button = QtWidgets.QPushButton(self.centralwidget)
        self.statistic_button.setGeometry(QtCore.QRect(642, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statistic_button.setFont(font)
        self.statistic_button.setObjectName("statistic_button")
        self.reload_button = QtWidgets.QPushButton(self.centralwidget)
        self.reload_button.setGeometry(QtCore.QRect(535, 48, 70, 32))
        self.reload_button.setObjectName("reload_button")
        self.seach_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.seach_txt.setGeometry(QtCore.QRect(170, 50, 250, 28))
        self.seach_txt.setMaxLength(32822)
        self.seach_txt.setObjectName("seach_txt")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(420, 50, 71, 27))
        self.search_button.setObjectName("search_button")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # thêm nút import
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(620, 80, 61, 28))
        self.import_button.setObjectName("import_button")

        # thêm widget thống kê
        self.static_widget = QtWidgets.QWidget(self.centralwidget)
        self.static_widget.setGeometry(QtCore.QRect(50, 80, 571, 431))
        self.static_widget.setObjectName("static_widget")
        self.charges_button = QtWidgets.QPushButton(self.static_widget)
        self.charges_button.setGeometry(QtCore.QRect(100, 160, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.charges_button.setFont(font)
        self.charges_button.setObjectName("charges_button")
        self.dead_static_button = QtWidgets.QPushButton(self.static_widget)
        self.dead_static_button.setGeometry(QtCore.QRect(360, 160, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dead_static_button.setFont(font)
        self.dead_static_button.setObjectName("dead_static_button")
        self.label = QtWidgets.QLabel(self.static_widget)
        self.label.setGeometry(QtCore.QRect(170, 20, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # lấy data từ db
        data_list = self.db_get_data_list()
        # biding data vào table
        self.init_data(data_list)

        # render UI
        self.retranslateUi()

        # ẩn table chat và widget thống kê
        self.table_chat.hide()
        self.static_widget.hide()

        # xử lí các button
        self.reload_button.clicked.connect(self.reload_table)
        self.chat_button.clicked.connect(self.open_message_screen)
        self.search_button.clicked.connect(self.seach_hospital)
        self.delete_many_button.clicked.connect(self.delete_many)
        self.choose_many_button.clicked.connect(self.select_all_checkbox)
        self.get_many_button.clicked.connect(self.get_all_report_ischecked)
        self.import_button.clicked.connect(self.import_data_from_file)
        self.statistic_button.clicked.connect(self.open_static_widget)


    def db_get_data_list(self):

        self.database_config_setup=cm.read_json_file(cm.FILE_JSON_PATH)
        self.cnx=mysql.connector.connect(**self.database_config_setup)
        self.cursor=self.cnx.cursor()
        self.cursor.execute('select code_kcb, hos_name, address, district from hospital')
        data_rs = self.cursor.fetchall()
        self.cnx.commit()
        self.cnx.close()
        return data_rs


    def init_data(self, data_list):

        try:

            self.checkbox_table = QCheckBox('Chọn')

            for i in range(0, len(data_list)):

                # binding data theo row i
                self.tableWidget.insertRow(i)
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data_list[i][0])))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data_list[i][1])))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data_list[i][2])))
                self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(data_list[i][3])))
                # tạo nut edit và xóa
                button_get = QPushButton('Lấy', self.tableWidget)
                button_delete = QPushButton('Xóa', self.tableWidget)
                self.tableWidget.setCellWidget(i, 5, button_get)
                self.tableWidget.setCellWidget(i, 6, button_delete)

                # tạo checkbox
                checkbox_table = QCheckBox('Chọn')
                self.tableWidget.setCellWidget(i,0,checkbox_table)

                index_edit = QtCore.QPersistentModelIndex(self.tableWidget.model().index(i, 5))
                index_delete = QtCore.QPersistentModelIndex(self.tableWidget.model().index(i, 6))
                index_checkbox = QtCore.QPersistentModelIndex(self.tableWidget.model().index(i,0))

                # nhấn lấy và xóa
                button_get.clicked.connect(
                    lambda *arg, index=index_edit: self.handle_button_get(index)
                )
                button_delete.clicked.connect(
                    lambda *arg, index=index_delete: self.handle_button_delete(index)
                )

        except Exception as e:
            print(e)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Goverment", "Goverment Screen"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Goverment", "Chọn"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Goverment", "Mã KCB"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Goverment", "Tên cơ sở"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Goverment", "Địa chỉ"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Goverment", "Tên Quận"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Goverment", "Báo cáo"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Goverment", "Xóa"))
        self.choose_many_button.setText(_translate("Goverment", "Chọn nhiều"))
        self.delete_many_button.setText(_translate("Goverment", "Xóa nhiều"))
        self.get_many_button.setText(_translate("Goverment", "Lấy nhiều"))
        self.chat_button.setText(_translate("Goverment", "Chat Scr"))
        self.statistic_button.setText(_translate("Goverment", "Thống kê"))
        self.reload_button.setText(_translate("Goverment", "Bệnh viện"))
        self.search_button.setText(_translate("Goverment", "Tìm kiếm"))
        # table chat
        item = self.table_chat.horizontalHeaderItem(0)
        item.setText(_translate("Goverment", "Đến Chat"))
        item = self.table_chat.horizontalHeaderItem(1)
        item.setText(_translate("Goverment", "Mã KCB"))
        item = self.table_chat.horizontalHeaderItem(2)
        item.setText(_translate("Goverment", "Tên cơ sở"))
        item = self.table_chat.horizontalHeaderItem(3)
        item.setText(_translate("Goverment", "New Column"))
        item = self.table_chat.horizontalHeaderItem(4)
        item.setText(_translate("Goverment", "Tên Quận"))
        self.import_button.setText(_translate("Goverment", "Import"))

        # widget thống kê item
        self.charges_button.setText(_translate("Goverment", "Chi phí"))
        self.dead_static_button.setText(_translate("Goverment", "Dự đoán"))
        self.label.setText(_translate("Goverment", "Machine Thống Kê"))


    # button chọn nhiều
    def select_all_checkbox(self):

        try:

            for row in range(self.tableWidget.rowCount()):

                checkbox = self.tableWidget.cellWidget(row,0)
                checkbox.setChecked(True)

        except Exception as e:
            print(e)


    # load lại table
    def reload_table(self):

        # ẩn chat và thống kê
        self.table_chat.hide()
        self.static_widget.hide()

        # show button và table hospital
        self.show_all_button()
        self.tableWidget.show()



    # mở màn hình chat
    def open_message_screen(self):

        # hide các button, table hospital và thống kê
        self.tableWidget.hide()
        self.static_widget.hide()
        self.hide_all_button()

        try:

            self.tableWidget.hide()

            self.table_chat.show()
            self.table_chat.setRowCount(0)

            #lấy data
            data_list = self.db_get_data_list()

            #binding vào table
            for i in range(len(data_list)):
                # binding data theo row i
                self.table_chat.insertRow(i)
                self.table_chat.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data_list[i][0])))
                self.table_chat.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data_list[i][1])))
                self.table_chat.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data_list[i][2])))
                self.table_chat.setItem(i, 4, QtWidgets.QTableWidgetItem(str(data_list[i][3])))

                # tạo nút chat
                button_chat = QPushButton('Chat', self.table_chat)
                self.table_chat.setCellWidget(i, 0, button_chat)

                index_chat = QtCore.QPersistentModelIndex(self.table_chat.model().index(i, 0))

                # nhấn lấy và xóa
                button_chat.clicked.connect(
                    lambda *arg, index=index_chat: self.open_chat(index)
                )

        except Exception as e:
            print(e)

        # self.open_message = Chat.Messenger()
        # self.open_message.show()
    def open_chat(self,index):

        try:

            # lấy mã code kcb
            model = self.table_chat.model()
            code_kcb_index = model.index(index.row(),1)
            code_kcb = model.data(code_kcb_index)
            # lấy hospital_id
            database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            cnx = mysql.connector.connect(**database_config_setup)
            cursor = cnx.cursor()
            query = '%{}%'.format(code_kcb)
            cursor.execute('select hos_id from hospital where code_kcb like %s',(query,))
            hos_id = cursor.fetchone()
            hos_id=int(hos_id[0])
            cnx.commit()
            cnx.close()

            # lấy staff id
            database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            cnx = mysql.connector.connect(**database_config_setup)
            cursor = cnx.cursor()
            query = '{}'.format(hos_id)
            cursor.execute('select staff_id from staff where hospital_id = %s', (query,))
            staff_id = cursor.fetchone()
            cnx.commit()
            cnx.close()

            staff_id=staff_id[0]
            # mở message box
            self.open_message = Chat.Messenger(staff_id)
            self.open_message.show()

        except Exception as e:
            print(e)

    # tìm kiếm bệnh viện theo tên
    def seach_hospital(self):

        try:
            search_name = self.seach_txt.text().strip()
            self.database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            self.cnx = mysql.connector.connect(**self.database_config_setup)
            self.cursor = self.cnx.cursor()
            query = '%{}%'.format(search_name)
            self.cursor.execute('select code_kdb, hos_name, address, district from hospital where hos_name like %s',
                                (query,))
            data_rs = self.cursor.fetchall()
            self.cnx.commit()
            self.cnx.close()
            if not data_rs:
                error_dialog = QMessageBox(QMessageBox.Critical, "Field Error",
                                           'Không có tên bệnh viện: {}'.format(search_name), QMessageBox.Close)
                error_dialog.setStyleSheet("width: 300px")
                error_dialog.exec()
            else:
                self.tableWidget.setRowCount(0)
                self.init_data(data_rs)
        except Exception as e:
            print(e)


    # xóa nhiều
    def delete_many(self):

        try:

            # lấy id từ checkbox được chọn
            list_id = []
            for row in range(self.tableWidget.rowCount()):

                # truy cập đến ô tại hàng i cột 1
                cell_widget = self.tableWidget.cellWidget(row, 0)

                # Kiểm tra xem ô đó có phải là QCheckBox hay không
                if isinstance(cell_widget, QCheckBox):
                    # Lấy giá trị của checkbox
                    checkbox_value = cell_widget.checkState()

                    # Kiểm tra giá trị của checkbox và xử lý tương ứng
                    if checkbox_value == Qt.Checked:

                        # truy cập đến ô tại hàng row, cột 2
                        item = self.tableWidget.item(row, 1)
                        # lấy giá trị của ô đó
                        id_value = item.text()
                        list_id.append(id_value)

            # B2: update bảng report theo report_id thành status = 1
            data_delete = list_id

            for i in range(len(data_delete)):

                db_setup = cm.read_json_file(cm.FILE_JSON_PATH)
                cnx = mysql.connector.connect(**db_setup)
                cursor = cnx.cursor()
                data_update = list_id
                id = str(data_update[i])
                update_stm = "Delete From hospital WHERE code_kdb = %s;"
                cursor.execute(update_stm, [id, ])
                cnx.commit()
                cnx.close()

            print('update success')
            # B3: hiển thị lại table
            self.tableWidget.setRowCount(0)
            data_list = self.db_get_data_list()
            self.init_data(data_list)

        except Exception as e:
            print(e)

    def handle_button_get(self,index):

        try:

            # các bước: lấy mã kcb -> hospital id -> lấy report id và path
            table_model = self.tableWidget.model()
            kcb_index = table_model.index(index.row(),1)

            #lấy mã kcb
            get_kcb = table_model.data(kcb_index)
            get_kcb = [get_kcb]

            # gọi database để lấy hospital id
            database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            cnx = mysql.connector.connect(**database_config_setup)
            cursor = cnx.cursor()
            cursor.execute('select hos_id from hospital where code_kcb = %s', get_kcb)
            hos_id = cursor.fetchone()
            cnx.commit()
            cnx.close()

            # gọi database để lấy path
            database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
            cnx = mysql.connector.connect(**database_config_setup)
            cursor = cnx.cursor()
            cursor.execute('select report_path,report_name from report where hospital_id = %s', hos_id)
            data = cursor.fetchone()
            cnx.commit()
            cnx.close()
            print(data)

            # lưu file lấy vào folder get_report
            # Đường dẫn đến thư mục nguồn chứa file Excel
            src_dir = './export_excel_file'

            # Đường dẫn đến thư mục đích để lưu file Excel đã sao chép
            dst_dir = './get_report'

            # Tên file Excel mà bạn muốn sao chép
            excel_file = data[0]

            # Đường dẫn đến file Excel trong thư mục nguồn
            src_file = f'{src_dir}/{excel_file}'

            # Đường dẫn đến file Excel trong thư mục đích
            dst_file = f'{dst_dir}/{excel_file}'

            # Sử dụng hàm shutil.copy để sao chép file từ đường dẫn nguồn đến đường dẫn đích
            shutil.copy(src_file, dst_file)

        except Exception as e:
            print(e)

    def get_all_report_ischecked(self):

        try:

            # lấy ma_kcb từ checkbox được chọn
            list_kcb = []
            for row in range(self.tableWidget.rowCount()):

                # truy cập đến ô tại hàng i cột 1
                cell_widget = self.tableWidget.cellWidget(row, 0)

                # Kiểm tra xem ô đó có phải là QCheckBox hay không
                if isinstance(cell_widget, QCheckBox):
                    # Lấy giá trị của checkbox
                    checkbox_value = cell_widget.checkState()

                    # Kiểm tra giá trị của checkbox và xử lý tương ứng
                    if checkbox_value == Qt.Checked:
                        # truy cập đến ô tại hàng row, cột 2
                        item = self.tableWidget.item(row, 1)
                        # lấy giá trị của ô đó
                        kcb_value = item.text()
                        list_kcb.append(kcb_value)

            # lấy tất cả hos_id từ kcb
            list_hos_id=[]
            list_path=[]
            list_hos_blank_report=[]
            list_hos_chua_nop=[]

            for i in range(len(list_kcb)):

                # gọi database để lấy hos_id
                database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
                cnx = mysql.connector.connect(**database_config_setup)
                cursor = cnx.cursor()
                cursor.execute('select hos_id from hospital where code_kcb = %s', [list_kcb[i],])
                hos_id = cursor.fetchone()
                list_hos_id.append(hos_id)
                cnx.commit()
                cnx.close()

                # gọi database để lấy path
                database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
                cnx = mysql.connector.connect(**database_config_setup)
                cursor = cnx.cursor()
                cursor.execute('select report_path,report_name,status,hospital_id from report where hospital_id = %s', hos_id)
                data = cursor.fetchall()

                for i in data:
                    if i[2] == '0':
                        list_hos_chua_nop.append(i[3])
                    else:
                        list_path.append(data)
                cnx.commit()
                cnx.close()

            # lấy tên những bệnh viện chưa nộp
            hos_chua_nop_name=[]
            if list_hos_chua_nop:
                for i in range(len(list_hos_chua_nop)):
                    database_config_setup = cm.read_json_file(cm.FILE_JSON_PATH)
                    cnx = mysql.connector.connect(**database_config_setup)
                    cursor = cnx.cursor()
                    cursor.execute('select hos_name from hospital where hos_id = %s',[list_hos_chua_nop[i],])
                    data = cursor.fetchone()
                    hos_chua_nop_name.append(data)
            if hos_chua_nop_name:
                error_dialog = QMessageBox(QMessageBox.Critical, "Trảm",
                                           '{} chưa nộp thông báo'.format(hos_chua_nop_name), QMessageBox.Close)
                error_dialog.setStyleSheet("width: 300px")
                error_dialog.exec()

        except Exception as e:
            print(e)

    # import file excel vào database
    def import_data_from_file(self):

        try:

            #b1: gọi db lấy list mã kcb
            db_connect = cm.read_json_file(cm.FILE_JSON_PATH)
            cnx = mysql.connector.connect(**db_connect)
            cursor = cnx.cursor()
            cursor.execute('select code_kcb from hospital')
            data_rs = cursor.fetchall()
            cnx.commit()
            cnx.close()
            list_kcb=[]

            # lấy mã kcb
            for i in data_rs:

                list_kcb.append(i[0])

            # read file
            file_name = self.open_dialog_file()
            df = pd.read_excel(file_name)

            if df.size == 0:
                return

            data_insert=[]
            # trả về đối tượng pandas
            for row in df.iterrows():

                values = row[1]
                list_data=[]

                for col_index, value in enumerate(values):

                    # nếu trùng mã kcb thì ko append vào list
                    if value in list_kcb or not value:
                        break

                    list_data.append(str(value))

                # mà mã kcb mới và list không rỗng thì append
                if list_data:

                    data_insert.append(tuple(list_data))

            if data_insert:

                db_connect = cm.read_json_file(cm.FILE_JSON_PATH)
                cnx = mysql.connector.connect(**db_connect)
                cursor = cnx.cursor()
                stm = 'INSERT INTO hospital (code_kcb, hos_name, address, district) VALUES (%s,%s,%s,%s)'
                cursor.executemany(stm,data_insert)
                cnx.commit()
                cnx.close()
                print('import from file success')

            self.tableWidget.setRowCount(0)
            new_data = self.db_get_data_list()
            self.init_data(new_data)

        except Exception as e:
            print(e)

    # mở file excel để import
    def open_dialog_file(item, file_type="Excel (*.xlsx );;All Files (*)"):
        QFileDialog = QtWidgets.QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(QFileDialog, "Select File", os.path.expanduser('.'),file_type, options=options)
        return fileName

    # machine
    def open_static_widget(self):
        try:
            # ẩn các thứ ko liên quan
            self.tableWidget.hide()
            self.table_chat.hide()
            self.hide_all_button()

            # mở màn hình static
            self.static_widget.show()

            # fix lại tên
            charges_path = './get_report'
            dead_static_path='./get_report'
            self.charges_button.clicked.connect(self.charges_plot)
            self.dead_static_button.clicked.connect(self.predict_dead)

        except Exception as e:
            print(e)



    def open_static_excel_file(self,path):
        file_type = "Excel (*.xlsx );;All Files (*)"
        QFileDialog = QtWidgets.QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(QFileDialog, "Select File", os.path.expanduser(path), file_type,
                                                  options=options)
        return fileName

    # hiện tất cả các nút
    def show_all_button(self):

        self.delete_many_button.show()
        self.get_many_button.show()
        self.import_button.show()
        self.seach_txt.show()
        self.search_button.show()
        self.choose_many_button.show()

    # đóng tất cả các nút
    def hide_all_button(self):

        self.search_button.hide()
        self.choose_many_button.hide()
        self.import_button.hide()
        self.delete_many_button.hide()
        self.get_many_button.hide()
        self.seach_txt.hide()

    # biểu đồ thống kê
    def charges_plot(self):

        try:

            charges_path = './get_report/'
            file_name = self.open_static_excel_file(charges_path)

            # Machine.hospital_charges(file_name)
            self.open_plot = Machine.HospitalCharges(file_name)
            self.open_plot.show()

        except Exception as e:
            print(e)

    # dự đoán tỉ lệ tử vong
    def predict_dead(self):

        try:

            self.open_predict_screen = Dead_Heart.Ui_MainWindow()
            self.open_predict_screen.setupUi()
            self.open_predict_screen.show()

        except Exception as e:
            print(e)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  # manages the GUI application’s control flow and main settings, It handles widget specific initialization, finalization,It initializes the application with the user’s desktop settings
    ui = Ui_Goverment()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
