from sklearn.tree import DecisionTreeRegressor
import pandas as pd

df = pd.read_csv("insurance.csv")
melbourne_model = DecisionTreeRegressor(random_state=1)

print(df)

y = df["charges"]

X = df[["age", "bmi", "children"]]

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))