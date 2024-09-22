import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
# from dotenv  import load_dotenv
# load_dotenv()
import os


st.set_page_config(page_title= "Conversational Q&A Chatbot...")
st.header("Hy, lets chat...")

chat = ChatOpenAI(temperature= 0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [SystemMessage(content= "AI Assistant...")]

def get_response(que):
    st.session_state['flowmessages'].append(HumanMessage(content= que))
    ans = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=ans.content))
    return ans.content

input = st.text_input("Input : ", key= 'input')
response = get_response(input)

submit = st.button("Go")

if submit:
    st.subheader("The response  is... ")
    st.write(response)