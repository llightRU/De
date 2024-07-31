from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox
import sys
import validate as v
import json
import common as cm
import Machine

class Ui_Medical_Certi(QMainWindow):
    def __init__(self,farmer_id=0,parent=None):
        super(Ui_Medical_Certi,self).__init__(parent)
        self.farmer_id = farmer_id
        filename = r'C:\Users\Gli\Desktop\final\config\config.json'
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
        self.resize(500, 720)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.medical_certi = QtWidgets.QLabel(self.centralwidget)
        self.medical_certi.setGeometry(QtCore.QRect(190, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.medical_certi.setFont(font)
        self.medical_certi.setObjectName("medical_certi")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 30, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.id_name_combobox = QtWidgets.QComboBox(self.groupBox)
        self.id_name_combobox.setGeometry(QtCore.QRect(60, 20, 281, 31))
        self.id_name_combobox.setObjectName("id_name_combobox")
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
        self.groupBox_10.setGeometry(QtCore.QRect(60, 160, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gender_txt = QtWidgets.QLineEdit(self.groupBox_10)
        self.gender_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.gender_txt.setObjectName("gender_txt")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(60, 100, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.age_txt = QtWidgets.QLineEdit(self.groupBox_9)
        self.age_txt.setGeometry(QtCore.QRect(60, 20, 281, 21))
        self.age_txt.setObjectName("age_txt")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(200, 650, 91, 31))
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

        #initial data

        if self.farmer_id!=0:
            self.initial_data()
        else:
            self.initial_comboBox()

        # render UI
        self.retranslateUi()

        # xử lí button lưu - save_button
        self.save_button.clicked.connect(self.predict_and_save_farmer_result)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Medical_Certi", "Medical Certificate Screen"))
        self.medical_certi.setText(_translate("Medical_Certi", "Giấy khám"))
        self.groupBox.setTitle(_translate("Medical_Certi", "ID bệnh nhân"))
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

    #initial data
    def initial_comboBox(self):
        data = cm.show_table(self.cnx.cursor(),'farmer')
        if data:
            search = []
            for i in range(len(data)):
                search.append(str(data[i][0])+' - '+str(data[i][1]))

            self.id_name_combobox.setEditable(True)
            self.id_name_combobox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
            self.id_name_combobox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
            self.id_name_combobox.addItems(search)

    def initial_data(self):
        try:
            farmer = cm.get_farmer_by_id(self.cnx.cursor(),self.farmer_id)
            l = ["" + str(self.farmer_id) + " - " + farmer[1], '1']
            self.id_name_combobox.addItems(l)
            self.id_name_combobox.setCurrentText(""+str(self.farmer_id)+" - "+farmer[1])
            self.id_name_combobox.setEnabled(False)
            age = datetime.today().year - farmer[3].year
            self.age_txt.setText(str(age))
            self.age_txt.setEnabled(False)
            sex = 'Female'
            if farmer[-1]==1:
                sex = 'Male'
            self.gender_txt.setText(sex)
            self.gender_txt.setEnabled(False)
            health = cm.check_health_from_farmerId(self.cnx.cursor(),self.farmer_id)
            health = [str(s) for s in health]
            self.dthc_txt.setText(health[3])
            self.hst_txt.setText(health[4])
            self.hc_txt.setText(health[5])
            self.tc_txt.setText(health[6])
            self.MCH_txt.setText(health[7])
            self.MCHC_txt.setText(health[8])
            self.MCV_txt.setText(health[9])

        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)


    # lưu lại -> hiện ra dự đoán nhập bệnh hay ko
    def predict_and_save_farmer_result(self):
        # self.farmer_id
        data_predict=[self.dthc_txt.text(),self.hst_txt.text(),self.hc_txt.text(),self.tc_txt.text(),self.MCH_txt.text(),self.MCHC_txt.text(),self.MCV_txt.text(),self.age_txt.text(),0]
        if data_predict:
            machine_predict = Machine.treatment_classification(data_predict)
            if machine_predict==1:
                QMessageBox.information(self, 'Thông báo nhập viện', 'Cho nhập viện đi ông cháu',QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Thông báo nhập viện', 'Bệnh nhân ngoài vòng kiểm soát', QMessageBox.Close)
        else:
            error_dialog = QMessageBox(QMessageBox.Critical, "Field Error",
                                       'Điền đủ thông tin vào ông cháu', QMessageBox.Close)
            error_dialog.setStyleSheet("width: 300px")
            error_dialog.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Medical_Certi(1)
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())