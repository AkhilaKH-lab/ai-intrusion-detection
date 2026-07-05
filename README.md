# AI-Driven Intrusion Detection System for Cloud-Based E-Learning Environments

## 📌 Project Overview

This project is a machine learning-based prototype designed to simulate an intrusion detection system for cloud-based e-learning environments. It detects suspicious user behavior based on login patterns and session activity, while protecting student identity through a pseudonymization layer.

The goal is to demonstrate how AI can be applied to enhance cybersecurity in educational platforms, without compromising user privacy.

## 🎯 Problem Statement

With the rapid growth of online learning platforms, security threats such as unauthorized access and abnormal user behavior have increased. This project aims to identify such intrusions using an AI-based classification model, while ensuring that any monitoring or alerting system respects student privacy.

## 🧠 Features

- Detects normal vs suspicious user activity using machine learning (Logistic Regression)
- Trained on a 300-sample synthetic dataset with realistic, overlapping behavior distributions (not perfectly separable — mirrors real-world ambiguity)
- Evaluated with accuracy, precision, recall, F1-score, and a confusion matrix — not accuracy alone, since missed intrusions (false negatives) matter more than false alarms in a security context
- Privacy-aware: student identities are pseudonymized (SHA-256 hashed) before any logging or output — raw identities are never exposed
- Lightweight and easy to run

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (Logistic Regression, train/test split, evaluation metrics)
- hashlib (pseudonymization / privacy layer)

## 📂 Project Structure

```
ai-intrusion-detection/
│
├── data/
│   └── dataset.csv
│
├── src/
│   ├── generate_dataset.py
│   ├── train_model.py
│   ├── privacy_utils.py
│   └── intrusion_detector.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Generate the dataset:
   ```
   python src/generate_dataset.py
   ```

3. Train and evaluate the model:
   ```
   python src/train_model.py
   ```

## 📊 Output Example

```
Model Accuracy: 0.9667

Classification Report:
              precision    recall  f1-score   support
      Normal       0.94      1.00      0.97        30
   Intrusion       1.00      0.93      0.97        30

    accuracy                           0.97        60
   macro avg       0.97      0.97      0.97        60
weighted avg       0.97      0.97      0.97        60

Flagged student pseudonyms (raw identities never exposed):
['c17ce4edc733ecc4', 'db38719e536f521a', '2fd408977b554e9e', ...]
```

## 🔒 Privacy & Security Design

Student identifiers are pseudonymized using a salted SHA-256 hash before any
processing, logging, or output. This means anyone reviewing flagged accounts
sees only an irreversible pseudonym, never the real student ID.

Note: this is pseudonymization, not formal differential privacy — it protects
identity in logs and output, but doesn't provide the mathematical noise
guarantees that differential privacy offers for aggregate statistics. That's
listed as a future improvement below.

## 🔮 Future Improvements

- REST API layer simulating the cloud-based e-learning environment
- Formal differential privacy for aggregate statistics
- Integration with a real intrusion-detection benchmark (e.g., NSL-KDD)
- Deep learning-based intrusion detection
- Web dashboard for monitoring
- Deployment on cloud platforms

## 📚 Research Relevance

This project aligns with research in:

- AI-driven cybersecurity
- Cloud security systems
- E-learning platform protection
- Intrusion detection systems (IDS)
- Privacy-preserving data processing

## 👩‍💻 Author

Akhila K H