import os
import sys

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QTableWidgetItem, QApplication, QProgressBar, QMessageBox
import heart_predict_machine
import predict_heart
import Machine
import view
import select_model

class Ui_MainWindow(QMainWindow):

    def __init__(self,parent=None):

        super(QMainWindow,self).__init__(parent)

    def setupUi(self):

        self.setObjectName("MainWindow")
        self.resize(800, 610)
        self.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.heart_predict_table = QtWidgets.QTableWidget(self.centralwidget)
        self.heart_predict_table.setGeometry(QtCore.QRect(110, 40, 530, 410))
        self.heart_predict_table.setObjectName("heart_predict_table")
        self.heart_predict_table.setColumnCount(14)
        self.heart_predict_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.heart_predict_table.setHorizontalHeaderItem(13, item)
        self.heart_predict_table.horizontalHeader().setDefaultSectionSize(60)
        self.train_dead_button = QtWidgets.QPushButton(self.centralwidget)
        self.train_dead_button.setGeometry(QtCore.QRect(650, 90, 93, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.train_dead_button.setFont(font)
        self.train_dead_button.setAutoDefault(False)
        self.train_dead_button.setFlat(False)
        self.train_dead_button.setObjectName("train_dead_button")
        self.heart_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.heart_group_box.setGeometry(QtCore.QRect(40, 470, 331, 61))
        self.heart_group_box.setObjectName("heart_group_box")
        self.heart_group_box_2 = QtWidgets.QGroupBox(self.heart_group_box)
        self.heart_group_box_2.setGeometry(QtCore.QRect(0, 0, 331, 61))
        self.heart_group_box_2.setObjectName("heart_group_box_2")
        self.dead_combobox = QtWidgets.QComboBox(self.heart_group_box_2)
        self.dead_combobox.setGeometry(QtCore.QRect(30, 30, 191, 22))
        self.dead_combobox.setObjectName("dead_combobox")

        self.dead_view_button = QtWidgets.QPushButton(self.heart_group_box_2)
        self.dead_view_button.setGeometry(QtCore.QRect(230, 26, 93, 28))
        self.dead_view_button.setObjectName("dead_view_button")

        self.heart_view_button = QtWidgets.QPushButton(self.heart_group_box_2)
        self.heart_view_button.setGeometry(QtCore.QRect(230, 26, 93, 28))
        self.heart_view_button.setObjectName("heart_view_button")

        self.heart_combobox = QtWidgets.QComboBox(self.heart_group_box_2)
        self.heart_combobox.setGeometry(QtCore.QRect(30, 30, 191, 22))
        self.heart_combobox.setObjectName("heart_combobox")


        # add item combobox
        self.heart_combobox.addItem("")
        self.heart_combobox.addItem("")
        self.heart_combobox.addItem("")
        self.heart_combobox.addItem("")
        self.heart_combobox.addItem("")
        self.heart_combobox.addItem("")

        self.predict_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.predict_group_box.setGeometry(QtCore.QRect(440, 480, 301, 61))
        self.predict_group_box.setObjectName("predict_group_box")
        self.heart_predict_button = QtWidgets.QPushButton(self.predict_group_box)
        self.heart_predict_button.setGeometry(QtCore.QRect(120, 20, 93, 28))
        self.heart_predict_button.setObjectName("heart_predict_button")
        self.dead_predict_button = QtWidgets.QPushButton(self.predict_group_box)
        self.dead_predict_button.setGeometry(QtCore.QRect(120, 20, 93, 28))
        self.dead_predict_button.setObjectName("dead_predict_button")
        self.import_dead_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_dead_button.setGeometry(QtCore.QRect(110, 10, 71, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.import_dead_button.setFont(font)
        self.import_dead_button.setAutoDefault(False)
        self.import_dead_button.setFlat(False)
        self.import_dead_button.setObjectName("import_dead_button")
        self.train_heart_button = QtWidgets.QPushButton(self.centralwidget)
        self.train_heart_button.setGeometry(QtCore.QRect(650, 90, 93, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.train_heart_button.setFont(font)
        self.train_heart_button.setAutoDefault(False)
        self.train_heart_button.setFlat(False)
        self.train_heart_button.setObjectName("train_heart_button")
        self.import_hear_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_hear_button.setGeometry(QtCore.QRect(110, 10, 71, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.import_hear_button.setFont(font)
        self.import_hear_button.setAutoDefault(False)
        self.import_hear_button.setFlat(False)
        self.import_hear_button.setObjectName("import_hear_button")
        self.dead_predict_table = QtWidgets.QTableWidget(self.centralwidget)
        self.dead_predict_table.setGeometry(QtCore.QRect(110, 40, 530, 410))
        self.dead_predict_table.setObjectName("dead_predict_table")
        self.dead_predict_table.setColumnCount(13)
        self.dead_predict_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.dead_predict_table.setHorizontalHeaderItem(12, item)
        self.dead_predict_table.horizontalHeader().setDefaultSectionSize(60)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuDead = QtWidgets.QMenu(self.menubar)
        self.menuDead.setObjectName("menuDead")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionHeart = QtWidgets.QAction(self)
        self.actionHeart.setObjectName("actionHeart")
        self.menuDead.addAction(self.actionHeart)
        self.menubar.addAction(self.menuDead.menuAction())

        # show các chức năng heart predict
        self.heart_combobox.hide()
        self.heart_view_button.hide()
        self.heart_predict_table.hide()
        self.heart_predict_button.hide()
        self.import_hear_button.hide()
        self.train_heart_button.hide()

        # self.dead_combobox.setEditable(True)
        self.dead_combobox.addItem("")
        self.dead_combobox.addItem("")
        self.dead_combobox.addItem("")
        self.dead_combobox.addItem("")

        # chọn button train model
        self.train_heart_button.clicked.connect(self.train_model_process)

        # init data
        file_name = './get_report/heart-disease.csv'
        self.init_data(file_name)

        #render UI
        self.retranslateUi()

        # xử lí khi chuyển màn hình dự đoán tim
        self.actionHeart.triggered.connect(self.predict_heart)

        # Tan san
        self.heart_predict_table.hide()
        self.import_hear_button.hide()
        self.init_data_1('./get_report/dataset.csv', 500)
        # xử lý hiện ra biểu đồ
        self.dead_view_button.clicked.connect(self.view)
        # xử lý import file
        self.import_dead_button.clicked.connect(self.import_data_from_file)

        # xử lý button train dead
        self.train_dead_button.clicked.connect(self.train_dead)

        # xử lý button dự đoán - predict
        self.dead_predict_button.clicked.connect(self.predict_dead)
    def init_data(self,file_name):

        # đọc data
        df = pd.read_csv(file_name)

        # lấy số lượng hàng và cột
        num_rows = len(df.index)
        num_cols = len(df.columns)

        # thiết lập tableWidget với số lượng hàng và cột tương ứng với dataframe
        self.heart_predict_table.setRowCount(num_rows)
        self.heart_predict_table.setColumnCount(num_cols)

        # đặt tên cho các cột trong tableWidget
        self.heart_predict_table.setHorizontalHeaderLabels(df.columns)

        # lặp qua từng hàng và cột của dataframe
        for row in range(num_rows):
            for col in range(num_cols):
                # lấy giá trị của từng ô trong dataframe
                cell_value = df.iloc[row, col]
                # chuyển giá trị sang dạng chuỗi
                cell_value_str = str(cell_value)
                # tạo QTableWidgetItem từ giá trị chuỗi
                table_item = QTableWidgetItem(cell_value_str)
                # đặt QTableWidgetItem vào tableWidget
                self.heart_predict_table.setItem(row, col, table_item)

        # button import nhieu
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.dead_predict_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "age"))
        item = self.dead_predict_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "anaemia"))
        item = self.dead_predict_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "creatinine_phosphokinase"))
        item = self.dead_predict_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "diabetes"))
        item = self.dead_predict_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ejection_fraction"))
        item = self.dead_predict_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "high_blood_pressure"))
        item = self.dead_predict_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "platelets"))
        item = self.dead_predict_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "serum_creatinine"))
        item = self.dead_predict_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "serum_sodium"))
        item = self.dead_predict_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "sex"))
        item = self.dead_predict_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "smoking"))
        item = self.dead_predict_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "time"))
        item = self.dead_predict_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "DEATH_EVENT"))
        self.train_dead_button.setText(_translate("MainWindow", "Train Model"))
        self.heart_group_box.setTitle(_translate("MainWindow", "Data Analysis"))
        self.heart_view_button.setText(_translate("MainWindow", "view"))
        self.heart_group_box_2.setTitle(_translate("MainWindow", "Data Analysis"))
        self.dead_view_button.setText(_translate("MainWindow", "view"))
        self.predict_group_box.setTitle(_translate("MainWindow", "In/Out care patient"))
        self.heart_predict_button.setText(_translate("MainWindow", "Prediction"))
        self.dead_predict_button.setText(_translate("MainWindow", "Prediction"))
        self.import_dead_button.setText(_translate("MainWindow", "import"))
        self.train_heart_button.setText(_translate("MainWindow", "Train Model"))
        self.import_hear_button.setText(_translate("MainWindow", "import"))
        item = self.heart_predict_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "age"))
        item = self.heart_predict_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "giới tính"))
        item = self.heart_predict_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "tức ngực"))
        item = self.heart_predict_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "huyết áp"))
        item = self.heart_predict_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "cholestoral trong máu"))
        item = self.heart_predict_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "lượng đường trong máu"))
        item = self.heart_predict_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "điện tâm đồ"))
        item = self.heart_predict_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "nhịp tim"))
        item = self.heart_predict_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "đau thắt ngực khi tập thể dục"))
        item = self.heart_predict_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "stress"))
        item = self.heart_predict_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "slope"))
        item = self.heart_predict_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "số lượng các mạch chính"))
        item = self.heart_predict_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "stress thalium"))
        item = self.heart_predict_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "target"))
        self.menuDead.setTitle(_translate("MainWindow", "Dead"))
        self.actionHeart.setText(_translate("MainWindow", "Heart"))
        # combobox
        self.heart_combobox.setItemText(0, _translate("MainWindow",'Number of nah and heart disease'))
        self.heart_combobox.setItemText(1, _translate("MainWindow",'Heart disease rates by sex'))
        self.heart_combobox.setItemText(2, _translate("MainWindow",'Disease by age and maximum rhythm'))
        self.heart_combobox.setItemText(3, _translate("MainWindow",'Age'))
        self.heart_combobox.setItemText(4, _translate("MainWindow",'Visualization'))
        self.heart_combobox.setItemText(5, _translate("MainWindow",'Frequency of heart disease by degree of chest pain'))
        # combobox dead
        self.dead_combobox.setItemText(0, _translate("MainWindow", "analysis of hospital_death"))
        self.dead_combobox.setItemText(1, _translate("MainWindow", "analysis of gender"))
        self.dead_combobox.setItemText(2, _translate("MainWindow", "analysis of icu_stay_type"))
        self.dead_combobox.setItemText(3, _translate("MainWindow", "analysis of apache_2_bodysystem"))

    # mở các chức năng của predict heart
    def predict_heart(self):

        # Đổi tên
        _translate = QtCore.QCoreApplication.translate
        self.menuDead.setTitle(_translate("MainWindow", "Heart"))
        # self.actionHeart.setText(_translate("MainWindow", "Dead"))

        try:

            # ẩn các chức năng dead predict
            self.import_dead_button.hide()
            self.dead_predict_table.hide()
            self.dead_predict_button.hide()
            self.dead_view_button.hide()
            self.dead_combobox.hide()
            self.train_dead_button.hide()

            # show các chức năng heart predict
            self.heart_combobox.show()
            self.heart_view_button.show()
            self.heart_predict_table.show()
            self.heart_predict_button.show()
            self.import_hear_button.show()
            self.train_heart_button.show()

            # chọn view đồ thị
            self.heart_view_button.clicked.connect(self.view_plot)

            # chọn import button
            self.import_hear_button.clicked.connect(self.import_data)

            # chọn button dự đoán
            self.heart_predict_button.clicked.connect(self.open_predict_screen)

        except Exception as e:

            print(e)

    def view_plot(self, text):

        try:
            # lấy giá trị combobox
            plot_name_select = self.heart_combobox.currentText()
            print(plot_name_select)

            self.show_plot = heart_predict_machine.Show_Plot()

            if plot_name_select == 'Number of nah and heart disease':
                self.show_plot.volumn_heart_disease()
                self.show_plot.show()
            elif plot_name_select == 'Heart disease rates by sex':
                self.show_plot.sex_heart_percent()
                self.show_plot.show()
            elif plot_name_select == 'Disease by age and maximum rhythm':
                self.show_plot.age_max_heart_rate()
                self.show_plot.show()
            elif plot_name_select == 'Age':
                self.show_plot.age_plot()
                self.show_plot.show()
            elif plot_name_select == 'Visualization':
                self.show_plot.visualization()
                self.show_plot.show()
            elif plot_name_select == 'Frequency of heart disease by degree of chest pain':
                self.show_plot.heart_disease_frequency()
                self.show_plot.show()

        except Exception as e:

            print(e)

    # mở file
    def open_dialog_file(item, file_type="All Files (*)"):
        QFileDialog = QtWidgets.QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(QFileDialog, "Select File", os.path.expanduser('./get_report'),file_type, options=options)
        return fileName

    # import data from file
    def import_data(self):

        try:

            # read file
            file_name = self.open_dialog_file()

            # init lại data
            # self.heart_predict_table.setRowCount(0)
            self.init_data(file_name)

        except Exception as e:

            print(e)

    def train_model_process(self):

        try:

            self.progress_bar = QProgressBar(self)
            self.progress_bar.setGeometry(70, 240, 690, 28)
            self.progress_bar.setMaximum(100)
            self.progress_bar.setMinimum(0)
            self.progress_bar.show()


            for i in range(101):
                self.progress_bar.setValue(i)
                QApplication.processEvents()
                import time
                time.sleep(0.03)

            self.progress_bar.show()

            # mở biểu đồ độ chính xác
            self.show_plot = heart_predict_machine.Show_Plot()
            self.show_plot.compare_model()
            self.show_plot.show()

            self.progress_bar.hide()

        except Exception as e:
            print(e)

    # mở màn hình chọn model
    def open_predict_screen(self):

        self.open_select_model = select_model.Ui_MainWindow()
        self.open_select_model.setupUi()
        self.open_select_model.show()
        
        # # mở cửa sổ dự đoán
        # self.open_predict_screen = predict_heart.Ui_MainWindow()
        # self.open_predict_screen.setupUi()
        # self.open_predict_screen.show()

        # biểu đồ thống kê
    def dead_plot(self):
            try:
                file_name = './get_report/dataset.csv'
                self.open_plot = Machine.Hospital_dead(file_name)
            except Exception as e:
                print(e)

    def dead_gender(self):
            try:
                file_name = './get_report/dataset.csv'
                self.open_plot = Machine.Hospital_dead_gender(file_name)
            except Exception as e:
                print(e)

    def dead_icu(self):
            try:
                file_name = './get_report/dataset.csv'
                self.open_plot = Machine.Hospital_dead_icu(file_name)
            except Exception as e:
                print(e)

    def dead_apache(self):
            try:
                file_name = './get_report/dataset.csv'
                self.open_plot = Machine.Hospital_dead_apache(file_name)
            except Exception as e:
                print(e)

    def view(self):
        try:
            name = self.dead_combobox.currentText()
            if name == 'analysis of hospital_death':
                self.dead_plot()
            elif name == 'analysis of gender':
                self.dead_gender()
            elif name == 'analysis of icu_stay_type':
                self.dead_icu()
            else:
                self.dead_apache()

        except Exception as e:
            print(e)

        # import file excel vào database
    def import_data_from_file(self):
            try:
                # read file
                file_name = self.open_dialog_file()
                self.init_data_1(file_name, 1000)
            except Exception as e:
                print(e)

    def init_data_1(self, filename, numrow):

        # đọc data
        df = pd.read_csv(filename)

        # lấy số lượng hàng và cột
        # num_rows = len(df.index)
        num_rows = numrow
        num_cols = len(df.columns)


        # thiết lập tableWidget với số lượng hàng và cột tương ứng với dataframe
        self.dead_predict_table.setRowCount(num_rows)
        self.dead_predict_table.setColumnCount(num_cols)

        # đặt tên cho các cột trong tableWidget
        self.dead_predict_table.setHorizontalHeaderLabels(df.columns)

        # lặp qua từng hàng và cột của dataframe
        for row in range(num_rows):
            for col in range(num_cols):
                # lấy giá trị của từng ô trong dataframe
                cell_value = df.iloc[row, col]
                # chuyển giá trị sang dạng chuỗi
                cell_value_str = str(cell_value)
                # tạo QTableWidgetItem từ giá trị chuỗi
                table_item = QTableWidgetItem(cell_value_str)
                # đặt QTableWidgetItem vào tableWidget
                self.dead_predict_table.setItem(row, col, table_item)


    def train_dead(self):
        try:

            self.progress_bar = QProgressBar(self)
            self.progress_bar.setGeometry(70, 240, 690, 28)
            self.progress_bar.setMaximum(100)
            self.progress_bar.setMinimum(0)
            self.progress_bar.show()


            for i in range(101):
                self.progress_bar.setValue(i)
                QApplication.processEvents()
                import time
                time.sleep(0.03)

            self.progress_bar.show()
            self.progress_bar.hide()

            # mở biểu đồ độ chính xác
            accuracy,new_label = Machine.dead_predict('./get_report/dataset.csv')
            error_dialog = QMessageBox(QMessageBox.Critical, "Độ chính xác",
                                       'Mô hình K-NN bạn chọn có độ chính xác {}'.format(accuracy), QMessageBox.Close)
            error_dialog.setStyleSheet("width: 400px")
            error_dialog.exec()
            self.progress_bar.hide()

        except Exception as e:
            print(e)

    def predict_dead(self):

        try:

            new_data, new_label = Machine.dead_predict_pass_data('./get_report/dataset.csv')
            label=''
            if new_data ==1:
                label='Tử vong'
            else:
                label='Sống'
            error_dialog = QMessageBox(QMessageBox.Critical, "Giấy báo tử",
                                       '{} được dự đoán là: {}'.format(new_data,label), QMessageBox.Close)
            error_dialog.setStyleSheet("width: 400px,height: 500px")
            error_dialog.exec()
            self.progress_bar.hide()

        except Exception as e:

            print(e)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  # manages the GUI application’s control flow and main settings, It handles widget specific initialization, finalization,It initializes the application with the user’s desktop settings
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())