import os
import numpy as np
from scipy.constants import pt
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from PyQt5.uic.properties import QtWidgets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd


# dự đoán nhập viện
def treatment_classification(data_predict=[]):

    data = pd.read_csv('./get_report/treatment.csv')
    print(data['SOURCE'].value_counts())

    X_train, X_test, y_train, y_test = preprocess_inputs(data)

    models = {
        "Logistic Regression": LogisticRegression(),
        "Decision Tree": DecisionTreeClassifier(),
        "Neural Network": MLPClassifier(),
        "Random Forest": RandomForestClassifier(),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)

    for name, model in models.items():
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(name + " Accuracy: {:.2f}%".format(acc * 100))

    num_trees = 100
    seed = 7
    rf = RandomForestClassifier(n_estimators=num_trees, random_state=seed)
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)
    print(classification_report(y_test, predictions))

    # test data baru
    # ket:
    # 33.8 = HAEMATOCRIT
    # 11.1 = HAEMOGLOBINS
    # 4.18 = ERYTHROCYTE
    # 4.6 = LEUCOCYTE
    # 150 = THROMBOCYTE
    # 26.6 = MCH
    # 32.8 = MCHC
    # 80.9 = MCV
    # 33 = AGE
    # 0 = SEX
    list_predict = []
    for item in range(len(data_predict)-1):
        list_predict.append(float(data_predict[item]))
    list_predict.append(int(data_predict[-1]))
    print(list_predict)
    prediction_rf = rf.predict([list_predict])
    score1 = rf.score(X_test, y_test)
    if prediction_rf[0] == 1:
        pred = "in care patient"
    else:
        pred = "out care patient"
    print('Prediksi :', pred)
    print("Test score: {0:.2f} %".format(100 * score1))

    return prediction_rf[0]

# train data
def preprocess_inputs(df):

    df = df.copy()

    # Binary encoding
    df['SEX'] = df['SEX'].replace({'F': 0, 'M': 1})

    # Split df into X and y
    y = df['SOURCE']
    X = df.drop('SOURCE', axis=1)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=1)

    # Scale X
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = pd.DataFrame(scaler.transform(X_train), index=X_train.index, columns=X_train.columns)
    X_test = pd.DataFrame(scaler.transform(X_test), index=X_test.index, columns=X_test.columns)

    return X_train, X_test, y_train, y_test

# fake data - bỏ
def fake_data():
    # đọc dữ liệu
    df_1 = pd.read_csv('./get_report/inpatientCharges.csv')
    name_1 = df_1['Hospital Referral Region Description'].unique()

    df_2 = pd.read_excel('./import_file/benhvien.xlsx')
    name_2 = df_2['Cơ sở KCB'].head(306).unique()

    new_values = {}
    for i in range(len(name_1)):
        new_values.update({name_1[i]: name_2[i]})

    workbook = openpyxl.load_workbook("C:/Users/FPT SHOP/Desktop/inpatientCharges.xlsx")
    worksheet = workbook["Sheet1"]

    # Thay đổi giá trị của từng ô thuộc tập giá trị cần thay đổi
    for cell in worksheet["H"]:
        if cell.value in new_values:
            cell.value = new_values[cell.value]

    # Lưu lại file Excel
    workbook.save("example.xlsx")

# thống kê chi phí - bỏ
def hospital_charges(path):
    try:
        df = None

        if path:

            if 'xlsx' in path:
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)

            # Nhóm theo tên bệnh viện và tính tổng chi phí trung bình
            cost_by_hospital = df.groupby('Hospital Referral Region Description')[' Average Total Payments '].sum()

            # Sắp xếp giá trị giảm dần và chọn ra 20 bệnh viện có chi phí cao nhất
            top_hospitals = cost_by_hospital.sort_values(ascending=True)[0:10]

            # vẽ biểu đồ
            plt.figure(figsize=(20, 10))
            plt.barh(top_hospitals.index, top_hospitals.values, color='blue')
            plt.title('Top 10 bệnh viện có chi phí nội trú cao nhất')
            plt.yticks(fontsize=7)
            plt.xlabel('Chi phí nội trú($)')
            plt.ylabel('Tên bệnh viện')
            plt.grid(axis='x')
            plt.show()



    except Exception as e:
        print(e)

