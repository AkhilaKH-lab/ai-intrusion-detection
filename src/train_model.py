import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from privacy_utils import pseudonymize

# Load dataset
data = pd.read_csv("data/dataset.csv")

# Protect student identity immediately — before any further processing or logging
data["student_id_hash"] = data["student_id"].apply(pseudonymize)
data = data.drop(columns=["student_id"])

# Features (input)
X = data[["failed_logins", "session_duration", "unusual_activity"]]

# Label (output)
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Create AI model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Normal", "Intrusion"]))

# Privacy-aware alerting: identify flagged students without exposing real identities
test_student_hashes = data.loc[X_test.index, "student_id_hash"]
flagged = test_student_hashes[y_pred == 1]
print("\nFlagged student pseudonyms (raw identities never exposed):")
print(flagged.tolist())


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