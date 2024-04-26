# Adapted from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps#build-a-simple-chatbot-gui-with-streaming

import streamlit as st
import random
import time

import client


MODEL = "llama3"

def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None

col1, col2 = st.columns([6,1])

with col1:
    st.header(f"Chat with LLama 3 8B")

with col2:
    st.button('Reset ↺', on_click=reset_chat)


# Initialize chat history
if "messages" not in st.session_state:
    reset_chat()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        context = st.session_state.context

        # Simulate stream of response with milliseconds delay
        for chunk, ctx in client.generate(MODEL, prompt, context=context):
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)
        st.session_state.context = ctx

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
