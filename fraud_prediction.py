import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

pd.options.mode.chained_assignment = None  # default='warn'
final_model = LogisticRegression(max_iter=200000)


def score_model(X, y, kf):
    accuracy_scores = []
    precision_scores = []
    recall_scores = []
    f1_scores = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model = LogisticRegression(max_iter=200000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy_scores.append(accuracy_score(y_test, y_pred))
        precision_scores.append(precision_score(y_test, y_pred))
        recall_scores.append(recall_score(y_test, y_pred))
        f1_scores.append(f1_score(y_test, y_pred, average='weighted', labels=np.unique(y_pred)))
    print("accuracy:", np.mean(accuracy_scores))
    print("precision:", np.mean(precision_scores))
    print("recall:", np.mean(recall_scores))
    print("f1 score:", np.mean(f1_scores))


def change_data(credit):
    for i in range(0, len(credit['type'])):
        if credit['type'][i] == 'PAYMENT':
            credit['type'][i] = 0
        elif credit['type'][i] == 'DEBIT':
            credit['type'][i] = 1
        elif credit['type'][i] == 'CASH_OUT':
            credit['type'][i] = 2
        elif credit['type'][i] == 'TRANSFER':
            credit['type'][i] = 3
        elif credit['type'][i] == 'CASH_IN':
            credit['type'][i] = 4
    return credit


def view_data():
    file_path = 'credit_datasheet_head.csv'
    credit_data = pd.read_csv(file_path)

    def encode_type(x):
        if x == 'PAYMENT':
            return 1
        elif x == 'DEBIT':
            return 2
        elif x == 'CASH_OUT':
            return 3
        elif x == 'TRANSFER':
            return 4
        elif x == 'CASH_IN':
            return 5

    credit_data['type'] = [encode_type(x) for x in credit_data['type']]
    print(credit_data.describe())
    np.savetxt('myfile.csv', credit_data.describe(), delimiter=',', fmt='%.2f')
    amount_data = credit_data['amount']
    with open('view_data.txt', 'a') as the_file:
        the_file.write(str(np.median(amount_data)) + '\n')
        the_file.write(str(np.mean(amount_data)) + '\n')
        the_file.write(str(np.percentile(amount_data, 25)) + '\n')
        the_file.write(str(np.percentile(amount_data, 75)) + '\n')
        the_file.write(str(np.percentile(amount_data, 50)) + '\n')
        the_file.write(str(np.std(amount_data)) + '\n')
        the_file.write(str(np.var(amount_data)) + '\n')
    plot_data(credit_data)


def plot_data(data):
    plt.scatter(data['amount'], data['type'], c=data['isFraud'])
    plt.title('Amount and type graph')
    plt.xlabel('Amount')
    # 1 -> PAYMENT
    # 2 -> DEBIT
    # 3 -> CASH_OUT
    # 4 -> TRANSFER
    # 5 -> CASH_IN
    plt.ylabel('Type')
    plt.show()


def fit_model():
    file_path = 'credit_datasheet_head.csv'
    credit_data = pd.read_csv(file_path)
    credit_data = change_data(credit_data)
    features = ['step', 'type', 'amount', 'oldbalanceOrg', 'oldbalanceDest']

    x = credit_data[features].values
    y = credit_data['isFraud'].values
    final_model.fit(x, y)
    print('The coefficients are:')
    print(final_model.coef_, final_model.intercept_)
    print(final_model.score(x, y))

    # kf = KFold(n_splits=10, shuffle=True)
    # score_model(X, y, kf)


view_data()
