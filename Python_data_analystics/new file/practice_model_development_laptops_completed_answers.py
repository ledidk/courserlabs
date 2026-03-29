import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# =========================
# Load dataset (local file expected after notebook download step)
# =========================
df = pd.read_csv("laptops.csv", header=0)

# Shared target
Y = df['Price']

# =========================
# Task 1: Single Linear Regression
# =========================
lm = LinearRegression()
X = df[['CPU_frequency']]
lm.fit(X, Y)
Yhat = lm.predict(X)

ax1 = sns.distplot(df['Price'], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values", ax=ax1)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
plt.legend(['Actual Value', 'Predicted Value'])
plt.show()

mse_slr = mean_squared_error(df['Price'], Yhat)
r2_score_slr = lm.score(X, Y)
print('Task 1 - The R-square for Linear Regression is: ', r2_score_slr)
print('Task 1 - The mean square error of price and predicted value is: ', mse_slr)

# =========================
# Task 2: Multiple Linear Regression
# =========================
lm1 = LinearRegression()
Z = df[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core', 'OS', 'GPU', 'Category']]
lm1.fit(Z, Y)
Y_hat = lm1.predict(Z)

ax2 = sns.distplot(df['Price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values", ax=ax2)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
plt.legend(['Actual Value', 'Predicted Value'])
plt.show()

mse_mlr = mean_squared_error(Y, Y_hat)
r2_mlr = r2_score(Y, Y_hat)
print('Task 2 - MSE for Multiple Linear Regression is: ', mse_mlr)
print('Task 2 - R^2 for Multiple Linear Regression is: ', r2_mlr)

# =========================
# Task 3: Polynomial Regression
# =========================
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(independent_variable.min(), independent_variable.max(), 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title(f'Polynomial Fit for Price ~ {Name}')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    plt.xlabel(Name)
    plt.ylabel('Price of laptops')
    plt.show()

X_poly = X.to_numpy().flatten()

f1 = np.polyfit(X_poly, Y, 1)
p1 = np.poly1d(f1)

f3 = np.polyfit(X_poly, Y, 3)
p3 = np.poly1d(f3)

f5 = np.polyfit(X_poly, Y, 5)
p5 = np.poly1d(f5)

PlotPolly(p1, X_poly, Y, 'CPU_frequency')
PlotPolly(p3, X_poly, Y, 'CPU_frequency')
PlotPolly(p5, X_poly, Y, 'CPU_frequency')

r_squared_1 = r2_score(Y, p1(X_poly))
mse_1 = mean_squared_error(Y, p1(X_poly))
print('Task 3 - The R-square value for 1st degree polynomial is: ', r_squared_1)
print('Task 3 - The MSE value for 1st degree polynomial is: ', mse_1)

r_squared_3 = r2_score(Y, p3(X_poly))
mse_3 = mean_squared_error(Y, p3(X_poly))
print('Task 3 - The R-square value for 3rd degree polynomial is: ', r_squared_3)
print('Task 3 - The MSE value for 3rd degree polynomial is: ', mse_3)

r_squared_5 = r2_score(Y, p5(X_poly))
mse_5 = mean_squared_error(Y, p5(X_poly))
print('Task 3 - The R-square value for 5th degree polynomial is: ', r_squared_5)
print('Task 3 - The MSE value for 5th degree polynomial is: ', mse_5)

# =========================
# Task 4: Pipeline
# =========================
Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]

pipe = Pipeline(Input)

Z_float = Z.astype(float)
pipe.fit(Z_float, Y)
ypipe = pipe.predict(Z_float)

print('Task 4 - MSE for multi-variable polynomial pipeline is: ', mean_squared_error(Y, ypipe))
print('Task 4 - R^2 for multi-variable polynomial pipeline is: ', r2_score(Y, ypipe))
