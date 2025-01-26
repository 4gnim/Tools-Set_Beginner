import re
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Sample Dataset
# A dataset of text samples and their labels: 1 = suspicious, 0 = safe
data = [
    ("Your account has been compromised, please reset your password immediately!", 1),
    ("Congratulations, you've won a $1,000 gift card! Click here to claim.", 1),
    ("Please verify your account to avoid deactivation.", 1),
    ("Our terms and conditions have been updated. Read more here.", 0),
    ("Weekly newsletter: Top 10 productivity tips.", 0),
    ("Your package has been shipped. Track your order here.", 0),
    ("Unusual login attempt detected. Confirm your identity.", 1),
    ("Update your payment information to avoid service interruption.", 1),
    ("Friendly reminder: Your subscription is expiring soon.", 0),
    ("Limited time offer: Get 50% off your next purchase.", 0),
]

# Split data into text and labels
texts, labels = zip(*data)

# Step 2: Feature Extraction
# Convert text into numerical features using Bag of Words (CountVectorizer)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = labels

# Step 3: Model Training
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Step 4: Save the Model and Vectorizer
joblib.dump(model, "social_engineering_analyzer.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# Step 5: Interactive Social Engineering Analyzer
print("\n=== Social Engineering Attack Analyzer ===")
print("Enter a message or email text to analyze for potential social engineering threats. Type 'exit' to quit.")

# Load the saved model and vectorizer
model = joblib.load("social_engineering_analyzer.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Interactive input loop
while True:
    user_input = input("\nEnter text to analyze: ")
    if user_input.lower() == "exit":
        print("Exiting Social Engineering Attack Analyzer. Stay safe online! 🌐")
        break
    
    # Transform user input and predict
    user_features = vectorizer.transform([user_input])
    prediction = model.predict(user_features)[0]
    
    if prediction == 1:
        print("⚠️ This message is suspicious and may be a social engineering attack.")
    else:
        print("✅ This message appears safe.")
