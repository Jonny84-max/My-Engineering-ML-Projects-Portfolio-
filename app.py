# app.py - Portfolio main file
import streamlit as st

# Sidebar selection
st.sidebar.title("Select a Project")
choice = st.sidebar.radio("Projects:", [
    "NNIT Student Support System",
    "Predictive Maintenance for Marine Engines",
    "Hull Biofouling Predictor and Optimizer",
    "User-Friendly Interactive Chatbot"
])

# Load the project dynamically
if choice == "NNIT Student Support System":
    import nnit_students_chatbot  # Import runs the app
elif choice == "Predictive Maintenance for Marine Engines":
    import predictive_maintenance_marine_engine
elif choice == "Hull Biofouling Predictor and Optimizer":
    import hull_biofouling_optimizer
elif choice == "User-Friendly Interactive Chatbot":
    import interactive_chatbot

# Optional: show footer or instructions
st.sidebar.markdown("---")
st.sidebar.write("Click a project to launch it.")
