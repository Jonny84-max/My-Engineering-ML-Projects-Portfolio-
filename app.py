import streamlit as st
import NNIT_Students_Chatbot    # copy code from NNIT-Students-Support-System
import Predictive_maintenance_Marine_Engine  # copy code from NNIT-Students-Support-System
import hull_biofouling_Prediction    # copy code from NNIT-Students-Support-System
import User_interactive_chatbot     # copy code from Python_Chatbot

st.title("My Engineering ML Projects Portfolio")
st.sidebar.title("Select a Project")

choice = st.sidebar.radio("Projects:", [
    "NNIT Student Support System",
    "Predictive Maintenance for Marine Engines",
    "Hull Biofouling Predictor and Optimizer",
    "User-Friendly Interactive Chatbot"
])

if choice == "NNIT Student Support System":
    nnit_chatbot.run()
elif choice == "Predictive Maintenance for Marine Engines":
    marine_maintenance.run()
elif choice == "Hull Biofouling Predictor and Optimizer":
    hull_biofouling.run()
elif choice == "User-Friendly Interactive Chatbot":
    interactive_chatbot.run()
