import re
import joblib
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dataset kecil: URL dan label (1 = phishing, 0 = aman)
data = [
    ("http://secure-login.bank.com", 0),
    ("https://paypal-secure.com/login", 1),
    ("http://example.com/home", 0),
    ("https://free-gift-card.com", 1),
    ("http://mybank.secure-update.com", 1),
    ("https://github.com/login", 0),
]

# Ekstrak URL dan label
urls, labels = zip(*data)

# Fitur sederhana: Panjang URL dan jumlah karakter spesial
def extract_features(url):
    return [len(url), len(re.findall(r'[?&=]', url))]

# Ubah data menjadi fitur
features = np.array([extract_features(url) for url in urls])
labels = np.array(labels)

# Bagi data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Train model sederhana (Naive Bayes)
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediksi pada data testing
y_pred = model.predict(X_test)
print("Akurasi:", accuracy_score(y_test, y_pred))

# Simpan model dan fungsi ekstraksi
joblib.dump(model, "phishing_detector.pkl")
joblib.dump(extract_features, "feature_extractor.pkl")

# ==== Tool sederhana untuk mendeteksi phishing ====
print("\n=== Phishing Link Detector ===")

# Load model dan fungsi ekstraksi
model = joblib.load("phishing_detector.pkl")
extract_features = joblib.load("feature_extractor.pkl")

# Input URL untuk deteksi
while True:
    user_url = input("Masukkan URL (atau ketik 'exit' untuk keluar): ")
    if user_url.lower() == "exit":
        break
    user_features = np.array([extract_features(user_url)])
    prediction = model.predict(user_features)[0]
    if prediction == 1:
        print("⚠️ URL ini terdeteksi sebagai *phishing*!")
    else:
        print("✅ URL ini aman.")
