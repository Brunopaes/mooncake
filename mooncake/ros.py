from sklearn.externals.six import StringIO
from keras.callbacks import EarlyStopping
from sklearn.tree import export_graphviz
from sklearn.metrics import r2_score
from keras.models import Sequential
from IPython.display import Image
from keras.layers import Dense

import helpers
import models

import pydotplus
import datetime
import pandas


train_path = '../data/new_train_2020-03-04.csv'
val_path = '../data/validation_2020-03-04.csv'

df = pandas.read_csv(train_path).drop(['Unnamed: 0', 'Ocorrencia'], axis=1)
df_val = pandas.read_csv(val_path).drop(['Unnamed: 0', 'Ocorrencia'], axis=1)

train, test = helpers.data_separation(df)
test, validation = helpers.data_separation(test, 0.4)

x_train, y_train = helpers.x_and_y_separation(train)
x_test, y_test = helpers.x_and_y_separation(test)
x_validation, y_validation = helpers.x_and_y_separation(validation)
x_fraud_val, y_fraud_val = helpers.x_and_y_separation(df_val)

y_train = pandas.DataFrame(y_train)
y_test = pandas.DataFrame(y_test)
y_validation = pandas.DataFrame(y_validation)
y_fraud_val = pandas.DataFrame(y_fraud_val)

# ---------------------------------------------------------- Neural Net
nn_model = Sequential()

nn_model.add(Dense(15, input_dim=29, activation='relu'))
nn_model.add(Dense(15, activation='relu'))
nn_model.add(Dense(1))

nn_model.compile(loss='mean_squared_error', optimizer='adam',
                 metrics=['accuracy'])

early_stop = EarlyStopping(monitor='loss', patience=2, verbose=1)

history = nn_model.fit(x_train, y_train, epochs=100, batch_size=1, verbose=1,
                       callbacks=[early_stop], shuffle=False)

y_train_pred_nn = nn_model.predict(x_train)
y_pred_test_nn = nn_model.predict(x_test)
y_validation_pred_nn = nn_model.predict(x_validation)
y_fraud_val_pred_nn = nn_model.predict(x_fraud_val)

print("The R2 score on the Train set is:\t{:0.3f}".format(
    r2_score(y_train, y_train_pred_nn)))

print("The R2 score on the Test set is:\t{:0.3f}".format(
    r2_score(y_test, y_pred_test_nn)))

nn_test_mse = nn_model.evaluate(x_test, y_test, batch_size=1)
print('Error: %f' % nn_test_mse)

# ---------------------------------------------------------- Tree
tree = models.TreeDecision(x_train, y_train).fit()

y_train['tree'] = tree.predict(x_train)
y_test['tree'] = tree.predict(x_test)
y_validation['tree'] = tree.predict(x_validation)
y_fraud_val['tree'] = tree.predict(x_fraud_val)

cm_tree_train = helpers.confusion_matrix(y_train, ['Fraude', 'tree'])
cm_tree_test = helpers.confusion_matrix(y_test, ['Fraude', 'tree'])
cm_tree_val = helpers.confusion_matrix(y_validation, ['Fraude', 'tree'])
cm_tree_fraud = helpers.confusion_matrix(y_fraud_val, ['Fraude', 'tree'])

feature_cols = x_train.columns
dot_data = StringIO()

export_graphviz(tree, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names=feature_cols,
                class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('../data/tree_entropy_{}.png'.format(datetime.date.today()))
Image(graph.create_png())

# ---------------------------------------------------------- RandomForest
r_forest = models.RandomForest(x_train, y_train.Fraude).fit()

y_train['r_forest'] = r_forest.predict(x_train)
y_test['r_forest'] = r_forest.predict(x_test)
y_validation['r_forest'] = r_forest.predict(x_validation)
y_fraud_val['r_forest'] = r_forest.predict(x_fraud_val)

cm_r_forest_train = helpers.confusion_matrix(y_train, ['Fraude', 'r_forest'])
cm_r_forest_test = helpers.confusion_matrix(y_test, ['Fraude', 'r_forest'])
cm_r_forest_val = helpers.confusion_matrix(y_validation, ['Fraude', 'r_forest'])
cm_r_forest_fraud = helpers.confusion_matrix(y_fraud_val, ['Fraude', 'r_forest'])
