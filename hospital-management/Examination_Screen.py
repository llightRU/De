from datetime import datetime
import Predict_InOutPatient
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Medical_Certi_Screen as mcs
import validate as v
import json
import common as cm
import pandas as pd
import Machine
import view

class Ui_Examination(QMainWindow):
    def __init__(self, staff_id=4,parent=None):
        super(Ui_Examination, self).__init__(parent)
        filename = './database_config.json'
        self.staff_id = staff_id
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
        self.setObjectName("Examination")
        self.resize(800, 610)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.health_table = QtWidgets.QTableWidget(self.centralwidget)
        self.health_table.setGeometry(QtCore.QRect(110, 40, 530, 410))
        self.health_table.setObjectName("health_table")
        self.health_table.setColumnCount(14)
        self.health_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(10, item)
        # thêm column bạch cầu
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(11, item)
        # done
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.health_table.setHorizontalHeaderItem(13, item)
        self.health_table.horizontalHeader().setDefaultSectionSize(97)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setGeometry(QtCore.QRect(670, 170, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_button.setFont(font)
        self.export_button.setObjectName("export_button")
        self.add_new_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_button.setGeometry(QtCore.QRect(670, 100, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_new_button.setFont(font)
        self.add_new_button.setObjectName("add_new_button")
        self.search_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.search_txt.setGeometry(QtCore.QRect(280, 10, 278, 31))
        self.search_txt.setObjectName("search_txt")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(570, 10, 71, 31))
        self.search_button.setObjectName("search_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 460, 461, 16))
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        # thêm UI
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(110, 10, 71, 31))
        font = QtGui.QFont()
        font.setKerning(True)
        self.import_button.setFont(font)
        self.import_button.setAutoDefault(False)
        self.import_button.setFlat(False)
        self.import_button.setObjectName("import_button")
        self.predict_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.predict_group_box.setGeometry(QtCore.QRect(440, 500, 301, 71))
        self.predict_group_box.setObjectName("predict_group_box")
        self.predict_button = QtWidgets.QPushButton(self.predict_group_box)
        self.predict_button.setGeometry(QtCore.QRect(120, 25, 93, 28))
        self.predict_button.setObjectName("predict_button")
        self.data_analysis_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.data_analysis_group_box.setGeometry(QtCore.QRect(40, 500, 331, 71))
        self.data_analysis_group_box.setObjectName("data_analysis_group_box")
        self.plot_combobox = QtWidgets.QComboBox(self.data_analysis_group_box)
        self.plot_combobox.setGeometry(QtCore.QRect(30, 30, 191, 22))
        self.plot_combobox.setObjectName("plot_combobox")
        self.view_button = QtWidgets.QPushButton(self.data_analysis_group_box)
        self.view_button.setGeometry(QtCore.QRect(230, 26, 93, 28))
        self.view_button.setObjectName("view_button")
        self.train_button = QtWidgets.QPushButton(self.centralwidget)
        self.train_button.setGeometry(QtCore.QRect(670, 250, 93, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        font.setPointSize(9)
        self.train_button.setFont(font)
        self.train_button.setAutoDefault(False)
        self.train_button.setFlat(False)
        self.train_button.setObjectName("train_button")

        # start code

        # initial data
        self.initial_table()

        list_view = ['correlation', 'age plot', 'thrombocyte plot', 'median plot', 'treatment pie']
        self.plot_combobox.setEditable(True)
        self.plot_combobox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.plot_combobox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.plot_combobox.addItems(list_view)

        # button active
        self.search_button.clicked.connect(self.search_button_active)
        self.add_new_button.clicked.connect(self.add_new_button_active)
        self.export_button.clicked.connect(self.export_button_active)
        self.import_button.clicked.connect(self.import_button_active)
        # predict button
        self.predict_button.clicked.connect(self.predict_in_or_out_patient)
        self.view_button.clicked.connect(self.view_button_active)

        self.train_button.hide()
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Examination", "Examination Screen"))
        item = self.health_table.horizontalHeaderItem(0)
        item.setText(_translate("Examination", "Patient_id"))
        item = self.health_table.horizontalHeaderItem(1)
        item.setText(_translate("Examination", "Patient_name"))
        item = self.health_table.horizontalHeaderItem(2)
        item.setText(_translate("Examination", "Age"))
        item = self.health_table.horizontalHeaderItem(3)
        item.setText(_translate("Examination", "In_care"))
        item = self.health_table.horizontalHeaderItem(4)
        item.setText(_translate("Examination", "HAEMATOCRIT"))
        item = self.health_table.horizontalHeaderItem(5)
        item.setText(_translate("Examination", "HAEMOGLOBINS"))
        item = self.health_table.horizontalHeaderItem(6)
        item.setText(_translate("Examination", "ERYTHROCYTE"))
        item = self.health_table.horizontalHeaderItem(7)
        item.setText(_translate("Examination", "LEUCOCYTE"))
        item = self.health_table.horizontalHeaderItem(8)
        item.setText(_translate("Examination", "MCH"))
        item = self.health_table.horizontalHeaderItem(9)
        item.setText(_translate("Examination", "MCHC"))
        item = self.health_table.horizontalHeaderItem(10)
        item.setText(_translate("Examination", "MCV"))
        item = self.health_table.horizontalHeaderItem(11)
        item.setText(_translate("Examination", "Bạch cầu"))
        item = self.health_table.horizontalHeaderItem(12)
        item.setText(_translate("Examination", "Edit"))
        item = self.health_table.horizontalHeaderItem(13)
        item.setText(_translate("Examination", "Delete"))
        self.export_button.setText(_translate("Examination", "Xuất"))
        self.add_new_button.setText(_translate("Examination", "Thêm mới"))
        self.search_button.setText(_translate("Examination", "Search"))
        self.label.setText(_translate("Examination",
                                      "Incare:  0 - Out care patient                                 1 - In care patient"))
        self.train_button.setText(_translate("MainWindow", "Train Model"))
        self.data_analysis_group_box.setTitle(_translate("MainWindow", "Data Analysis"))
        self.view_button.setText(_translate("MainWindow", "view"))
        self.predict_group_box.setTitle(_translate("MainWindow", "In/Out care patient"))
        self.predict_button.setText(_translate("MainWindow", "Prediction"))
        self.import_button.setText(_translate("MainWindow", "import"))


    # initial data
    def initial_table(self):
        try:
            cursor = self.cnx.cursor()
            results = cm.show_table(cursor, 'check_health')
            if results:
                self.data_to_table(results)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    # action to table
    def uncell(self, s):
        try:
            item = QtWidgets.QTableWidgetItem(str(s))
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            return item
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)
            return ''

    def data_to_table(self, results):
        try:
            self.health_table.clearContents()
            self.health_table.setRowCount(0)
            if results == [None] or results == []:
                QMessageBox.information(self, 'Information', 'There\'s no value like that', QMessageBox.Close)
                return
            for i in range(len(results)):
                value = cm.get_farmer_by_farmerId(self.cnx.cursor(), results[i][1])
                if not value:
                    continue
                self.health_table.insertRow(i)
                name = value[1]
                age = datetime.today().year - value[3].year
                in_care = value[5]
                self.health_table.setItem(i, 0, self.uncell(results[i][0]))
                self.health_table.setItem(i, 1, self.uncell(name))
                self.health_table.setItem(i, 2, self.uncell(age))
                self.health_table.setItem(i, 3, self.uncell(in_care))
                self.health_table.setItem(i, 4, self.uncell(results[i][3]))
                self.health_table.setItem(i, 5, self.uncell(results[i][4]))
                self.health_table.setItem(i, 6, self.uncell(results[i][5]))
                self.health_table.setItem(i, 7, self.uncell(results[i][6]))
                self.health_table.setItem(i, 8, self.uncell(results[i][7]))
                self.health_table.setItem(i, 9, self.uncell(results[i][8]))
                self.health_table.setItem(i, 10, self.uncell(results[i][9]))
                self.health_table.setItem(i, 11, self.uncell(results[i][10]))
                self.edit_btn = QtWidgets.QPushButton(self)
                self.edit_btn.clicked.connect(self.edit_window)
                self.edit_btn.setText('Edit')
                self.health_table.setCellWidget(i, 12, self.edit_btn)
                self.delete_btn = QtWidgets.QPushButton(self)
                self.delete_btn.clicked.connect(self.delete_btn_click)
                self.delete_btn.setText('Delete')
                self.health_table.setCellWidget(i, 13, self.delete_btn)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    # active button
    # button on table
    def edit_window(self):
        try:
            button = self.sender()
            index = self.health_table.indexAt(button.pos())
            table_model = self.health_table.model()
            id = table_model.data(table_model.index(index.row(), 0))
            self.add_new_button_active(id)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def delete_btn_click(self):
        try:
            button = self.sender()
            index = self.health_table.indexAt(button.pos())
            table_model = self.health_table.model()
            id = table_model.data(table_model.index(index.row(), 0))
            name = table_model.data(table_model.index(index.row(), 1))
            account_id = cm.get_accId_from_farmer_id(self.cnx.cursor(), id)[0]
            button_reply = QMessageBox.question(self, 'Confirmation message',
                                                'You want to delete patient {}?'.format(name),
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                if cm.delete_account_from_id(self.cnx, account_id):
                    QMessageBox.information(self, 'Success', 'Delete successfull', QMessageBox.Close)
                    self.initial_table()
                else:
                    QMessageBox.information(self, 'Error', 'There\'s some error')
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    # button on window
    def search_button_active(self):
        try:
            text = self.search_txt.text()
            cursor = self.cnx.cursor()
            if v.check_id(text):
                value = [cm.check_health_from_farmerId(cursor, text)]
                self.data_to_table(value)
            elif v.check_search_name(text):
                ids = cm.get_farmer_id_by_name(cursor, text)
                values = []
                for id in ids:
                    values.append(cm.check_health_from_farmerId(cursor, id[0]))
                self.data_to_table(values)
            else:
                QMessageBox.information(self, 'Error', 'Search is not invalid\nPlease re-input', QMessageBox.Close)

        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def add_new_button_active(self,id=0):
        try:
            self.ui_mcs = mcs.Ui_Medical_Certi(id)
            self.ui_mcs.setupUi()
            self.ui_mcs.show()
            self.ui_mcs.save_button.clicked.connect(self.save_button_active)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def data_from_table(self):
        try:
            row = self.health_table.rowCount()
            df = pd.DataFrame(columns=['Patient_id','Patient_name','Age','In_care','HAEMATOCRIT','HAEMOGLOBINS','ERYTHROCYTE','LEUCOCYTE','MCH','MCHC','MCV','THROMBOCYTE'])
            for i in range(row):
                value = []
                for j in range(12):
                    value.append(self.health_table.item(i,j).text())
                df.loc[len(df.index)] = value
            return df
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)
            return []
    def export_button_active(self):
        try:
            df = self.data_from_table()
            if len(df.index) == 0:
                QMessageBox.information(self, 'Error', 'There is no value', QMessageBox.Close)
                return
            if cm.data_to_excel('Medical_Check',df):
                QMessageBox.information(self, 'Success', 'Export success full', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Fail', 'Something wrong', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    #button of medical_certi_screen
    def save_button_active(self):
        try:
            farmer_id = self.ui_mcs.id_name_combobox.currentText().split(' - ')[0]
            health_fix = []
            health_fix.append(self.ui_mcs.dthc_txt.text())
            health_fix.append(self.ui_mcs.hst_txt.text())
            health_fix.append(self.ui_mcs.hc_txt.text())
            health_fix.append(self.ui_mcs.tc_txt.text())
            health_fix.append(self.ui_mcs.MCH_txt.text())
            health_fix.append(self.ui_mcs.MCHC_txt.text())
            health_fix.append(self.ui_mcs.MCV_txt.text())

            health_fix.append(self.ui_mcs.bc_txt.text())

            for x in health_fix:
                if not v.check_health(x):
                    QMessageBox.information(self, 'Error', 'Something wrong in health unit', QMessageBox.Close)
                    return

            if self.ui_mcs.farmer_id !=0:
                health_fix.append(self.ui_mcs.inpatient.text())
                health_fix.append(farmer_id)
                if cm.update_health(self.cnx,health_fix):
                    QMessageBox.information(self, 'Success', 'Update successfull', QMessageBox.Close)
                    self.ui_mcs.hide()
            else:
                health_fix = [self.staff_id, farmer_id, health_fix[0], health_fix[1],
                              health_fix[2], health_fix[3], health_fix[4], health_fix[5], health_fix[6], health_fix[7]]
                if cm.insert_check_health(self.cnx,health_fix):
                    QMessageBox.information(self, 'Success', 'Insert successfull', QMessageBox.Close)
                    self.ui_mcs.hide()
            self.initial_table()
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    def predict_in_or_out_patient(self):
        self.predict_screen = Predict_InOutPatient.Ui_Medical_Certi()
        self.predict_screen.setupUi()
        self.predict_screen.show()

    def view_button_active(self):
        try:
            text = self.plot_combobox.currentText()
            text = text.lower()
            if text == 'correlation':
                view.treatment_correlation()
            elif text == 'age plot':
                view.treatement_age()
            elif text == 'thrombocyte plot':
                view.treatment_thrombocyte()
            elif text == 'median plot':
                view.treatment_median_of_all()
            elif text == 'treatment pie':
                view.treatment_pie()
            else:
                QMessageBox.information(self, 'Error', 'Your combo box is not valid', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)

    #External button
    def df_to_table(self,results):
        try:
            self.health_table.clearContents()
            self.health_table.setRowCount(0)
            if len(results) ==0:
                QMessageBox.information(self, 'Information', 'There\'s no value like that', QMessageBox.Close)
                return
            for i in range(len(results)):
                self.health_table.insertRow(i)
                result = results.iloc[i]
                self.health_table.setItem(i, 0, self.uncell(result[1]))
                self.health_table.setItem(i, 1, self.uncell(result[2]))
                self.health_table.setItem(i, 2, self.uncell(result[3]))
                self.health_table.setItem(i, 3, self.uncell(result[4]))
                self.health_table.setItem(i, 4, self.uncell(result[5]))
                self.health_table.setItem(i, 5, self.uncell(result[6]))
                self.health_table.setItem(i, 6, self.uncell(result[7]))
                self.health_table.setItem(i, 7, self.uncell(result[8]))
                self.health_table.setItem(i, 8, self.uncell(result[9]))
                self.health_table.setItem(i, 9, self.uncell(result[10]))
                self.health_table.setItem(i, 10, self.uncell(result[11]))
                self.health_table.setItem(i, 11, self.uncell(result[12]))
                self.edit_btn = QtWidgets.QPushButton(self)
                self.edit_btn.clicked.connect(self.edit_window)
                self.edit_btn.setText('Edit')
                self.health_table.setCellWidget(i, 12, self.edit_btn)
                self.delete_btn = QtWidgets.QPushButton(self)
                self.delete_btn.clicked.connect(self.delete_btn_click)
                self.delete_btn.setText('Delete')
                self.health_table.setCellWidget(i, 13, self.delete_btn)
        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)
    def import_button_active(self):
        try:
            dir = './'
            filter = "Excel files (*.xlsx)"
            fname = QFileDialog.getOpenFileName(self, 'Open file', dir,filter)
            if not fname[0]:
                return
            fname = fname[0]
            df = pd.read_excel(fname)
            self.df_to_table(df)

        except Exception as err:
            QMessageBox.information(self, 'Error', str(err.args[0]), QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Examination()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
