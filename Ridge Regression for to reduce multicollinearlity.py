import pandas as pd
import numpy as np
from statsmodels.api import formula
from statsmodels.formula.api import ols
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plp
import seaborn as sns

data_ceosal = pd.read_csv("C:\\Users\\darioylauri\\Desktop\\CEOSAL2.CSV")
data_ceosal = data_ceosal.drop(["Unnamed: 0", "lsalary", "lsales", "lmktval"], axis = 1)


formula = "salary ~ age+college+grad+comten+ceoten+sales+profits+mktval+comtensq+ceotensq+profmarg"
model_ceosal = ols(formula, data_ceosal).fit()
model_ceosal.summary()

sns.heatmap(data_ceosal.corr(), square = True)

''' The model indicate that are strong multicollinearity. Then, we will
use the Ridge regression '''


X_matrix = data_ceosal.drop(["salary"], axis = 1).to_numpy()
Y_matrix = np.array(data_ceosal["salary"]).reshape(len(data_ceosal), 1)

X_train, X_test, Y_train, Y_test = train_test_split(X_matrix, Y_matrix, train_size = 0.7)

model1 = linear_model.LinearRegression()
model1.fit(X_train, Y_train)
model1.score(X_train, Y_train)
model1.score(X_test, Y_test)

model2 = linear_model.RidgeCV(store_cv_values = True)
model2.fit(X_train, Y_train)
model2.coef_
model2.score(X_train, Y_train)
model2.score(X_test, Y_test)


data_coefficients = pd.DataFrame(data = {"Name": list(data_ceosal.drop(["salary"], axis = 1).columns), "Values": list(model2.coef_[0])})

