from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import common as cm
import mysql.connector

class Messenger(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Tạo layout chính cho MainWindow
        self.main_layout = QVBoxLayout()

        # Tạo nút gửi tin nhắn
        send_button = QPushButton(QIcon('img/send.jpg'), "-- Send -->", self)
        send_button.setIconSize(QtCore.QSize(60, 60))
        send_button.clicked.connect(self.send_message)

        # Tạo trường nhập tin nhắn
        self.message_input = QPlainTextEdit()
        self.message_input.setMaximumHeight(80)

        # Tạo frame để chứa trường chat
        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        # Tạo layout cho frame
        frame_layout = QVBoxLayout()
        frame.setLayout(frame_layout)

        # Tạo trường chat để hiển thị tin nhắn
        self.chat_display = QPlainTextEdit()
        self.chat_display.setReadOnly(True)
        # set font
        self.chat_display.setFont(QtGui.QFont('Arial', 14))

        # Thêm các thành phần vào layout chính
        self.main_layout.addWidget(self.chat_display)
        self.main_layout.addWidget(self.message_input)
        self.main_layout.addWidget(send_button)

        # Thiết lập layout cho frame
        frame_layout.addLayout(self.main_layout)
        frame_layout.setAlignment(Qt.AlignBottom)

        # Thiết lập widget chính cho MainWindow
        self.setCentralWidget(frame)
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Messenger')

        # hiển thị tin nhắn
        self.message_list = self.get_message()
        print(self.message_list)
        for i in range(len(self.message_list)):
            # nếu là tin nhắn của staff thì style đỏ
            if(self.message_list[i][4]==1):
                # Định dạng văn bản của tin nhắn
                format = QtGui.QTextCharFormat()
                format.setForeground(QtCore.Qt.red)

                # Thêm tin nhắn vào trường chat và định dạng văn bản
                cursor = self.chat_display.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                cursor.insertText('\nYour: ' + self.message_list[i][1], format)
            else:
                # Định dạng lại văn bản
                format = QtGui.QTextCharFormat()
                format.setForeground(QtCore.Qt.black)

                # Thêm tin nhắn vào trường chat và định dạng văn bản
                cursor = self.chat_display.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                cursor.insertText('\nGoverment: ' + self.message_list[i][1], format)
                # # tin nhắn của goverment
                # self.chat_display.appendPlainText(self.message_list[i][1])

    def send_message(self):
        try:
            # Lấy nội dung tin nhắn từ trường nhập
            message = self.message_input.toPlainText().strip()
            if message:
                # # Hiển thị tin nhắn lên trường chat
                # self.chat_display.appendPlainText('Your: '+ message)
                # # Xóa nội dung tin nhắn trong trường nhập
                # self.message_input.clear()

                # Định dạng văn bản của tin nhắn
                format = QtGui.QTextCharFormat()
                format.setForeground(QtCore.Qt.red)

                # Thêm tin nhắn vào trường chat và định dạng văn bản
                cursor = self.chat_display.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                cursor.insertText('\nYour: ' + message, format)

                # xóa nội dung message_input
                self.message_input.clear()

            # insert message vào database
            list_data = [1,1,message,1]
            data_base_config = cm.read_json_file(cm.FILE_JSON_PATH)
            cnx = mysql.connector.connect(**data_base_config)
            cursor = cnx.cursor()
            stm = 'insert into message(staff_id,goverment_id,content,mark_staff_txt) VALUES (%s,%s,%s,%s)'
            cursor.execute(stm,list_data)
            cnx.commit()
            cnx.close()
            print('success insert')
        except Exception as e:
            print(e)

    # lấy message từ db với staff_id
    def get_message(self):

        try:

            data_base_config = cm.read_json_file(cm.FILE_JSON_PATH)
            cnx = mysql.connector.connect(**data_base_config)
            cursor = cnx.cursor()
            cursor.execute('SELECT m.m_id,content,m.staff_id,m.goverment_id,m.mark_staff_txt FROM message m INNER JOIN goverment g ON m.goverment_id = g.goverment_id WHERE m.staff_id = 9;')
            message_list = cursor.fetchall()
            cnx.commit()
            cnx.close()
            print(type(message_list[0][4]))
            return message_list

        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication([])
    messenger = Messenger()
    messenger.show()
    app.exec_()