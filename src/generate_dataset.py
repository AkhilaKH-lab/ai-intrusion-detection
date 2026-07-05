import numpy as np
import pandas as pd

np.random.seed(42)
n_samples = 300
half = n_samples // 2

# Normal behavior (label 0) — overlapping distributions, not hard cutoffs
normal_failed_logins = np.clip(np.random.normal(loc=2, scale=1.5, size=half), 0, None).round().astype(int)
normal_session_duration = np.clip(np.random.normal(loc=18, scale=6, size=half), 0, None).round(1)
normal_unusual_activity = np.random.binomial(1, 0.15, size=half)
normal_labels = np.zeros(half, dtype=int)

# Intrusion behavior (label 1)
intrusion_failed_logins = np.clip(np.random.normal(loc=6, scale=2.5, size=half), 0, None).round().astype(int)
intrusion_session_duration = np.clip(np.random.normal(loc=7, scale=4, size=half), 0, None).round(1)
intrusion_unusual_activity = np.random.binomial(1, 0.65, size=half)
intrusion_labels = np.ones(half, dtype=int)

df = pd.DataFrame({
    "failed_logins": np.concatenate([normal_failed_logins, intrusion_failed_logins]),
    "session_duration": np.concatenate([normal_session_duration, intrusion_session_duration]),
    "unusual_activity": np.concatenate([normal_unusual_activity, intrusion_unusual_activity]),
    "label": np.concatenate([normal_labels, intrusion_labels]),
})
df.insert(0, "student_id", [f"student_{i:04d}" for i in range(len(df))])
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv("data/dataset.csv", index=False)
print(f"Generated {len(df)} rows -> data/dataset.csv")