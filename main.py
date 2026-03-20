import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from scipy.sparse import hstack

# Load train data
df = pd.read_csv("train.csv")

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def decide_action(emotion, intensity, stress, energy):
    if stress > 7:
        return "breathing", "now"
    elif energy < 3:
        return "rest", "now"
    elif emotion == "sad":
        return "journaling", "later_today"
    elif emotion == "happy":
        return "deep_work", "now"
    else:
        return "walk", "within_15_min"
df['clean_text'] = df['journal_text'].apply(clean_text)

# Features
tfidf = TfidfVectorizer()
X_text = tfidf.fit_transform(df['clean_text'])
X_num = df[['stress_level']]
X = hstack([X_text, X_num])

# Train model
model = RandomForestClassifier()
model.fit(X, df['emotional_state'])

from sklearn.ensemble import RandomForestRegressor

model_intensity = RandomForestRegressor()
model_intensity.fit(X, df['intensity'])

# Load test data
test = pd.read_csv("test.csv")
test['clean_text'] = test['journal_text'].apply(clean_text)

X_text_test = tfidf.transform(test['clean_text'])
X_num_test = test[['stress_level']]
X_test = hstack([X_text_test, X_num_test])

# Predict
pred = model.predict(X_test)
pred_intensity = model_intensity.predict(X_test)
probs = model.predict_proba(X_test)
confidence = probs.max(axis=1)
uncertain_flag = (confidence < 0.6).astype(int)
actions = []
times = []

for i in range(len(test)):
    action, when = decide_action(
        pred[i],
        pred_intensity[i],
        test['stress_level'].iloc[i],
        test['energy_level'].iloc[i]
    )
    actions.append(action)
    times.append(when)
# Save CSV
output = pd.DataFrame({
    "id": test["id"],
    "predicted_state": pred,
    "predicted_intensity": pred_intensity,
    "confidence": confidence,
    "uncertain_flag": uncertain_flag,
    "what_to_do": actions,
    "when_to_do": times
})

output.to_csv("predictions.csv", index=False)

print("✅ predictions.csv created")