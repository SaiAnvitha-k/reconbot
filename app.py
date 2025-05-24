import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gpt
from chat_security_utils import *
import time

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="🛡️ ReconBot: Cybersecurity Chat",
    page_icon="🛡️",
    layout="wide"
)

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("🚫 GOOGLE_API_KEY not found. Check your .env file.")
    st.stop()

gpt.configure(api_key=API_KEY)
model = gpt.GenerativeModel("models/gemini-1.5-flash")

st.markdown(
    "<h1 style='color:#0f0f0f;background-color:#d9ffcc;padding:10px;border-radius:10px;'>"
    "🛡️ ReconBot | Cybersecurity Assistant</h1>",
    unsafe_allow_html=True
)

# Rate limiter
if "last_query_time" not in st.session_state:
    st.session_state.last_query_time = 0

# Get input
user_input = st.chat_input("Type your cybersecurity question...")
if user_input:
    if time.time() - st.session_state.last_query_time < 2:
        st.warning("⏳ You're sending messages too quickly.")
        st.stop()
    st.session_state.last_query_time = time.time()

    st.chat_message("user", avatar="🧑‍💼").markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("ReconBot is analyzing..."):
            dots_placeholder = st.empty()
            for i in range(3):
                dots_placeholder.markdown(f"⏳ Thinking{'.' * (i + 1)}")
                time.sleep(0.4)
            dots_placeholder.empty()

            sanitized_query = sanitize_input(user_input)
            if sanitized_query.startswith("[Input blocked"):
                st.markdown(sanitized_query)
            else:
                try:
                    gemini_response = model.generate_content(sanitized_query)
                    st.markdown(gemini_response.text)
                except Exception as e:
                    st.markdown(f"⚠️ Error: {e}")