class HospitalCharges(QWidget):
    def __init__(self, path):
        super().__init__()

        self.title = 'Top 10 viện phí'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600

        self.initUI(path)

    def initUI(self, path):

        # đọc dữ liệu
        try:
            if 'xlsx' in path:
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)
        except Exception as e:
            print(e)
            return

        # tính tổng chi phí trung bình theo tên bệnh viện
        cost_by_hospital = df.groupby('Hospital Referral Region Description')[' Average Total Payments '].sum()

        # chọn ra 10 bệnh viện có chi phí cao nhất
        top_hospitals = cost_by_hospital.sort_values(ascending=True)[0:10]

        # tạo đồ thị
        fig = Figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.barh(top_hospitals.index, top_hospitals.values, color='blue')
        ax.set_title(self.title)
        ax.set_xlabel('Chi phí nội trú($)')
        ax.set_ylabel('Tên bệnh viện')
        ax.grid(axis='x')

        # thêm đồ thị vào widget
        self.canvas = FigureCanvas(fig)

        #c1:
        # layout = QVBoxLayout()
        # layout.addWidget(canvas)
        #
        # self.setLayout(layout)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setWindowTitle(self.title)
        # self.show()

        #c2:
        # Tạo layout Grid và thêm biểu đồ vào layout
        layout = QGridLayout()
        layout.addWidget(self.canvas, 1, 1, 1, 1)

        # Thiết lập layout cho widget
        self.setLayout(layout)

        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('Biểu đồ chi phí nội trú của bệnh viện')
        self.show()

def heart_predict():
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv('./get_report/heart_failure_clinical_records_dataset.csv')

    # Chọn các trường quan trọng để đưa vào mô hình
    features = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
                'ejection_fraction', 'high_blood_pressure', 'platelets',
                'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']

    # Chọn trường target
    target = 'DEATH_EVENT'

    # Chia tập dữ liệu thành tập train và tập test
    train_data, test_data, train_target, test_target = train_test_split(data[features], data[target], test_size=0.2,
                                                                        random_state=42)

    # Khởi tạo mô hình K-NN với số lượng láng giềng gần nhất là 5
    model = KNeighborsClassifier(n_neighbors=5)

    # Train mô hình trên tập train
    model.fit(train_data, train_target)

    # Đưa ra dự đoán trên tập test
    pred_target = model.predict(test_data)

    # Tính độ chính xác của mô hình trên tập test
    accuracy = accuracy_score(test_target, pred_target)

    # In ra độ chính xác của mô hình
    print(f"Độ chính xác của mô hình là {accuracy}")

    # Khởi tạo mô hình Logistic Regression
    model = LogisticRegression()

    # Train mô hình trên tập train
    model.fit(train_data, train_target)

    # Đưa ra dự đoán trên tập test
    pred_target = model.predict(test_data)

    # Tính độ chính xác của mô hình trên tập test
    accuracy = accuracy_score(test_target, pred_target)

    # In ra độ chính xác của mô hình
    print(f"Độ chính xác của mô hình là {accuracy}")

    # Khởi tạo mô hình Random Forest với số lượng cây là 100
    model = RandomForestClassifier(n_estimators=100)

    # Train mô hình trên tập train
    model.fit(train_data, train_target)

    # Đưa ra dự đoán trên tập test
    pred_target = model.predict(test_data)

    # Tính độ chính xác của mô hình trên tập test
    accuracy = accuracy_score(test_target, pred_target)

    # In ra độ chính xác của mô hình
    print(f"Độ chính xác của mô hình là {accuracy}")

    # Khởi tạo mô hình SVM với kernel là RBF
    model = SVC(kernel='rbf')

    # Train mô hình trên tập train
    model.fit(train_data, train_target)

    # Đưa ra dự đoán trên tập test
    pred_target = model.predict(test_data)

    # Tính độ chính xác của mô hình trên tập test
    accuracy = accuracy_score(test_target, pred_target)

    # In ra độ chính xác của mô hình
    print(f"Độ chính xác của mô hình là {accuracy}")


class Hospital_dead(QWidget):
    def __init__(self, path):
        super().__init__()
        self.initUI(path)
    def initUI(self, path):
        # đọc dữ liệu
        try:
            if 'xlsx' in path:
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)
        except Exception as e:
            print(e)
            return
        plt.rcParams['figure.figsize'] = (12, 6)
        df['hospital_death'].value_counts().plot(kind='pie', autopct='%1.2f%%', figsize=(8, 8))
        plt.show()

