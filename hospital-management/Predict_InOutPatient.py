from datetime import datetime

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
import sys
import validate as v
import json
import common as cm
import Machine
import machine_build
import numpy as np
class Ui_Medical_Certi(QMainWindow):
    def __init__(self,farmer_id=0,parent=None):
        super(Ui_Medical_Certi,self).__init__(parent)
        self.farmer_id = farmer_id
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
        self.setObjectName("Medical_Certi")
        self.resize(500, 755)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.medical_certi = QtWidgets.QLabel(self.centralwidget)
        self.medical_certi.setGeometry(QtCore.QRect(190, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.medical_certi.setFont(font)
        self.medical_certi.setObjectName("medical_certi")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 220, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.dthc_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.dthc_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.dthc_txt.setObjectName("dthc_txt")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(60, 280, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.hst_txt = QtWidgets.QLineEdit(self.groupBox_4)
        self.hst_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.hst_txt.setObjectName("hst_txt")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(60, 340, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.hc_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.hc_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.hc_txt.setObjectName("hc_txt")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(60, 400, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.tc_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.tc_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.tc_txt.setObjectName("tc_txt")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(60, 460, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.MCH_txt = QtWidgets.QLineEdit(self.groupBox_7)
        self.MCH_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.MCH_txt.setObjectName("MCH_txt")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(60, 520, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.MCHC_txt = QtWidgets.QLineEdit(self.groupBox_8)
        self.MCHC_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.MCHC_txt.setObjectName("MCHC_txt")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(60, 130, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gender_txt = QtWidgets.QLineEdit(self.groupBox_10)
        self.gender_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.gender_txt.setObjectName("gender_txt")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(60, 60, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.age_txt = QtWidgets.QLineEdit(self.groupBox_9)
        self.age_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.age_txt.setObjectName("age_txt")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(190, 700, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(60, 580, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.MCV_txt = QtWidgets.QLineEdit(self.groupBox_11)
        self.groupBox_12 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_12.setGeometry(QtCore.QRect(60, 640, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.bc_txt = QtWidgets.QLineEdit(self.groupBox_12)
        self.bc_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.bc_txt.setObjectName("bc_txt")
        self.MCV_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.MCV_txt.setObjectName("MCV_txt")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # xử lí button lưu - save_button
        self.save_button.clicked.connect(self.predict_and_save_farmer_result)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Medical_Certi", "Medical Certificate Screen"))
        self.medical_certi.setText(_translate("Medical_Certi", "Dự đoán"))
        self.groupBox_3.setTitle(_translate("Medical_Certi", "Dung tích hồng cầu"))
        self.groupBox_4.setTitle(_translate("Medical_Certi", "Huyết sắc tố"))
        self.groupBox_5.setTitle(_translate("Medical_Certi", "Hồng cầu"))
        self.groupBox_6.setTitle(_translate("Medical_Certi", "Tiểu cầu"))
        self.groupBox_7.setTitle(_translate("Medical_Certi", "Lượng huyết sắc tố trung bình hồng cầu"))
        self.groupBox_8.setTitle(_translate("Medical_Certi", "Nồng độ huyết sắc tố trung bình hồng cầu"))
        self.groupBox_10.setTitle(_translate("Medical_Certi", "Giới tính"))
        self.groupBox_9.setTitle(_translate("Medical_Certi", "Tuổi"))
        self.save_button.setText(_translate("Medical_Certi", "Lưu"))
        self.groupBox_11.setTitle(_translate("Medical_Certi", "Thể tích hồng cầu trung bình"))
        self.groupBox_12.setTitle(_translate("Medical_Certi", "Bạch cầu"))

    # lưu lại -> hiện ra dự đoán nhập bệnh hay ko
    def predict_and_save_farmer_result(self):

        try:

            # lấy ra các trường
            data_predict = [self.dthc_txt.text(), self.hst_txt.text(), self.hc_txt.text(), self.tc_txt.text(),self.bc_txt.text(),
                            self.MCH_txt.text(), self.MCHC_txt.text(), self.MCV_txt.text(), self.age_txt.text(),self.gender_txt.text()]
            gender_male=['Male','male','boy','Boy','MALE','BOY','nam','Nam']

            if data_predict[len(data_predict)-1] in gender_male:
                data_predict[len(data_predict)-1] = '1'
                print('boy')
            else:
                data_predict[len(data_predict)-1] = '0'
                print('girl')

            for i in data_predict:

                if not i:
                    error_dialog = QMessageBox(QMessageBox.Critical, "Field Error",
                                               'Điền đủ thông tin vào ông cháu', QMessageBox.Close)
                    error_dialog.setStyleSheet("width: 300px")
                    error_dialog.exec()
                    return

                if i<0 or i>1300:
                    QMessageBox.information(self, 'Xin mời nhập lại', 'Thông tin không này điêu', QMessageBox.Close)
                    return

            data_predict = [int(x) for x in data_predict]
            if data_predict:
                #[335 109 344  58 275 317 325 974  99   0]
                data_predict = np.array(data_predict).reshape(1,-1)
                machine_predict = machine_build.model.predict(data_predict)
                if machine_predict == 1:
                    QMessageBox.information(self, 'Thông báo nhập viện', 'Cho nhập viện đê', QMessageBox.Close)
                else:
                    QMessageBox.information(self, 'Thông báo nhập viện', 'Bệnh nhân không cần nhập viện',
                                            QMessageBox.Close)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Medical_Certi()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())