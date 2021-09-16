import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

pd.options.mode.chained_assignment = None  # default='warn'

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
        f1_scores.append(f1_score(y_test, y_pred))
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


file_path = 'credit_datasheet_head.csv'
credit_data = pd.read_csv(file_path)
print(credit_data.shape)
credit_data = change_data(credit_data)
features = ['step', 'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig',
            'oldbalanceDest', 'newbalanceDest']

X = credit_data[features].values
y = credit_data['isFraud'].values

kf = KFold(n_splits=10, shuffle=True)

final_model = LogisticRegression(max_iter=200000)
final_model.fit(X, y)
score_model(X, y, kf)
