import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def treatment_correlation():
    try:
        df = pd.read_csv('./get_report/treatment.csv')
        plt.figure(figsize=(10, 10))
        sns.heatmap(df.corr(), annot=True)
        plt.show()
    except Exception as err:
            print(err)

def treatement_age():
    try:
        df = pd.read_csv('./get_report/treatment.csv')
        df1 = df[df['SOURCE'] == 'in']
        fig,axes = plt.subplots(1,2,sharey=True,figsize=(12,8))
        fig.suptitle('Treatment age plot')
        sns.histplot(ax=axes[0], data=df1['AGE'], color="blue", label="100% Equities", kde=True, stat="density",
                     linewidth=0)
        axes[0].set_title('Age of inpatient')
        df2 = df[df['SOURCE'] =='out']
        sns.histplot(ax=axes[1], data=df2['AGE'], color="blue", label="100% Equities", kde=True, stat="density",
                     linewidth=0)
        axes[1].set_title('Age of outpatient')
        plt.show()
    except Exception as err:
            print(err)

def treatment_median_of_all():
    try:
        df = pd.read_csv('./get_report/treatment.csv')
        fig,axes = plt.subplots(1,2,sharey=True,figsize=(15,15))
        fig.suptitle('Treatment median plot')
        df1 = df[df['SOURCE'] == 'in']
        df1 = df1.mean(numeric_only=True)
        sns.barplot(ax= axes[0],x=df1.index[:-1], y=df1.values[:-1])
        axes[0].set_title('Median of inpatient')
        df2 = df[df['SOURCE'] == 'out']
        df2 = df2.mean(numeric_only=True)
        sns.barplot(ax=axes[1],x=df2.index[:-1], y=df2.values[:-1])
        axes[1].set_title('Median of outpatient')
        plt.show()
    except Exception as err:
            print(err)

def treatment_thrombocyte():
    try:
        df = pd.read_csv('./get_report/treatment.csv')
        df1 = df[df['SOURCE'] == 'in']
        fig,axes = plt.subplots(1,2,sharey=True,figsize=(12,8))
        fig.suptitle('Treatment thrombocyte plot')
        sns.histplot(ax=axes[0], data=df1['THROMBOCYTE'], color="blue", label="100% Equities", kde=True, stat="density",
                     linewidth=0)
        axes[0].set_title('thrombocyte of inpatient')
        df2 = df[df['SOURCE'] =='out']
        sns.histplot(ax=axes[1], data=df2['THROMBOCYTE'], color="blue", label="100% Equities", kde=True, stat="density",
                     linewidth=0)
        axes[1].set_title('thrombocyte of outpatient')
        plt.show()
    except Exception as err:
            print(err)

def treatment_pie():
    try:
        df = pd.read_csv('./get_report/treatment.csv')
        df1 = df[df['SOURCE'] == 'in']
        df2 = df[df['SOURCE'] == 'out']
        sub = ['Inpatient','Outpatient']
        per = [len(df1)/len(df),len(df2)/len(df)]
        sns.set(font_scale=1.2)
        plt.figure(figsize=(8, 8))
        plt.pie(
            x=per,
            labels=sub,
            autopct='%1.2f%%',
            colors=sns.color_palette('Paired'),
            explode=[0.05, 0.05]
        )
        plt.show()
    except Exception as err:
        print(err)


def max_value():
    df = pd.read_csv('./get_report/treatment.csv')
    df = df.drop(columns=['SOURCE','SEX'])
    df = df.values
    print(df.max())

if __name__ == "__main__":
    max_value()
