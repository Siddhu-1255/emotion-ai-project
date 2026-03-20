# Error Analysis

## 📌 Overview

This document analyzes failure cases and limitations of the model.

---

## ❌ Failure Cases

### 1. Very Short Text

Example: "ok", "fine"

* Model lacks context
* Prediction becomes unreliable

---

### 2. Ambiguous Emotion

Example: "I am tired but happy"

* Multiple emotions present
* Model predicts only one label

---

### 3. Low Confidence Predictions

* Confidence values around 0.4–0.5
* uncertain_flag becomes 1

---

### 4. Noisy Text

Example: "hppy lol idk wat im doin"

* Slang and spelling errors affect TF-IDF

---

### 5. Contradictory Inputs

Example:

* Text: "I feel calm"
* Stress level: 9
* Conflict between text and numeric features

---

### 6. Limited Dataset

* Very small training data
* Model cannot generalize well

---

### 7. Overfitting Risk

* RandomForest may memorize small dataset

---

### 8. Missing Emotional Depth

* Intensity prediction not always accurate

---

### 9. Fixed Decision Rules

* Action logic is rule-based, not learned
* May not fit all users

---

### 10. Language Limitation

* Only English text supported

---

## 💡 Insights

* Confidence score is critical for reliability
* Combining text + numeric features improves results
* Rule-based decisions provide safety fallback

---

## 🚀 Improvements

* Use larger dataset
* Add spell correction
* Use advanced NLP models (BERT)
* Personalization for users
* Better uncertainty handling

---
