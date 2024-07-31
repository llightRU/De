import requests
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
import predict_heart

class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.logistic_button = QtWidgets.QPushButton(self.centralwidget)
        self.logistic_button.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.logistic_button.setObjectName("logistic_button")
        self.knn_button = QtWidgets.QPushButton(self.centralwidget)
        self.knn_button.setGeometry(QtCore.QRect(10, 120, 93, 31))
        self.knn_button.setObjectName("knn_button")
        self.rd_fr_button = QtWidgets.QPushButton(self.centralwidget)
        self.rd_fr_button.setGeometry(QtCore.QRect(10, 210, 161, 31))
        self.rd_fr_button.setObjectName("rd_fr_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 40, 221, 181))
        self.widget.setObjectName("widget")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # nhét ảnh
        # Thiết lập kích thước cửa sổ
        self.setGeometry(300, 200, 400, 300)

        # Tạo label chứa bức ảnh
        self.image_label = QLabel(self)
        self.image_label.setGeometry(190, 50, 221, 181)

        # Tải ảnh và thiết lập kích thước, vị trí và đường dẫn
        self.image = QPixmap('./img/select.png')
        self.image_label.setPixmap(self.image)
        self.image_label.setScaledContents(True)
        self.image_label.setPixmap(self.image.scaled(self.image_label.size()))

        self.retranslateUi()

        # button chọn các model
        self.knn_button.clicked.connect(self.open_predict_screen)
        self.logistic_button.clicked.connect(self.open_predict_screen)
        self.rd_fr_button.clicked.connect(self.open_predict_screen)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Select Model"))
        self.logistic_button.setText(_translate("MainWindow", "LogisticRegression"))
        self.knn_button.setText(_translate("MainWindow", "KNN"))
        self.rd_fr_button.setText(_translate("MainWindow", "RandomForestClassifer"))

    def open_predict_screen(self):

        # mở cửa sổ dự đoán
        self.open_predict_screen = predict_heart.Ui_MainWindow()
        self.open_predict_screen.setupUi()
        self.open_predict_screen.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication([])
    window = Ui_MainWindow()
    window.setupUi()
    window.show()
    app.exec_()