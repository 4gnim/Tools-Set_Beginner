# Phishing Link Detector 🔗

The **Phishing Link Detector** is a simple Python-based tool to identify whether a URL is phishing or safe. This program uses a basic **machine learning** model with Naive Bayes.

## Features 🚀

- Detects phishing URLs based on URL length and special character count.
- Trains and predicts using **Scikit-learn**.
- Runs directly with user input for testing URLs.

## How It Works ⚙️

1. The program uses a small dataset to train the detection model.
2. Extracts features from URLs, such as URL length and the count of special characters (`?`, `&`, `=`).
3. The machine learning model predicts whether a URL is phishing (1) or safe (0).

## Requirements 🛠️

Ensure Python and the following libraries are installed:

- **Scikit-learn**
- **Joblib**

Install the dependencies with:

```bash
pip install scikit-learn joblib
```
