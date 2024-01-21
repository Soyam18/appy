from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=os.get_env("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(questions):
    response=chat.send_messages(questions,stream=True)
    return response

st.set_page_config("Q&A Chatbot")
st.header("Conversational ChatBot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("input: ", key="input")
submit=st.button("send")

if input and submit:
     response=get_gemini_response(input)
     st.session_state['chat_history'].append(("You, input"))
     st.subheader("Response: ")
     for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Response", chunk.text))

st.subheader("chat_history")
for role, response in st.session_state['chat_history']:
    st.write(f"{role}: {response}")
