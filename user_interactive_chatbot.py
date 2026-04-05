# user_interactive_chatbot.py
import datetime

# For Streamlit
import streamlit as st
# For Gradio
import gradio as gr

# --- Core chatbot logic ---
def chatbot_response(name):
    """Generates greeting with current WAT date/time."""
    wat = datetime.timezone(datetime.timedelta(hours=1))  # UTC+1
    now = datetime.datetime.now(wat)
    date = now.strftime('%B %d, %Y')
    time = now.strftime('%I:%M %p')
    return f"Nice to meet you, {name}! Today's date is {date} and the current time in WAT is {time}."

# --- Streamlit interface ---
def run_streamlit():
    st.title("Python Chatbot")
    st.write("A simple chatbot that greets you and shows current date/time in WAT.")
    
    name = st.text_input("Hello! What is your name?")
    if name:
        response = chatbot_response(name)
        st.write(response)

# --- Gradio interface ---
def run_gradio():
    iface = gr.Interface(
        fn=chatbot_response,
        inputs=gr.Textbox(label="Hello! What is your name?"),
        outputs=gr.Textbox(label="Response"),
        title="Python Chatbot (Gradio)",
        description="A simple chatbot that greets you and shows current date/time in WAT."
    )
    iface.launch()

# --- Unified run function ---
def run(platform="streamlit"):
    """
    Run the chatbot app. 
    platform: "streamlit" or "gradio"
    """
    platform = platform.lower()
    if platform == "streamlit":
        run_streamlit()
    elif platform == "gradio":
        run_gradio()
    else:
        raise ValueError("Unknown platform! Choose 'streamlit' or 'gradio'.")
