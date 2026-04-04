import streamlit as st
import nnit_students_chatbot
import predictive_maintenance_marine_engine
import hull_biofouling_prediction
import user_interactive_chatbot

st.title("My Engineering ML Projects Portfolio")
st.sidebar.title("Select a Project")

choice = st.sidebar.radio("Projects:", [
    "NNIT Student Support System",
    "Predictive Maintenance for Marine Engines",
    "Hull Biofouling Predictor and Optimizer",
    "User-Friendly Interactive Chatbot"
])

if choice == "NNIT Student Support System":
    import nnit_students_chatbot

elif choice == "Predictive Maintenance for Marine Engines":
    import predictive_maintenance_marine_engine

elif choice == "Hull Biofouling Predictor and Optimizer":
    import hull_biofouling_prediction

elif choice == "User-Friendly Interactive Chatbot":
    import user_interactive_chatbot
