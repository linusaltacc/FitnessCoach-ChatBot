import streamlit as st
from streamlit_chat import message
import requests
from chatgpt_fitness import *
from gpt3_fitness import *
from VertexAI import vertexAI

st.header("Fitness Coach Chatbot")
st.markdown("[Github](https://github.com/linusaltacc/FitnessCoach-ChatBot-using-ChatGPT)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hey", key="input")
    return input_text 

form = st.form("my_form",clear_on_submit=False)
p = form.selectbox('Select a Prompt', ("VertexAI (chat-bison@001)","GPT3 (text davinci 003)", "ChatGPT (GPT 3.5 turbo)"))
submit = form.form_submit_button("Submit")
prompt = vertexAI #default prompt
if submit:
    if p == "GPT3":
        prompt = gpt3
    elif p == "ChatGPT":
        prompt = chatgpt
    elif p == "Palm":
        prompt = vertexAI

user_input = get_text()
if user_input:
    st.session_state.past.append(user_input)
    st.session_state.generated.append(prompt(user_input))

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))