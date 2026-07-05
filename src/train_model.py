import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("data/dataset.csv")

# Features (input)
X = data[["failed_logins", "session_duration", "unusual_activity"]]

# Label (output)
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create AI model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Test example
test_input = pd.DataFrame(
    [[7, 3, 1]],
    columns=["failed_logins", "session_duration", "unusual_activity"]
)

prediction = model.predict(test_input)
if prediction[0] == 1:
    print("🚨 Intrusion Detected")
else:
    print("✅ Normal Activity")