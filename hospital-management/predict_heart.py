import os
import sys

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import heart_predict_machine
class Ui_MainWindow(QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 20, 181, 61))
        self.groupBox.setObjectName("groupBox")
        self.age_txt = QtWidgets.QLineEdit(self.groupBox)
        self.age_txt.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.age_txt.setObjectName("age_txt")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 20, 201, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gioi_tinh_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.gioi_tinh_txt.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.gioi_tinh_txt.setObjectName("gioi_tinh_txt")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 110, 201, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.huyet_ap_txt = QtWidgets.QLineEdit(self.groupBox_4)
        self.huyet_ap_txt.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.huyet_ap_txt.setObjectName("huyet_ap_txt")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(60, 200, 181, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.choles_txt = QtWidgets.QLineEdit(self.groupBox_5)
        self.choles_txt.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.choles_txt.setObjectName("choles_txt")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(380, 200, 201, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.luong_duong_txt = QtWidgets.QLineEdit(self.groupBox_6)
        self.luong_duong_txt.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.luong_duong_txt.setObjectName("luong_duong_txt")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(180, 280, 161, 61))
        self.groupBox_7.setObjectName("groupBox_7")
        self.dien_tam_do_txt = QtWidgets.QLineEdit(self.groupBox_7)
        self.dien_tam_do_txt.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.dien_tam_do_txt.setObjectName("dien_tam_do_txt")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(380, 290, 201, 61))
        self.groupBox_8.setObjectName("groupBox_8")
        self.nhip_tim_txt = QtWidgets.QLineEdit(self.groupBox_8)
        self.nhip_tim_txt.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.nhip_tim_txt.setObjectName("nhip_tim_txt")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(150, 380, 181, 61))
        self.groupBox_9.setObjectName("groupBox_9")
        self.dau_tuc_txt = QtWidgets.QLineEdit(self.groupBox_9)
        self.dau_tuc_txt.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.dau_tuc_txt.setObjectName("dau_tuc_txt")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(380, 380, 201, 61))
        self.groupBox_10.setObjectName("groupBox_10")
        self.stress_txt = QtWidgets.QLineEdit(self.groupBox_10)
        self.stress_txt.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.stress_txt.setObjectName("stress_txt")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(380, 470, 201, 61))
        self.groupBox_11.setObjectName("groupBox_11")
        self.so_luong_mach_chinh_txt = QtWidgets.QLineEdit(self.groupBox_11)
        self.so_luong_mach_chinh_txt.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.so_luong_mach_chinh_txt.setObjectName("so_luong_mach_chinh_txt")
        self.groupBox_12 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_12.setGeometry(QtCore.QRect(150, 470, 161, 61))
        self.groupBox_12.setObjectName("groupBox_12")
        self.slope_txt = QtWidgets.QLineEdit(self.groupBox_12)
        self.slope_txt.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.slope_txt.setObjectName("slope_txt")
        self.groupBox_13 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_13.setGeometry(QtCore.QRect(180, 560, 161, 61))
        self.groupBox_13.setObjectName("groupBox_13")
        self.stress_thalium_txt = QtWidgets.QLineEdit(self.groupBox_13)
        self.stress_thalium_txt.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.stress_thalium_txt.setObjectName("stress_thalium_txt")
        self.predict_button = QtWidgets.QPushButton(self.centralwidget)
        self.predict_button.setGeometry(QtCore.QRect(430, 580, 101, 31))
        self.predict_button.setObjectName("predict_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 121, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 110, 161, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tuc_nguc_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.tuc_nguc_txt.setGeometry(QtCore.QRect(20, 30, 113, 22))
        self.tuc_nguc_txt.setObjectName("tuc_nguc_txt")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 30, 41, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 50, 51, 21))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 300, 151, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 320, 161, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 280, 101, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 390, 61, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 410, 61, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 470, 71, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 490, 131, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 510, 131, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 560, 71, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(10, 580, 111, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 600, 161, 21))
        self.label_18.setObjectName("label_18")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        # tạo button dự đoán nhiều
        self.predict_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.predict_button_2.setGeometry(QtCore.QRect(430, 620, 101, 31))
        self.predict_button_2.setObjectName("predict_button_2")

        # button dự đoán
        self.predict_button.clicked.connect(self.predict_result)
        # button dự đoán nhiều
        self.predict_button_2.clicked.connect(self.predict_list_import_data)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Dự đoán bệnh tim"))
        self.groupBox.setTitle(_translate("MainWindow", "Tuổi"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Giới tính"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Huyết áp"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Cholestoral trong máu"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Lượng đường trong máu"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Điện tâm đồ"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Nhịp tim"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Đau tức ngực khi tập thể dục"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Stress"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Số lượng mạch chính"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Slope"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Stress Thalium"))
        self.predict_button.setText(_translate("MainWindow", "Dự đoán"))
        self.label.setText(_translate("MainWindow", "0. Đau điển hình"))
        self.label_2.setText(_translate("MainWindow", "1. Đau ko điển hình"))
        self.label_3.setText(_translate("MainWindow", "2. Đau ko lq đến tim"))
        self.label_4.setText(_translate("MainWindow", "3. Ko có triệu chứng"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tức ngực"))
        self.label_5.setText(_translate("MainWindow", "0. Nữ"))
        self.label_6.setText(_translate("MainWindow", "1. Nam"))
        self.label_8.setText(_translate("MainWindow", "1. Sóng ST-T bất thường"))
        self.label_9.setText(_translate("MainWindow", "2. Phì đại thất trái (có/chắc)"))
        self.label_10.setText(_translate("MainWindow", "0. Ko đáng lưu ý"))
        self.label_11.setText(_translate("MainWindow", "0. Không"))
        self.label_12.setText(_translate("MainWindow", "1. Có"))
        self.label_13.setText(_translate("MainWindow", "0: Upsloping"))
        self.label_14.setText(_translate("MainWindow", "1: Tim khỏe điển hình"))
        self.label_15.setText(_translate("MainWindow", "2. Dấu hiệu ko khỏe"))
        self.label_16.setText(_translate("MainWindow", "1,3: normal"))
        self.label_17.setText(_translate("MainWindow", "6. Từng yếu giờ ổn"))
        self.label_18.setText(_translate("MainWindow", "7. Khiếm khuyết can reverse"))
        self.predict_button_2.setText(_translate("MainWindow", "Dự đoán nhiều"))

    # dự đoán bệnh tim
    def predict_result(self):

        age,sex,cp,trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal = \
            (int(self.age_txt.text()),int(self.gioi_tinh_txt.text()),int(self.tuc_nguc_txt.text()),
             int(self.huyet_ap_txt.text()),int(self.choles_txt.text()),int(self.luong_duong_txt.text()),
             int(self.dien_tam_do_txt.text()),int(self.nhip_tim_txt.text()),int(self.dau_tuc_txt.text()),
             int(self.stress_txt.text()),int(self.slope_txt.text()),int(self.so_luong_mach_chinh_txt.text()),
             int(self.stress_thalium_txt.text()))
        # list_data = [self.age_txt,self.gioi_tinh_txt,self.tuc_nguc_txt,self.huyet_ap_txt,self.choles_txt,
        #              self.luong_duong_txt,self.dien_tam_do_txt,self.nhip_tim_txt,self.dau_tuc_txt,self.stress_txt,
        #              self.slope_txt,self.so_luong_mach_chinh_txt,self.stress_thalium_txt]
        self.predict_heart = heart_predict_machine
        target = self.predict_heart.predict_Heart_Disease(age,sex,cp,trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        accuracy = self.predict_heart.cv_recall
        print(target,accuracy)
        s=''
        if target==1:
           s='Bị bệnh tim'
        else:
            s='Ko bị tim'
        error_dialog = QMessageBox(QMessageBox.Critical, "Field Error",
                                   'Kết quả dự đoán: {} với tỉ lệ chính xác: {}'.format(s,accuracy), QMessageBox.Close)
        error_dialog.setStyleSheet("width: 300px")
        error_dialog.exec()


    # mở file
    def open_dialog_file(item, file_type="All Files (*)"):
        QFileDialog = QtWidgets.QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(QFileDialog, "Select File", os.path.expanduser('./get_report'),file_type, options=options)
        return fileName

    def predict_list_import_data(self):

        try:

            file = self.open_dialog_file()
            df = pd.read_excel(file)
            df = df.drop('target', axis=1)
            data_list = df.values.tolist()
            self.predict_list_heart = heart_predict_machine
            label_list = []

            for i in data_list:

                age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal=i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]
                label = self.predict_list_heart.predict_Heart_Disease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
                label_list.append(label)

            print(label_list)
            # ghi dữ liệu
            df = pd.read_excel(file)
            target_series = pd.Series(label_list)
            df['target'] = target_series
            df.to_excel(file, index=False)
            QMessageBox.information(self, 'Successfull predict to list',
                                    "Predict success, open your {} to see predict result".format(file),
                                    QMessageBox.Close)

        except Exception as e:

            print(e)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  # manages the GUI application’s control flow and main settings, It handles widget specific initialization, finalization,It initializes the application with the user’s desktop settings
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())