from src.data_loader import load_data
from src.preprocess import add_rul, create_label
from src.model import train_model
from src.predict import load_model, predict

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Load data
data = load_data("data/train_FD001.txt")

# Preprocess
data = add_rul(data)
data = create_label(data)

# Features (keep it simple)
X = data[['sensor2', 'sensor3', 'sensor4', 'sensor7', 'sensor11']]
y = data['failure']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = train_model(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, preds)
print(f"Accuracy: {acc}")

# Save predictions
output = pd.DataFrame({
    "Actual": y_test,
    "Predicted": preds
})
output.to_csv("outputs/predictions.csv", index=False)
