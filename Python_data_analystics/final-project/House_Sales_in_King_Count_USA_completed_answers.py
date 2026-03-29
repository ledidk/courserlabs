import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split

# =========================
# Load Data
# =========================
# Make sure housing.csv is available locally (downloaded in notebook environment)
df = pd.read_csv("housing.csv")

# =========================
# Question 1
# Display data types of each column
# =========================
print("Q1: Data types")
print(df.dtypes)

# =========================
# Question 2
# Drop "id" and "Unnamed: 0", then describe
# =========================
df.drop(["id", "Unnamed: 0"], axis=1, inplace=True)
print("\nQ2: Statistical summary after dropping id and Unnamed: 0")
print(df.describe())

# Replace missing values in bedrooms and bathrooms (as notebook flow expects)
mean_bedrooms = df['bedrooms'].mean()
df['bedrooms'] = df['bedrooms'].fillna(mean_bedrooms)

mean_bathrooms = df['bathrooms'].mean()
df['bathrooms'] = df['bathrooms'].fillna(mean_bathrooms)

# =========================
# Question 3
# Count houses with unique floor values
# =========================
print("\nQ3: Floor counts")
print(df['floors'].value_counts().to_frame())

# =========================
# Question 4
# Boxplot for waterfront vs price
# =========================
plt.figure(figsize=(8, 6))
sns.boxplot(x='waterfront', y='price', data=df)
plt.title('House Price by Waterfront View')
plt.xlabel('Waterfront')
plt.ylabel('Price')
plt.show()

# =========================
# Question 5
# Regplot for sqft_above vs price
# =========================
plt.figure(figsize=(10, 6))
sns.regplot(x='sqft_above', y='price', data=df, line_kws={"color": "red"})
plt.title('sqft_above vs price')
plt.xlabel('sqft_above')
plt.ylabel('price')
plt.show()

# Correlation check (as notebook guidance)
df_numeric = df.select_dtypes(include=[np.number])
print("\nCorrelation with price:")
print(df_numeric.corr()['price'].sort_values())

# =========================
# Question 6
# Linear Regression using sqft_living -> price
# =========================
X_q6 = df[['sqft_living']]
Y = df['price']

lm_q6 = LinearRegression()
lm_q6.fit(X_q6, Y)
r2_q6 = lm_q6.score(X_q6, Y)
print("\nQ6: R^2 using sqft_living:", r2_q6)

# =========================
# Question 7
# Multiple Linear Regression with provided features
# =========================
features = ["floors", "waterfront", "lat", "bedrooms", "sqft_basement", "view",
            "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"]

X_q7 = df[features]
lm_q7 = LinearRegression()
lm_q7.fit(X_q7, Y)
r2_q7 = lm_q7.score(X_q7, Y)
print("Q7: R^2 using multiple features:", r2_q7)

# =========================
# Question 8
# Pipeline: scale + polynomial + linear model
# =========================
Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]

pipe = Pipeline(Input)
pipe.fit(X_q7, Y)
r2_q8 = pipe.score(X_q7, Y)
print("Q8: R^2 using pipeline:", r2_q8)

# =========================
# Train/test split for Q9 and Q10
# =========================
x_train, x_test, y_train, y_test = train_test_split(X_q7, Y, test_size=0.15, random_state=1)

print("\nnumber of test samples:", x_test.shape[0])
print("number of training samples:", x_train.shape[0])

# =========================
# Question 9
# Ridge regression alpha=0.1 on train/test
# =========================
ridge_q9 = Ridge(alpha=0.1)
ridge_q9.fit(x_train, y_train)
r2_q9 = ridge_q9.score(x_test, y_test)
print("Q9: R^2 Ridge on test data:", r2_q9)

# =========================
# Question 10
# 2nd order polynomial transform + Ridge(alpha=0.1)
# =========================
pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.transform(x_test)

ridge_q10 = Ridge(alpha=0.1)
ridge_q10.fit(x_train_pr, y_train)
r2_q10 = ridge_q10.score(x_test_pr, y_test)
print("Q10: R^2 Polynomial(2) + Ridge on test data:", r2_q10)
