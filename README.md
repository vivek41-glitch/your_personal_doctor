# your_personal_doctor
This is ML application in which user enter symtoms and model predict which diseas he have and also which medicine user should take .

Mini Doctor 

Symptom-Based Disease Prediction Using Machine Learning
Overview

Mini Doctor is a machine learning project that predicts possible diseases based on user-entered symptoms.
Along with disease prediction, the system also provides basic remedies or suggestions to overcome the condition.

This project is built for learning and demonstration purposes, not for real medical diagnosis.

How It Works

The user enters symptoms in text form

The input text is processed using text vectorization

A Naive Bayes classification model predicts the most likely disease

The system displays:

Predicted disease

Related remedies or suggestions (medicines, precautions, etc.)

Technologies Used

Python

Pandas

NumPy

Scikit-learn

Naive Bayes (Text Classification)

Streamlit (for UI)

Machine Learning Details

Learning Type: Supervised Learning

Problem Type: Multi-class Classification

Model Used: Naive Bayes

Text Processing: Scikit-learn text vectorization (used for symptom text)

Input Feature: Symptoms (text)

Output: Disease label + remedies

Features

Text-based symptom input

Disease prediction using ML

Remedy suggestions for predicted disease

Simple and interactive UI using Streamlit

Easy to understand workflow

Project Structure (Example)
├── app.py              # Streamlit application
├── dataset.csv         # Symptom, disease, remedy data
├── model.pkl           # Trained Naive Bayes model
├── vectorizer.pkl      # Text vectorizer
├── requirements.txt
└── README.md

How to Run the Project

Clone the repository

git clone <repo-link>


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py

Limitations

This is not a medical tool

Predictions depend on dataset quality

Remedies are general suggestions, not prescriptions

Cannot replace professional medical advice

Learning Outcomes

Text classification using Naive Bayes

Handling symptom text data

End-to-end ML pipeline

Building ML apps with Streamlit

Understanding real-world ML constraints

Future Improvements

Add more diseases and symptoms

Improve accuracy using advanced NLP models

Add confidence scores

Deploy the app online

Disclaimer

This project is created only for educational purposes.
Do not use it for real medical decisions.
