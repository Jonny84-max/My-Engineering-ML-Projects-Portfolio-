import streamlit as st
import NNIT_students_chatbot    # copy code from NNIT-Students-Support-System
import predictive_maintenance_marine_engine  # copy code from NNIT-Students-Support-System
import hull_biofouling_Prediction    # copy code from NNIT-Students-Support-System
import user_interactive_chatbot     # copy code from Python_Chatbot

st.title("My Engineering ML Projects Portfolio")
st.sidebar.title("Select a Project")

choice = st.sidebar.radio("Projects:", [
    "NNIT Student Support System",
    "Predictive Maintenance for Marine Engines",
    "Hull Biofouling Predictor and Optimizer",
    "User-Friendly Interactive Chatbot"
])

if choice == "NNIT Student Support System":
    NNIT_students_chatbot.run()
elif choice == "Predictive Maintenance for Marine Engines":
    predictive_maintenance_marine_engine.run()
elif choice == "Hull Biofouling Predictor and Optimizer":
    hull_biofouling_Prediction.run()
elif choice == "User-Friendly Interactive Chatbot":
    user_interactive_chatbot.run()
