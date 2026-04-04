import streamlit as st
import nnit_students_chatbot    
import predictive_maintenance_marine_engine 
import hull_biofouling_Prediction   
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
    nnit_students_chatbot.run()
elif choice == "predictive_maintenance_marine_engines":
    predictive_maintenance_marine_engine.run()
elif choice == "hull_biofouling_prediction":
    hull_biofouling_Prediction.run()
elif choice == "User-Friendly Interactive Chatbot":
    user_interactive_chatbot.run()
