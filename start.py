from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


# Load Dataframe from csv
df = pd.read_csv("insurance.csv")

# Define model. Specify a number for random_state to ensure same results each run
dec_model = DecisionTreeRegressor(random_state=1)

# Set target variable
y = df["charges"]

# Set features
X = df[["age", "bmi", "children"]]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# Fit model
dec_model.fit(train_X, train_y)

val_predictions = dec_model.predict(val_X)

