from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import first_screen
import common as cm
import validate as v
import json

class Ui_Farmer(QMainWindow):
    def __init__(self,id,parent=None):
        super(Ui_Farmer,self).__init__(parent)
        self.id = id
        print(type(self.id))
        filename = './database_config.json'
        if v.check_file_open(filename):
            with open(filename) as f:
                config = json.load(f)
                f.close()
            try:
                self.cnx = cm.connect_sql(config)
                cm.connect_database(self.cnx,config)
            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0]) + "\nYour init file config is wrong",
                                        QMessageBox.Close)

    def setupUi(self):
        self.setObjectName("Farmer")
        self.resize(791, 554)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.info_button = QtWidgets.QPushButton(self.centralwidget)
        self.info_button.setGeometry(QtCore.QRect(0, 240, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.info_button.setFont(font)
        self.info_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.info_button.setObjectName("info_button")
        self.profile_button = QtWidgets.QPushButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(0, 290, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.profile_button.setFont(font)
        self.profile_button.setObjectName("profile_button")
        self.search_hos_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_hos_button.setGeometry(QtCore.QRect(0, 340, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.search_hos_button.setFont(font)
        self.search_hos_button.setObjectName("search_hos_button")
        self.change_pass_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_pass_button.setGeometry(QtCore.QRect(0, 390, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.change_pass_button.setFont(font)
        self.change_pass_button.setObjectName("change_pass_button")
        self.log_out_button = QtWidgets.QPushButton(self.centralwidget)
        self.log_out_button.setGeometry(QtCore.QRect(0, 440, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.log_out_button.setFont(font)
        self.log_out_button.setObjectName("log_out_button")
        self.info_title = QtWidgets.QLabel(self.centralwidget)
        self.info_title.setGeometry(QtCore.QRect(350, 10, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.info_title.setFont(font)
        self.info_title.setObjectName("info_title")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 60, 451, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(310, 0, 20, 491))
        self.line_2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.avatar = QtWidgets.QLabel(self.centralwidget)
        self.avatar.setGeometry(QtCore.QRect(0, 0, 321, 221))
        self.avatar.setText("")
        self.avatar.setObjectName("avatar")
        self.account_box = QtWidgets.QGroupBox(self.centralwidget)
        self.account_box.setGeometry(QtCore.QRect(360, 90, 401, 401))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.account_box.setFont(font)
        self.account_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.account_box.setObjectName("account_box")
        self.label = QtWidgets.QLabel(self.account_box)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.account_box)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.account_box)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.name_txt = QtWidgets.QLineEdit(self.account_box)
        self.name_txt.setGeometry(QtCore.QRect(150, 40, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.name_txt.setFont(font)
        self.name_txt.setObjectName("name_txt")
        self.label_4 = QtWidgets.QLabel(self.account_box)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.account_box)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dob_txt = QtWidgets.QDateEdit(self.account_box)
        self.dob_txt.setGeometry(QtCore.QRect(150, 130, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.dob_txt.setFont(font)
        self.dob_txt.setObjectName("dob_txt")
        self.save_account_button = QtWidgets.QPushButton(self.account_box)
        self.save_account_button.setGeometry(QtCore.QRect(270, 330, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.save_account_button.setFont(font)
        self.save_account_button.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.save_account_button.setObjectName("save_account_button")
        self.male_button = QtWidgets.QRadioButton(self.account_box)
        self.male_button.setGeometry(QtCore.QRect(80, 250, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.male_button.setFont(font)
        self.male_button.setObjectName("male_button")
        self.female_button = QtWidgets.QRadioButton(self.account_box)
        self.female_button.setGeometry(QtCore.QRect(240, 250, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.female_button.setFont(font)
        self.female_button.setObjectName("female_button")
        self.cardId_txt = QtWidgets.QLineEdit(self.account_box)
        self.cardId_txt.setGeometry(QtCore.QRect(150, 90, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.cardId_txt.setFont(font)
        self.cardId_txt.setObjectName("cardId_txt")
        self.country_txt = QtWidgets.QLineEdit(self.account_box)
        self.country_txt.setGeometry(QtCore.QRect(150, 170, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.country_txt.setFont(font)
        self.country_txt.setObjectName("country_txt")
        self.medical_box = QtWidgets.QGroupBox(self.centralwidget)
        self.medical_box.setGeometry(QtCore.QRect(360, 90, 401, 401))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.medical_box.setFont(font)
        self.medical_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.medical_box.setObjectName("medical_box")
        self.id_txt = QtWidgets.QLineEdit(self.medical_box)
        self.id_txt.setGeometry(QtCore.QRect(90, 40, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.id_txt.setFont(font)
        self.id_txt.setObjectName("id_txt")
        self.label_10 = QtWidgets.QLabel(self.medical_box)
        self.label_10.setGeometry(QtCore.QRect(50, 30, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.medical_table = QtWidgets.QTableWidget(self.medical_box)
        self.medical_table.setGeometry(QtCore.QRect(30, 90, 351, 241))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.medical_table.setFont(font)
        self.medical_table.setObjectName("medical_table")
        self.medical_table.setColumnCount(0)
        self.medical_table.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.medical_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.medical_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.medical_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.medical_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.medical_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.medical_table.setVerticalHeaderItem(5, item)
        self.change_password_box = QtWidgets.QGroupBox(self.centralwidget)
        self.change_password_box.setGeometry(QtCore.QRect(360, 90, 401, 401))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.change_password_box.setFont(font)
        self.change_password_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.change_password_box.setObjectName("change_password_box")
        self.label_7 = QtWidgets.QLabel(self.change_password_box)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.old_pass_txt = QtWidgets.QLineEdit(self.change_password_box)
        self.old_pass_txt.setGeometry(QtCore.QRect(150, 60, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.old_pass_txt.setFont(font)
        self.old_pass_txt.setObjectName("old_pass_txt")
        self.label_8 = QtWidgets.QLabel(self.change_password_box)
        self.label_8.setGeometry(QtCore.QRect(30, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.change_password_box)
        self.label_9.setGeometry(QtCore.QRect(30, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.new_pass_txt = QtWidgets.QLineEdit(self.change_password_box)
        self.new_pass_txt.setGeometry(QtCore.QRect(150, 120, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.new_pass_txt.setFont(font)
        self.new_pass_txt.setObjectName("new_pass_txt")
        self.confirm_txt = QtWidgets.QLineEdit(self.change_password_box)
        self.confirm_txt.setGeometry(QtCore.QRect(150, 180, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.confirm_txt.setFont(font)
        self.confirm_txt.setObjectName("confirm_txt")
        self.save_password_button = QtWidgets.QPushButton(self.change_password_box)
        self.save_password_button.setGeometry(QtCore.QRect(270, 330, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.save_password_button.setFont(font)
        self.save_password_button.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.save_password_button.setObjectName("save_password_button")
        self.find_hospital_box = QtWidgets.QGroupBox(self.centralwidget)
        self.find_hospital_box.setGeometry(QtCore.QRect(360, 90, 401, 401))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.find_hospital_box.setFont(font)
        self.find_hospital_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.find_hospital_box.setObjectName("find_hospital_box")
        self.hospital_table = QtWidgets.QTableWidget(self.find_hospital_box)
        self.hospital_table.setGeometry(QtCore.QRect(20, 150, 361, 221))
        self.hospital_table.setObjectName("hospital_table")
        self.hospital_table.setColumnCount(3)
        self.hospital_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hospital_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospital_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.hospital_table.setHorizontalHeaderItem(2, item)
        self.hospital_txt = QtWidgets.QLineEdit(self.find_hospital_box)
        self.hospital_txt.setGeometry(QtCore.QRect(20, 51, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.hospital_txt.setFont(font)
        self.hospital_txt.setObjectName("hospital_txt")
        self.search_button = QtWidgets.QPushButton(self.find_hospital_box)
        self.search_button.setGeometry(QtCore.QRect(280, 50, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.search_button.setObjectName("search_button")
        self.find_hosName_button = QtWidgets.QRadioButton(self.find_hospital_box)
        self.find_hosName_button.setGeometry(QtCore.QRect(70, 110, 95, 20))
        self.find_hosName_button.setObjectName("find_hosName_button")
        self.find_hosAd_button = QtWidgets.QRadioButton(self.find_hospital_box)
        self.find_hosAd_button.setGeometry(QtCore.QRect(230, 110, 95, 20))
        self.find_hosAd_button.setObjectName("find_hosAd_button")
        self.avatar.raise_()
        self.info_button.raise_()
        self.profile_button.raise_()
        self.search_hos_button.raise_()
        self.change_pass_button.raise_()
        self.log_out_button.raise_()
        self.info_title.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.account_box.raise_()
        self.medical_box.raise_()
        self.change_password_box.raise_()
        self.find_hospital_box.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        #code
        #avatar
        self.avatar.setPixmap(QtGui.QPixmap('img/farmer1.png'))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")

        #innitial values
        self.find_hosAd_button.setChecked(1)
        self.data_to_account_info()
        self.data_to_medical_box()
        self.data_to_find_hospital()
        #set all box invisible

        self.account_box.hide()
        self.medical_box.hide()
        self.change_password_box.hide()
        self.find_hospital_box.hide()

        # set current box

        self.current_box = self.account_box
        self.current_box.show()
        self.current_button = self.info_button
        self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")

        # set button active

        self.info_button.clicked.connect(self.info_button_active)
        self.profile_button.clicked.connect(self.profile_button_active)
        self.search_hos_button.clicked.connect(self.search_hos_button_active)
        self.change_pass_button.clicked.connect(self.change_password_button_active)
        self.log_out_button.clicked.connect(self.log_out_button_active)
        self.save_account_button.clicked.connect(self.save_account_button_active)
        self.save_password_button.clicked.connect(self.save_password_button_active)
        self.search_button.clicked.connect(self.search_button_active)


        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Farmer", "Farmer Screen"))
        self.info_button.setText(_translate("Farmer", "Thông tin cơ bản"))
        self.profile_button.setText(_translate("Farmer", "Chỉ số cơ thể"))
        self.search_hos_button.setText(_translate("Farmer", "Tìm bệnh viện"))
        self.change_pass_button.setText(_translate("Farmer", "Đổi mật khẩu"))
        self.log_out_button.setText(_translate("Farmer", "Đăng xuất"))
        self.info_title.setText(_translate("Farmer", "Thông tin"))
        self.account_box.setTitle(_translate("Farmer", "Account"))
        self.label.setText(_translate("Farmer", "Họ và tên:"))
        self.label_2.setText(_translate("Farmer", "Căn cước:"))
        self.label_3.setText(_translate("Farmer", "Ngày sinh:"))
        self.label_4.setText(_translate("Farmer", "Quê  quán:"))
        self.label_5.setText(_translate("Farmer", "Giới tính:"))
        self.save_account_button.setText(_translate("Farmer", "Save"))
        self.male_button.setText(_translate("Farmer", "Nam"))
        self.female_button.setText(_translate("Farmer", "Nữ"))
        self.medical_box.setTitle(_translate("Farmer", "Medical Profile"))
        self.label_10.setText(_translate("Farmer", "ID:"))
        item = self.medical_table.verticalHeaderItem(0)
        item.setText(_translate("Farmer", "Dung tích hồng cầu"))
        item = self.medical_table.verticalHeaderItem(1)
        item.setText(_translate("Farmer", "Huyết sắc tố"))
        item = self.medical_table.verticalHeaderItem(2)
        item.setText(_translate("Farmer", "Hồng cầu"))
        item = self.medical_table.verticalHeaderItem(3)
        item.setText(_translate("Farmer", "Tiểu cầu"))
        item = self.medical_table.verticalHeaderItem(4)
        item.setText(_translate("Farmer", "Huyết sắc tố trung bình hồng cầu"))
        item = self.medical_table.verticalHeaderItem(5)
        item.setText(_translate("Farmer", "Thể tích hồng cầu trung bình"))
        self.change_password_box.setTitle(_translate("Farmer", "Change password"))
        self.label_7.setText(_translate("Farmer", "Mật khẩu cũ:"))
        self.label_8.setText(_translate("Farmer", "Mật khẩu mới:"))
        self.label_9.setText(_translate("Farmer", "Xác nhận lại: "))
        self.save_password_button.setText(_translate("Farmer", "Save"))
        self.find_hospital_box.setTitle(_translate("Farmer", "Find hospital"))
        item = self.hospital_table.horizontalHeaderItem(0)
        item.setText(_translate("Farmer", "Tên"))
        item = self.hospital_table.horizontalHeaderItem(1)
        item.setText(_translate("Farmer", "Địa chỉ"))
        item = self.hospital_table.horizontalHeaderItem(2)
        item.setText(_translate("Farmer", "Order"))
        self.search_button.setText(_translate("Farmer", "Search"))
        self.find_hosName_button.setText(_translate("Farmer", "Tên"))
        self.find_hosAd_button.setText(_translate("Farmer", "Vùng"))


    #active the button

    def info_button_active(self):
        try:
            self.current_button.setStyleSheet("background-color: rgb(255,255,255);")
            self.current_button = self.info_button
            self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")
            self.account_box_active()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nWhen active account button, something wrong happen",
                                    QMessageBox.Close)
            return

    def profile_button_active(self):
        try:
            self.current_button.setStyleSheet("background-color: rgb(255,255,255);")
            self.current_button = self.profile_button
            self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")
            self.medical_box_active()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nWhen active medical button, something wrong happen",
                                    QMessageBox.Close)
            return

    def search_hos_button_active(self):
        try:
            self.current_button.setStyleSheet("background-color: rgb(255,255,255);")
            self.current_button = self.search_hos_button
            self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")
            self.find_hospital_box_active()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nWhen active find hospital button, something wrong happen",
                                    QMessageBox.Close)
            return

    def change_password_button_active(self):
        try:
            self.current_button.setStyleSheet("background-color: rgb(255,255,255);")
            self.current_button = self.change_pass_button
            self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")
            self.change_password_box_active()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nWhen active change password button, something wrong happen",
                                    QMessageBox.Close)
            return

    def log_out_button_active(self):
        try:
            self.ui_logout = first_screen.Ui_Hospital_App()
            self.ui_logout.setupUi()
            self.ui_logout.show()
            self.hide()
        except Exception as err:
            QMessageBox.information(self,'Error',str(err.args[0]),QMessageBox.Close)

    def hide_box(self):
        try:
            self.account_box.hide()
            self.find_hospital_box.hide()
            self.change_password_box.hide()
            self.medical_box.hide()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nWhen hide box, something wrong happen",QMessageBox.Close)
            return

    # initial data to group box
    def data_to_account_info(self):
        try:
            cursor = self.cnx.cursor()
            sql_join = "select f.user_name, f.id_card, " \
                       "f.dob, f.country, f.sex, f.acc_id ,f.id " \
                       "from farmer f " \
                       "inner join account " \
                       "on f.acc_id = account.acc_id " \
                       "where f.id = {}".format(self.id)
            cursor.execute(sql_join)
            values = cursor.fetchone()
            self.name_txt.setText(str(values[0]))
            self.cardId_txt.setText(str(values[1]))
            self.dob_txt.setDate(values[2])
            self.country_txt.setText(str(values[3]))
            if values[4]:
                self.male_button.setChecked(1)
            else:
                self.female_button.setChecked(1)
            self.account_values = values
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]),QMessageBox.Close)
            return

    def data_to_medical_box(self):
        try:
            self.id_txt.setText(str(self.account_values[-1]))
            self.id_txt.setEnabled(False)
            medical_results = cm.check_health_from_farmerId(self.cnx.cursor(),self.account_values[-1])
            if not medical_results:
                return
            self.medical_table.setColumnCount(self.medical_table.columnCount() + 1)
            self.medical_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Values"))
            for i in range(6):
                item = QtWidgets.QTableWidgetItem(str(medical_results[i+3]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.medical_table.setItem(0, i,item)

        except Exception as err:
            print(err)
            # QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)
            return

    def data_to_find_hospital(self):
        try:
            all_hospital = cm.show_table(self.cnx.cursor(),'hospital')
            for i in range(len(all_hospital)):
                self.hospital_table.insertRow(i)
                item = QtWidgets.QTableWidgetItem(str(all_hospital[i][2]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.hospital_table.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem(str(all_hospital[i][3]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.hospital_table.setItem(i, 1, item)
                ####
                self.edit_btn = QtWidgets.QPushButton(self)
                self.edit_btn.setText('Edit')
                self.hospital_table.setCellWidget(i, 2, self.edit_btn)
        except Exception as err:
            from PyQt5.QtWidgets import QMainWindow, QPushButton, QCheckBox, QMessageBox, QWidget
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)
            return

    # display the group box
    def account_box_active(self):
        try:
            self.hide_box()
            self.current_box = self.account_box
            self.current_box.show()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]) + "\nWhen active account box, something wrong happen",
                                    QMessageBox.Close)
            return

    def medical_box_active(self):
        try:
            self.hide_box()
            self.current_box = self.medical_box
            self.current_box.show()
            medical_results = cm.check_health_from_farmerId(self.cnx.cursor(),self.account_values[-1])
            if not medical_results:
                QMessageBox.information(self, 'Error',"\nDon't have medical result yet",
                                        QMessageBox.Close)
            return
        except Exception as err:
            QMessageBox.information(self, 'Error',
                                    str(err.args[0]) + "\nWhen active medical box, something wrong happen",
                                    QMessageBox.Close)
            return

    def find_hospital_box_active(self):
        try:
            self.hide_box()
            self.current_box = self.find_hospital_box
            self.current_box.show()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error',
                                    str(err.args[0]) + "\nWhen active find hospital box, something wrong happen",
                                    QMessageBox.Close)
            return

    def change_password_box_active(self):
        try:
            self.hide_box()
            self.current_box = self.change_password_box
            self.current_box.show()
            return
        except Exception as err:
            QMessageBox.information(self, 'Error',
                                    str(err.args[0]) + "\nWhen active change password box, something wrong happen",
                                    QMessageBox.Close)
            return

    #button inside the group box

    def save_account_button_active(self):
        try:
            values_fix = []
            values_fix.append(self.name_txt.text())
            values_fix.append(self.cardId_txt.text())
            values_fix.append(self.dob_txt.date().toPyDate())
            values_fix.append(self.country_txt.text())
            if self.female_button.isChecked():
                values_fix.append(0)
            else:
                values_fix.append(1)
            values_fix.append(self.account_values[-1])
            for x in zip(self.account_values,values_fix):
                print(x[0],x[1])
                if x[0] != x[1]:
                    print(x[0])
                    if v.valid_famer_info(self,values_fix):
                        cm.update_farmer(self.cnx,values_fix)
                    else:
                        break
                    break
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]),QMessageBox.Close)
            return

    def save_password_button_active(self):
        try:
            old_pass = self.old_pass_txt.text()
            new_pass = self.new_pass_txt.text()
            confirm = self.confirm_txt.text()
            info = cm.get_account_by_id(self.cnx.cursor(), self.account_values[-2])
            if old_pass != info[2]:
                QMessageBox.information(self, 'Error', 'Your old password is not correct', QMessageBox.Close)
                return
            if new_pass != confirm:
                QMessageBox.information(self, 'Error', 'Your password is not equal to cofirm', QMessageBox.Close)
                return
            if not v.check_pass(new_pass):
                QMessageBox.information(self, 'Error', 'Your password is invalid', QMessageBox.Close)
                return
            if new_pass == old_pass:
                QMessageBox.information(self, 'Error', 'Your new password is same as old password', QMessageBox.Close)
                return
            cm.update_password(self.cnx,new_pass,self.account_values[-2])
            QMessageBox.information(self, 'Success', 'Your password has been changed', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)
            return

    def search_button_active(self):
        try:
            if self.find_hosAd_button.isChecked():
                address = self.hospital_txt.text()
                hospital = cm.search_address(self.cnx.cursor(),'hospital',address)
            else:
                name = self.hospital_txt.text()
                hospital = cm.search_name(self.cnx.cursor(),'hospital',name)
            print(hospital)
            self.hospital_table.clearContents()
            self.hospital_table.setRowCount(0)
            for i in range(len(hospital)):
                self.hospital_table.insertRow(i)
                item = QtWidgets.QTableWidgetItem(str(hospital[i][2]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.hospital_table.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem(str(hospital[i][3]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.hospital_table.setItem(i, 1, item)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Farmer(1)
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

