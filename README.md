# Emotion AI System (Local ML Pipeline)

## 📌 Overview

This project builds a local machine learning system that analyzes user journal text and predicts emotional state, intensity, and suggests actions.

The system is fully local (no APIs used) and handles messy real-world input.

---

## ⚙️ Approach

1. Load training data from `train.csv`
2. Clean text (lowercase, remove special characters)
3. Convert text into numerical features using TF-IDF
4. Combine text features with numeric features (stress level)
5. Train:

   * Classification model → emotional state
   * Regression model → intensity
6. Predict on test data
7. Apply decision logic to suggest actions

---

## 🧠 Feature Engineering

* Text cleaning using regex
* TF-IDF vectorization
* Numeric feature used:

  * stress_level
* Combined features using sparse matrix

---

## 🤖 Model Choice

* RandomForestClassifier → for emotion prediction
* RandomForestRegressor → for intensity prediction

Reason:

* Works well on small datasets
* Handles mixed features (text + numeric)
* Robust to noise

---

## 📊 Output

The system generates `predictions.csv` with:

* predicted_state
* predicted_intensity
* confidence
* uncertain_flag
* what_to_do
* when_to_do

---

## ⚠️ Handling Edge Cases

### 1. Very Short Text

* Still processed using TF-IDF
* Relies more on numeric features

### 2. Missing Values

* Filled with default values (0)

### 3. Contradictory Inputs

* Confidence score used
* uncertain_flag = 1 if confidence < 0.6

---

## ▶️ How to Run

1. Install dependencies:

```
pip install pandas scikit-learn
```

2. Run:

```
python main.py
```

3. Output file:

```
predictions.csv
```

---

## 🚀 Conclusion

This system not only predicts emotions but also provides actionable suggestions, making it practical and user-focused.

---
