import json
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import Register_Screen
import common as cm
import validate as v
import Famer
import Goverment
import Staff

class Ui_Login(QMainWindow):
    def __init__(self,screen,parent=None):
        super(Ui_Login,self).__init__(parent)
        self.screen=screen
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
        self.setObjectName("Login")
        self.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(160, 0, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 40, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.account = QtWidgets.QLineEdit(self.groupBox)
        self.account.setGeometry(QtCore.QRect(60, 30, 281, 31))
        self.account.setObjectName("account")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 130, 391, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.password = QtWidgets.QLineEdit(self.groupBox_2)
        self.password.setGeometry(QtCore.QRect(60, 31, 281, 31))
        self.password.setObjectName("password")
        self.create_new_ac_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_new_ac_button.setGeometry(QtCore.QRect(400, 217, 93, 31))
        self.create_new_ac_button.setObjectName("create_new_ac_button")
        self.sign_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_button.setGeometry(QtCore.QRect(200, 210, 93, 31))
        self.sign_in_button.setObjectName("sign_in_button")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menuFarmer = QtWidgets.QMenu(self.menubar)
        self.menuFarmer.setGeometry(QtCore.QRect(895, 220, 159, 54))
        self.menuFarmer.setObjectName("menuFarmer")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFarmer.menuAction())

        # render UI Login
        self.retranslateUi()

        # xử lí các button - đăng kí: create_new_ac_button, đăng nhập: sign_in_button
        self.create_new_ac_button.clicked.connect(self.open_register_screen)
        self.sign_in_button.clicked.connect(self.sign_in)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Login Screen"))
        self.title.setText(_translate("Login", "Đăng Nhập"))
        self.groupBox.setTitle(_translate("Login", "Tài khoản"))
        self.groupBox_2.setTitle(_translate("Login", "Mật khẩu"))
        self.create_new_ac_button.setText(_translate("Login", "Tạo tài khoản"))
        self.sign_in_button.setText(_translate("Login", "Đăng nhập"))
        self.menuFarmer.setTitle(_translate("Login", "Farmer"))

    def open_register_screen(self):
        self.register_screen = Register_Screen.Ui_Register()
        self.register_screen.setupUi()
        self.register_screen.show()
        self.hide()

    def sign_in(self):
        try:
            # pass
            account = self.account.text()
            if not account:
                QMessageBox.information(self, 'Message', 'Account blank', QMessageBox.Close)
                return
            password = self.password.text()
            if not password:
                QMessageBox.information(self, 'Message', 'Password blank', QMessageBox.Close)
                return
            cursor = self.cnx.cursor()
            role = cm.get_account(cursor, account, password)
            print(role)

            id_farmer= cm.get_farmer_by_acc_id(cursor,role[0])
            if role[3] != self.screen:
                QMessageBox.information(self, 'Error', 'Your account is not in this screen', QMessageBox.Close)
                return
            if (role[3] == 1):
                self.Famer = Famer.Ui_Farmer(id_farmer[0])
                self.Famer.setupUi()
                self.Famer.show()
                self.hide()
            if (role[3] == 2):
                self.Staff = Staff.Ui_Staff()
                self.Staff.setupUi()
                self.Staff.show()
                self.hide()
            if (role[3] == 3):
                self.Goverment = Goverment.Ui_Goverment()
                self.Goverment.setupUi()
                self.Goverment.show()
                self.hide()

        except Exception as error:
            print(error)
            QMessageBox.information(self, 'Message', 'Account or Password incorect', QMessageBox.Close)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  # manages the GUI application’s control flow and main settings, It handles widget specific initialization, finalization,It initializes the application with the user’s desktop settings
    ui = Ui_Login()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())