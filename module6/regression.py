# notes
# Linear Regression
'''
used to analyze the relationship between two variable i.e independent(x) and dependent(y)
shows how change in independent affects dependent variable
works by finding best-fitting line that minimizes the diff betN the observed data and the predicted value
-- through a process called ordinary least squares(ols)
ols calculates optimal value for intercept Bo and slope B1 of the line that minimizes sum of 
squared errors between predicted value and actual data point
mathematically, y = Bo + B1(x)
y = dependent variable, 
x = independent,
Bo = y-intercept (value of y when x is zero),
B1 = slope of regression line (change in y for one unit change in x)
'''

'''
use case
predicting sales based of advertise speed
predicting price of house
'''

import numpy as np
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 3 * x ** 2 + 2 * x + np.random.normal(0, 10, 100)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
x_train = x_train.reshape(-1, 1)     # reshaping x_train to 2D array
model.fit(x_train, y_train)

x_test = x_test.reshape(-1, 1)
y_pred = model.predict(x_test)

print(x_train.shape, x_test.shape)       # (80,1)   and (20,1)
print(y_pred.shape)                       # (20,)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_test.flatten(), y=y_test, mode="markers", name="Actual Data"))
fig.add_trace(go.Scatter(x=x_test.flatten(), y=y_pred, mode="lines", name="Linear Regression Line"))

fig.update_layout(title="Linear Regression", xaxis_title="Independent variable(x)", yaxis_title="Dependent variable")
fig.show()