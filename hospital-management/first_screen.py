from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QBrush, QColor,QPalette
from PyQt5.QtWidgets import QApplication, QWidget
import Login_Screen

class Ui_Hospital_App(QMainWindow):
    def __init__(self,parent=None):
        super(Ui_Hospital_App,self).__init__(parent)
    def setupUi(self):
        self.setObjectName("Hospital_App")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # tạo QWidget để chứa ảnh, nằm trong centralwidget - bug self.centralwidget
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(350, 90, 361, 411))
        self.widget.setObjectName("widget")

        self.farmer_button = QtWidgets.QPushButton(self.centralwidget)
        self.farmer_button.setGeometry(QtCore.QRect(80, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.farmer_button.setFont(font)
        self.farmer_button.setObjectName("farmer_button")
        self.staff_button = QtWidgets.QPushButton(self.centralwidget)
        self.staff_button.setGeometry(QtCore.QRect(80, 200, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.staff_button.setFont(font)
        self.staff_button.setObjectName("staff_button")
        self.goverment_button = QtWidgets.QPushButton(self.centralwidget)
        self.goverment_button.setGeometry(QtCore.QRect(80, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.goverment_button.setFont(font)
        self.goverment_button.setObjectName("goverment_button")
        self.game_title = QtWidgets.QLabel(self.centralwidget)
        self.game_title.setGeometry(QtCore.QRect(240, 0, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.game_title.setFont(font)
        self.game_title.setObjectName("game_title")

        # chọn Widget chính - là centralwidget
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.viet_nam = QtWidgets.QMenu(self.menubar)
        self.viet_nam.setObjectName("viet_nam")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar.addAction(self.viet_nam.menuAction())

        # màu nền
        self.centralwidget.setStyleSheet("background-color: #AAAAAA;")

        # tạo nút chọn farmer
        self.login_farmer = QtWidgets.QPushButton(self.centralwidget)
        self.login_farmer.setGeometry(QtCore.QRect(470, 510, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_farmer.setFont(font)
        self.login_farmer.setObjectName("login")
        self.login_farmer.hide()

        # tạo nút chọn staff
        self.login_staff = QtWidgets.QPushButton(self.centralwidget)
        self.login_staff.setGeometry(QtCore.QRect(470, 510, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_staff.setFont(font)
        self.login_staff.setObjectName("login")
        self.login_staff.hide()

        # tạo nút chọn goverment
        self.login_goverment = QtWidgets.QPushButton(self.centralwidget)
        self.login_goverment.setGeometry(QtCore.QRect(470, 510, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_goverment.setFont(font)
        self.login_goverment.setObjectName("login")
        self.login_goverment.hide()

        # render giao diện
        self.retranslateUi()

        #style màu button
        self.goverment_button.setStyleSheet("background-color: rgb(255,255,255);")
        self.staff_button.setStyleSheet("background-color: rgb(255,255,255);")
        self.farmer_button.setStyleSheet("background-color: rgb(255,255,255);")

        #set up current button
        self.current_button = self.farmer_button

        # xử lí các button - Server nông dân: farmer_button, Server cán bộ: staff_button, Server chính phủ: goverment_button
        self.farmer_button.clicked.connect(self.background_farmer_img)
        self.staff_button.clicked.connect(self.background_staff_img)
        self.goverment_button.clicked.connect(self.background_goverment_img)

        # xử lí button chọn
        self.login_farmer.clicked.connect(
            lambda *arg,screen_id=1: self.open_login_screen(screen_id)
        )
        self.login_staff.clicked.connect(
            lambda *arg, screen_id=2: self.open_login_screen(screen_id)
        )
        self.login_goverment.clicked.connect(
        lambda *arg,screen_id=3: self.open_login_screen(screen_id)
        )

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Hospital_App", "Ballcube"))
        self.farmer_button.setText(_translate("Hospital_App", "Dân chơi"))
        self.staff_button.setText(_translate("Hospital_App", "Chủ sân"))
        self.goverment_button.setText(_translate("Hospital_App", "Admin"))
        self.game_title.setText(_translate("Hospital_App", "Chọn vai trò"))
        self.viet_nam.setTitle(_translate("Hospital_App", "Việt Nam"))
        self.login_farmer.setText(_translate("Hospital_App", "Chọn"))
        self.login_staff.setText(_translate("Hospital_App", "Chọn"))
        self.login_goverment.setText(_translate("Hospital_App", "Chọn"))
        self.login_farmer.setStyleSheet("background-color: rgb(255,255,255);")
        self.login_staff.setStyleSheet("background-color: rgb(255,255,255);")
        self.login_goverment.setStyleSheet("background-color: rgb(255,255,255);")

    def background_farmer_img(self):
        try:
            self.current_button.setStyleSheet("background-color: rgb(255,255,255);")
            self.current_button = self.farmer_button
            self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")
            # tạo ảnh cho QWidget
            pixmap = QPixmap('./img/farmer1.png')
            # Thay đổi kích thước của pixmap
            pixmap = pixmap.scaled(self.widget.width(), self.widget.height())
            # Tạo một brush từ đối tượng pixmap
            brush = QBrush(pixmap)
            palette = self.widget.palette()
            palette.setBrush(QPalette.Background, brush)
            self.widget.setPalette(palette)
            self.widget.setAutoFillBackground(True)
            self.widget.show()
            # hiển thị nút đăng nhập
            self.login_farmer.show()
        except Exception as e:
            print(e)

    def background_staff_img(self):
        self.current_button.setStyleSheet("background-color: rgb(255,255,255);")
        self.current_button = self.staff_button
        self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")
        # tạo ảnh cho QWidget
        pixmap = QPixmap('./img/staff1.png')
        # Thay đổi kích thước của pixmap
        pixmap = pixmap.scaled(self.widget.width(), self.widget.height())
        # Tạo một brush từ đối tượng pixmap
        brush = QBrush(pixmap)
        palette = self.widget.palette()
        palette.setBrush(QPalette.Background, brush)
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.show()
        # hiển thị nút đăng nhập
        self.login_staff.show()

    def background_goverment_img(self):
        self.current_button.setStyleSheet("background-color: rgb(255,255,255);")
        self.current_button = self.goverment_button
        self.current_button.setStyleSheet("background-color: rgb(85, 170, 255);")
        # tạo ảnh cho QWidget
        pixmap = QPixmap('./img/goverment1.png')
        # Thay đổi kích thước của pixmap
        pixmap = pixmap.scaled(self.widget.width(), self.widget.height())
        # Tạo một brush từ đối tượng pixmap
        brush = QBrush(pixmap)
        palette = self.widget.palette()
        palette.setBrush(QPalette.Background, brush)
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.show()
        # hiển thị nút đăng nhập
        self.login_goverment.show()

    def open_login_screen(self,screen_id):
        try:
            self.login_screen = Login_Screen.Ui_Login(screen_id)
            self.login_screen.setupUi()
            if int(screen_id) != 1:
                self.login_screen.create_new_ac_button.hide()
            self.login_screen.show()
        except Exception as e:
            print(e)



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  # manages the GUI application’s control flow and main settings, It handles widget specific initialization, finalization,It initializes the application with the user’s desktop settings
    ui = Ui_Hospital_App()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())