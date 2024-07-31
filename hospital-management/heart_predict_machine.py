# Regular EDA and plotting libraries
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QApplication
from PyQt5.uic.properties import QtWidgets
from matplotlib.figure import Figure
from matplotlib_inline.backend_inline import FigureCanvas
import warnings
warnings.filterwarnings("ignore")
# Models from scikit-learn
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Model Evaluations
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score

df = pd.read_csv('./get_report/heart-disease.csv')

#modeling
# split features and labels
X = df.drop('target', axis=1)
y = df['target']

# split into training, testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train model
# put models in dictionary

models = {
    'LogisticRegression': LogisticRegression(max_iter=1000),
    'KNN': KNeighborsClassifier(),
    'RandomForestClassifer': RandomForestClassifier()
}

# create function to fit and score model
def fit_and_score(models, X_train, X_test, y_train, y_test):
    # set random seed
    np.random.seed(42)

    # make dictonary to keep scores
    model_scores = {}

    # loop through models to fit and score
    for model_name, model in models.items():
        model.fit(X_train, y_train)  # fit model
        score = model.score(X_test, y_test)  # get score
        model_scores[model_name] = score  # put score for each model

    return model_scores
# fit and score
model_scores = fit_and_score(models, X_train, X_test, y_train, y_test)
# print(model_scores)

# # so sánh model
# model_compare = pd.DataFrame(model_scores, index=['accuracy'])
# model_compare.head()
# model_compare.T.plot(kind='bar');
# plt.show()

# improve model
# create hyperparameter grid for Logistic Regression
log_reg_grid = {
    'C': np.logspace(-4, 4, 20),
    'solver': ['liblinear']
}

# set up grid hyperparameter search for Logistic Regression
gs_log_reg = GridSearchCV(LogisticRegression(),
                                          log_reg_grid,
                                          cv=5,
                                          verbose=True)

# train the model
gs_log_reg.fit(X_train, y_train)
# make predictions
y_preds = gs_log_reg.predict(X_test)
# tìm C - check current best parameter
# print(gs_log_reg.best_params_)

