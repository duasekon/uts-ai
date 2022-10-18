from sklearn.neural_network import MLPClassifier
import pandas as pd
X = pd.read_excel('utsai.xlsx', index_col=0, header=0)
X
y = pd.read_excel(open('utsai.xlsx', 'rb'), index_col=0,
                 sheet_name='Sheet2')
y
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
         hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)
y_pred = clf.predict(X)
print(y_pred)