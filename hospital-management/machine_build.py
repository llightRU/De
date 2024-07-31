import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score,accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

def connect_to_google_sheet():
    try:
        ss_cred_path = r'./json_file/hospital-mangage-a18253231a0a.json'
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(ss_cred_path,scope)
        gc = gspread.authorize(creds)
        return gc
    except:
        return None

def read_sheet(gc,ws):
    try:
        spreadsheet_id = "1fkK5-bkqGy9gJD6SckhfCiy60rRxVAKl4L83d2I8enM"
        wks = gc.open_by_key(spreadsheet_id)
        worksheet = wks.worksheet(ws)
        df = pd.DataFrame(worksheet.get_all_records())
        return df
    except:
        return None


def tunning_model(X,y):
    model = LogisticRegression()
    parameters = [
              {'C':[1, 10, 100, 1000]},
              {'max_iter':[500,2000,5000]}]
    grid_search = GridSearchCV(estimator=model,
                            param_grid=parameters,
                            scoring='accuracy',
                            cv=5,
                            verbose=0)

    grid_search.fit(X,y)

    print('GridSearch CV best score : {:.4f}\n\n'.format(grid_search.best_score_))


    print('Parameters that give the best results :','\n\n', (grid_search.best_params_))

    print('\n\nEstimator that was chosen by the search :','\n\n', (grid_search.best_estimator_))

def build_model(X,y):
    max_iter = 500
    model = LogisticRegression(max_iter=max_iter)
    model.fit(X,y)
    return model

gc = connect_to_google_sheet()
df = read_sheet(gc,'in_out')
jk = {"M" : 1, "F" : 0}
df["SEX"] = df["SEX"].map(jk)
jk = {"out" : 0, "in" : 1}
df["SOURCE"] = df["SOURCE"].map(jk)

X = df.drop(columns='SOURCE').values
y = df['SOURCE'].values
model = build_model(X,y)

print(X[-1])
y_pred = model.predict(X[-1].reshape(1,-1))
print(y_pred)

if __name__ == "__main__":
    """gc = connect_to_google_sheet()
    df = read_sheet(gc,'in_out')
    jk = {"M" : 1, "F" : 0}
    df["SEX"] = df["SEX"].map(jk)   
    jk = {"out" : 0, "in" : 1}
    df["SOURCE"] = df["SOURCE"].map(jk) 

    X = df.drop(columns='SOURCE').values
    y = df['SOURCE'].values
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=42)

    max_iter = 500
    model = LogisticRegression(max_iter=max_iter)
    model.fit(X_train,y_train)
    y_pred_test = model.predict(X_test)
    print('Model f1 score: {0:0.4f}'. format(f1_score(y_test, y_pred_test)))
    print('Model accurancy score : {0:0.4f}'.format(accuracy_score(y_test,y_pred_test)))

    y_pred = model.predict(X_train[-1].reshape(1,-1))
    print(y_pred)"""
    pass