model = LogisticRegression(C=0.23357214690901212, solver='liblinear')
model.fit(X_train, y_train)
# Cross Validated Recall
# create a new classifier with current best parameter
cv_recall = cross_val_score(model, X, y, scoring='recall', cv=5)
cv_recall = np.mean(cv_recall)
cv_recall
# Dự báo
def predict_Heart_Disease(age,sex,cp,trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    #loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = age
    x[1] = sex
    x[2] = cp
    x[3] = trestbps
    x[4] = chol
    x[5] = fbs
    x[6] = restecg
    x[7] = thalach
    x[8] = exang
    x[9] = oldpeak
    x[10] = slope
    x[11] = ca
    x[12] = thal
    #if loc_index >= 0:
       #x[loc_index] = 1

    return gs_log_reg.predict([x])[0]
# predict = predict_Heart_Disease(100, 1, 0, 100, 100, 0, 0, 150,0, 3, 2, 1 ,2 )
# print(predict)

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QApplication

class Show_Plot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plot Static")
        self.setGeometry(100, 100, 800, 600)

    def test_plot(self):
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)

        x= [1,2,3,4,5]
        y= [12,3,5,5,6]

        self.axes.plot(x,y)
        # tạo widget để hiển thị biểu đồ
        canvas = FigureCanvas(self.figure)
        canvas.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        canvas.updateGeometry()

        # thêm widget vào QMainWindow
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)
        layout.addWidget(canvas)

    # số lượng no disease và heart disease
    def volumn_heart_disease(self):
        # Tạo Figure và Axes của Matplotlib
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        # Vẽ biểu đồ
        df['target'].value_counts().plot.bar(color=['salmon', 'lightblue'], ax=self.axes)
        self.axes.set_xlabel('0: No Disease, 1: Heart Disease')
        self.axes.set_ylabel('Count')
        self.axes.set_title('Heart Disease Distribution')
        # Tạo Widget để hiển thị biểu đồ
        canvas = FigureCanvas(self.figure)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()

        # Thêm Widget vào QMainWindow
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)
        layout.addWidget(canvas)


    # tỉ lệ bệnh tim của giới tính
    def sex_heart_percent(self):

        # Tạo widget để hiển thị biểu đồ
        self.canvas = FigureCanvas(plt.figure())

        # Vẽ biểu đồ
        pd.crosstab(df['sex'], df['target']).plot(kind='bar', ax=self.canvas.figure.add_subplot(111))
        plt.title('Heart disease frequency by Sex')
        plt.xlabel('0: No Disease, 1: Heart Disease ')
        plt.ylabel('Count')
        plt.legend(['Female', 'Male'])
        plt.xticks(rotation=0)

        # Thêm widget vào QMainWindow
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.canvas)

    # bệnh theo tuổi và nhịp tối đa
    def age_max_heart_rate(self):
        # Khởi tạo widget để hiển thị biểu đồ
        self.canvas = FigureCanvas(plt.figure(figsize=(10, 7)))
        self.setCentralWidget(self.canvas)
        # Vẽ biểu đồ
        positive_cases = df[df.target == 1]
        negative_cases = df[df.target == 0]
        plt.scatter(x=positive_cases.age, y=positive_cases.thalach, color='salmon', s=50, alpha=0.8)
        plt.scatter(x=negative_cases.age, y=negative_cases.thalach, color='lightblue', s=50, alpha=0.8)
        plt.title('Heart Disease in function of Age and Max Heart Rate')
        plt.xlabel('Age')
        plt.ylabel('Max Heart Rate')
        plt.legend(['Heart Disease', 'No Disease'])
        plt.tight_layout()

    # tuổi
    def age_plot(self):
        # Tạo Figure và Axes của Matplotlib
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)

        # Vẽ biểu đồ
        sns.histplot(data=df, x=df['age'], bins=30, ax=self.axes)
        self.axes.set_title('Age Histogram')
        self.axes.set_xlabel('Age')
        self.axes.set_ylabel('Count')

        # Tạo widget để hiển thị biểu đồ
        canvas = FigureCanvas(self.figure)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()

        # Thêm widget vào QMainWindow
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)
        layout.addWidget(canvas)

        # Thiết lập kích thước và tiêu đề của cửa sổ
        self.setGeometry(200, 200, 500, 400)
        self.setWindowTitle('Age Histogram')

    # Tần suất bệnh tim theo mức độ đau ngực
    def heart_disease_frequency(self):
        # Tạo Figure và Axes của Matplotlib
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)

        # Vẽ biểu đồ
        pd.crosstab(df['cp'], df['target']).plot(kind='bar', color=['lightblue', 'salmon'], ax=self.axes)
        self.axes.set_title('Heart Disease Frequency per Chest Pain level')
        self.axes.set_xlabel('Chest Pain Level')
        self.axes.set_ylabel('Count')
        self.axes.legend(['No Diease', 'Heart Disease'])

        # Tạo widget để hiển thị biểu đồ
        canvas = FigureCanvas(self.figure)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()

        # Thêm widget vào QMainWindow
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)
        layout.addWidget(canvas)


    # visualization
    def visualization(self):
        # Create a Figure object and set its size
        self.figure = Figure(figsize=(12, 8))

        # Add a plot to the Figure object
        self.axes = self.figure.add_subplot(111)

        # Create a correlation matrix
        corr_matrix = df.corr()

        # Create a heatmap of the correlation matrix
        sns.heatmap(corr_matrix, annot=True, linewidth=0.5, fmt='.2f', cmap='viridis_r', ax=self.axes)

        # Create a canvas widget to display the plot
        canvas = FigureCanvas(self.figure)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()

        # Add the canvas widget to the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(canvas)

    def compare_model(self):
        # create plot
        model_compare = pd.DataFrame(model_scores, index=['accuracy'])
        self.fig, self.ax = plt.subplots()
        model_compare.T.plot(kind='bar', ax=self.ax)
        self.ax.set_title('Model Comparison')
        self.ax.set_xlabel('Models')
        self.ax.set_ylabel('Accuracy')

        # create canvas widget
        canvas = FigureCanvas(self.fig)

        # add canvas widget to central widget
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(canvas)
        self.setCentralWidget(central_widget)


# if __name__ == '__main__':
#     model_scores = fit_and_score(models, X_train, X_test, y_train, y_test)
#     print(model_scores)

