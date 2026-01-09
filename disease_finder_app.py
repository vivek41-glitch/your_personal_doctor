import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load model, vectorizer, dataset
# -------------------------------
model = pickle.load(open('disease_nb_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
df = pd.read_csv('medicine_finder_dataset.csv') 

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="🩺 Mini Docter App", page_icon="💊", layout="wide")

st.title("🩺 Mini Docter App")
st.write("Enter your symptoms and get a predicted disease with suggested remedy/medicine.")

# User input
user_input = st.text_area("Enter your symptoms (separated by commas):", "")

if st.button("Predict Disease"):
    if user_input.strip() == "":
        st.warning("Please enter your symptoms before predicting.")
    else:
        user_vector = vectorizer.transform([user_input])
        prediction = model.predict(user_vector)[0]
        remedy = df[df["Disease"] == prediction]["Medicine/Remedy"].values[0]
        
        st.success(f"**Predicted Disease:** {prediction}")
        st.info(f"**Suggested Remedy/Medicine:** {remedy}")     