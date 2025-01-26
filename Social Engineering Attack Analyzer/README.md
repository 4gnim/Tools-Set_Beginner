# Social Engineering Attack Analyzer 🔍

Social Engineering Attack Analyzer is a simple Python-based tool designed to detect potential social engineering attacks in text, such as phishing emails or suspicious messages. The program uses **machine learning** with a Naive Bayes model to classify messages as safe or suspicious.

## Features 🚀

- Detect suspicious messages using text-based machine learning.
- Train and predict using **Scikit-learn**.
- Interactive CLI to analyze user-provided text in real-time.

## How It Works ⚙️

1. The program uses a small dataset to train the model.
2. Features are extracted from the text using **Bag of Words** (CountVectorizer).
3. The trained machine learning model classifies text as:
   - **1**: Suspicious (potential social engineering attack).
   - **0**: Safe.

## Requirements 🛠️

Ensure you have Python and the following libraries installed:

- **Scikit-learn**
- **Joblib**

Install the dependencies using the following command:

```bash
pip install scikit-learn joblib
```
