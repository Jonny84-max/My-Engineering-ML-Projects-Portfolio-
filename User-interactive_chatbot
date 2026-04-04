import datetime  # to get current date and time
import streamlit as st  # to create the chatbot interface
import gradio as gr     # gradio interface  

# Common title and description
Title_ = "Python_Chatbot"
Description_ = "A simple chatbot that greets you and shows the current date and time in WAT."

# simple function that takes user's name and responds
def Python_Chatbot(name):
    wat = datetime.timezone(datetime.timedelta(hours=1))  # set timezone to West Africa Time (UTC+1)
    now = datetime.datetime.now(wat) # get current time in WAT
    date = now.strftime('%B %d, %Y')
    time = now.strftime('%I:%M %p')
    return f"Nice to meet you, {name}! Today's date is {date} and the current time in WAT is {time}." # return greeting + current date and time
    
# Streamlit interface
def run():
    st.title(Title_)
    st.text(Description_)  # reuse common description
    name = st.text_input("Hello! What is your name?")   # Get user input
    if name:
        response = Python_Chatbot(name)  # Respond when button is pressed
        st.text(response)   # chatbot reply

# Gradio Interface
def run_gradio():
    iface = gr.Interface(
        fn=Simple_chatbot,
        inputs=gr.Textbox(label="Hello! What is your name?"),
        outputs=gr.Textbox(label="Response"),
        title="Python_Chatbot (Gradio)",
        description="descripton_"  # reuse common description
    )
    iface.launch()  # Launch Gradio app

# Choose Platform
platform = "streamlit"  # change to "gradio" to run Gradio instead
if platform.lower() == "gradio":
    run_gradio()
elif platform.lower() == "streamlit":
    run_streamlit()
else:
    print("Unknown platform! Choose 'gradio' or 'streamlit'.")
