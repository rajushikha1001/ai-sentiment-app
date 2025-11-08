import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load data
data = pd.read_csv("../../data/raw/tweets.csv", 
                   encoding='latin-1',
                   names=['target', 'id', 'date', 'flag', 'user', 'text'])

# Convert numeric target to labels
data['sentiment'] = data['target'].map({0: 'negative', 4: 'positive'})

X = data['text']
y = data['sentiment']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words='english')),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)

# Evaluate
print("Accuracy:", model.score(X_test, y_test))

# Save model
joblib.dump(model, "../models/sentiment_model.pkl")
print("✅ Model saved to models/sentiment_model.pkl")
