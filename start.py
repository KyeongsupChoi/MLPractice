from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn import tree


# Load Dataframe from csv
df = pd.read_csv("insurance.csv")

# Define model. Specify a number for random_state to ensure same results each run
dec_model = DecisionTreeRegressor(random_state=1)

# Set target variable
y = df["charges"]

# Set features
X = df[["age", "bmi", "children"]]

# Test split
train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.3, random_state=0)

# Fit model
dec_model.fit(train_X, train_y)

tree.export_graphviz(dec_model,out_file='tree.dot')

val_predictions = dec_model.predict(val_X)

print(val_predictions)
print(list(val_y))

print(df)