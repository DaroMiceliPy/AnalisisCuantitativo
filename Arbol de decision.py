import pandas as pd
import numpy as np
import matplotlib.pyplot as plp
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.tree import export_graphviz
from sklearn.tree import export_text
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

data = pd.read_csv("C:\\Users\\darioylauri\\Desktop\\hprice2.csv")
data = data.drop(["Unnamed: 0", "lprice", "lnox", "lproptax"], axis = 1)
data.dtypes

X_train, X_test, Y_train, Y_test = train_test_split(data.drop(["price"], axis = 1), data["price"])
model2 = DecisionTreeRegressor(max_depth = 2)
model2.fit(X_train, Y_train)
plot_tree(model2, feature_names = data.drop(["price"], axis = 1).columns, class_names = "Price", filled = True)
mean_squared_error(Y_test, model2.predict(X_test))






