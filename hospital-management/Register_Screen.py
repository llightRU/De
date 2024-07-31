import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
import Login_Screen
import sys

import common as cm
import validate as v

class Ui_Register(QMainWindow):

    def __init__(self,parent=None):
        super(Ui_Register,self).__init__(parent)
        filename = './database_config.json'
        if v.check_file_open(filename):
            with open(filename) as f:
                config = json.load(f)
                f.close()
            try:
                self.cnx = cm.connect_sql(config)
                cm.connect_database(self.cnx, config)
            except Exception as err:
                QMessageBox.information(self, 'Error', str(err.args[0]) + "\nYour init file config is wrong",
                                        QMessageBox.Close)

    def setupUi(self):
        self.setObjectName("Register")
        self.resize(500, 700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 50, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.name_txt = QtWidgets.QLineEdit(self.groupBox)
        self.name_txt.setGeometry(QtCore.QRect(60, 30, 281, 31))
        self.name_txt.setObjectName("name_txt")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 130, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.identify_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.identify_txt.setGeometry(QtCore.QRect(60, 31, 281, 31))
        self.identify_txt.setObjectName("identify_txt")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(190, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 480, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.password_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.password_txt.setGeometry(QtCore.QRect(60, 31, 281, 31))
        self.password_txt.setObjectName("password_txt")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(60, 390, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.account_txt = QtWidgets.QLineEdit(self.groupBox_4)
        self.account_txt.setGeometry(QtCore.QRect(60, 30, 281, 31))
        self.account_txt.setObjectName("account_txt")
        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_button.setGeometry(QtCore.QRect(40, 580, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sign_in_button.setFont(font)
        self.sign_in_button.setObjectName("sign_in_button")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(340, 580, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_button.setFont(font)
        self.register_button.setObjectName("register_button")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(60, 210, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.dob_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.dob_txt.setGeometry(QtCore.QRect(60, 30, 281, 31))
        self.dob_txt.setObjectName("dob_txt")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(60, 300, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.country_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.country_txt.setGeometry(QtCore.QRect(60, 31, 281, 31))
        self.country_txt.setObjectName("country_txt")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menuFarmer = QtWidgets.QMenu(self.menubar)
        self.menuFarmer.setObjectName("menuFarmer")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFarmer.menuAction())

        # render UI
        self.retranslateUi()

        # xử lí các button
        self.sign_in_button.clicked.connect(self.open_sign_in_screen)
        self.register_button.clicked.connect(self.regis_account)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Register", "Register Screen"))
        self.groupBox.setTitle(_translate("Register", "Họ và tên"))
        self.groupBox_2.setTitle(_translate("Register", "Căn cước"))
        self.title.setText(_translate("Register", "Đăng Ký"))
        self.groupBox_3.setTitle(_translate("Register", "Mật khẩu"))
        self.groupBox_4.setTitle(_translate("Register", "Tài khoản"))
        self.sign_in_button.setText(_translate("Register", "<< Đăng nhập"))
        self.register_button.setText(_translate("Register", "Đăng ký >>"))
        self.groupBox_5.setTitle(_translate("Register", "Ngày sinh"))
        self.groupBox_6.setTitle(_translate("Register", "Quê quán"))
        self.menuFarmer.setTitle(_translate("Register", "Farmer"))

    # tạo biến --sign_in_screen-- kết nối với màn hình đăng nhập
    def connect_sign_in_screen(self):
        self.sign_in_screen = Login_Screen.Ui_Login(1)
        self.sign_in_screen.setupUi()

    def open_sign_in_screen(self):
        # gọi hàm connect_sign_in_screen để khởi tạo biến --sign_in_screen-- kết nối với màn hình đăng nhập
        try:
            self.connect_sign_in_screen()
            self.sign_in_screen.show()
            self.hide()
        except Exception as e:
            print(e)

    def regis_account(self):
        try:
            cursor = self.cnx.cursor()
            name = self.name_txt.text()
            if not v.check_string(name):
                QMessageBox.information(self, 'Warning', 'name Should not be blank', QMessageBox.Close)
                return
            identify = self.identify_txt.text()
            if not  v.check_id_card(identify):
                QMessageBox.information(self, 'Warning', 'identify Should not be blank', QMessageBox.Close)
                return
            account = self.account_txt.text()
            if not account:
                QMessageBox.information(self, 'Warning', 'account Should not be blank', QMessageBox.Close)
                return
            password = self.password_txt.text()
            if not password:
                QMessageBox.information(self, 'Warning', 'password Should not be blank', QMessageBox.Close)
                return
            dob = v.get_date(self.dob_txt.text())
            if not v.check_date(dob):
                QMessageBox.information(self, 'Warning', 'dob Should be Year-Month-Day', QMessageBox.Close)
                return
            country = self.country_txt.text()
            if not v.check_string(country):
                QMessageBox.information(self, 'Warning', 'country Should not be blank', QMessageBox.Close)
                return

            all_user = cm.get_user_name(cursor)
            print(all_user)
            for i in all_user:
                if account == i[0]:
                    QMessageBox.information(self, 'Warning', 'username exist', QMessageBox.Close)

            if cm.insert_account(cursor, self.cnx, account, password) == True:
                acc_id = cm.get_acc_id_account(cursor, account, password)
                if cm.insert_famer(cursor, self.cnx, name,identify, dob, country, acc_id) == True:
                    QMessageBox.information(self, 'Message', 'Register successful', QMessageBox.Close)
                    # gọi hàm connect_sign_in_screen để khởi tạo biến --sign_in_screen-- kết nối với màn hình đăng nhập
                    self.connect_sign_in_screen()
                    self.hide()
                    self.sign_in_screen.show()
        except Exception as e:
            print(e)
            QMessageBox.information(self, 'Warning', 'Register fail', QMessageBox.Close)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  # manages the GUI application’s control flow and main settings, It handles widget specific initialization, finalization,It initializes the application with the user’s desktop settings
    ui = Ui_Register()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