class Hospital_dead_gender(QWidget):
    def __init__(self, path):
        super().__init__()
        self.initUI(path)
    def initUI(self, path):
        # đọc dữ liệu
        try:
            if 'xlsx' in path:
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)
        except Exception as e:
            print(e)
            return
        plt.figure(figsize=(10, 15))
        df['gender'].value_counts().plot(kind='pie', autopct='%1.2f%%', figsize=(8, 8))
        plt.show()

class Hospital_dead_icu(QWidget):
    def __init__(self, path):
        super().__init__()
        self.initUI(path)
    def initUI(self, path):
        # đọc dữ liệu
        try:
            if 'xlsx' in path:
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)
        except Exception as e:
            print(e)
            return
        plt.figure(figsize=(15, 10))
        df['icu_stay_type'].value_counts().plot(kind='pie', autopct='%1.2f%%', figsize=(8, 8))
        plt.show()

class Hospital_dead_apache(QWidget):
    def __init__(self, path):
        super().__init__()
        self.initUI(path)
    def initUI(self, path):
        # đọc dữ liệu
        try:
            if 'xlsx' in path:
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)
        except Exception as e:
            print(e)
            return
        plt.figure(figsize=(25, 15))
        df['apache_2_bodysystem'].value_counts().plot(kind='pie', autopct='%1.2f%%', figsize=(8, 8))
        plt.show()

def dead_predict(path):
    data = pd.read_csv(path)

    # Thay thế các giá trị null bằng giá trị trung bình của cột đó
    # data=data.fillna()
    data = data.fillna(data.mean())

    # Sử dụng mã hóa one-hot để biến đổi các giá trị dạng chuỗi thành các giá trị dạng số
    data = pd.get_dummies(data, columns=['ethnicity', 'gender','icu_stay_type'])

    # Tạo đặc trưng X và nhãn y
    X = data.drop(labels=['hospital_death','icu_admit_source','icu_type','apache_3j_bodysystem','apache_2_bodysystem'], axis=1)
    y = data['hospital_death']

    # Chia tập dữ liệu thành tập train và test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, train_size=0.7, random_state=42)

    # Huấn luyện mô hình
    # clf = neighbors.KNeighborsClassifier(n_neighbors=2, p=2)
    clf = HistGradientBoostingClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # In kết quả

    accuracy = accuracy_score(y_test, y_pred)
    print('KNN')
    print("Accuracy on test data:", accuracy)


    # Tạo một hàng mới với các giá trị tương ứng trong các cột
    new_data = X.tail(1)
    print(new_data)
    new_patient_pred = clf.predict(new_data)
    # In kết quả
    print("Predicted label for new patient: ", new_patient_pred)

    return accuracy, new_patient_pred

def dead_predict_pass_data(path):
    data = pd.read_csv(path)

    # Thay thế các giá trị null bằng giá trị trung bình của cột đó
    # data=data.fillna()
    data = data.fillna(data.mean())

    # Sử dụng mã hóa one-hot để biến đổi các giá trị dạng chuỗi thành các giá trị dạng số
    data = pd.get_dummies(data, columns=['ethnicity', 'gender','icu_stay_type'])

    # Tạo đặc trưng X và nhãn y
    X = data.drop(labels=['hospital_death','icu_admit_source','icu_type','apache_3j_bodysystem','apache_2_bodysystem'], axis=1)
    y = data['hospital_death']

    # Chia tập dữ liệu thành tập train và test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, train_size=0.7, random_state=42)

    # Huấn luyện mô hình
    # clf = neighbors.KNeighborsClassifier(n_neighbors=2, p=2)
    clf = HistGradientBoostingClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # In kết quả

    accuracy = accuracy_score(y_test, y_pred)
    print('KNN')
    print("Accuracy on test data:", accuracy)


    # Tạo một hàng mới với các giá trị tương ứng trong các cột
    new_data = X.tail(1)
    print(new_data)
    new_patient_pred = clf.predict(new_data)
    # In kết quả
    print("Predicted label for new patient: ", new_patient_pred)

    return new_data, new_patient_pred

if __name__=='__main__':
    treatment_classification()