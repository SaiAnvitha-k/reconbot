import streamlit as st
import re
import logging
import os

# Set logging level
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
if os.getenv("ENV", "dev") == "prod":
    logging.getLogger().setLevel(logging.WARNING)

# Map Gemini role to Streamlit roles
def map_role(role):
    return "assistant" if role == "model" else role

# Input validation to block prompt injection
def sanitize_input(user_query):
    blocked_patterns = [
        r"<script.*?>", r"</script>", r"(?i)system:", r"(?i)act\s+as", r"(?i)sudo", r"(?i)admin"
    ]
    for pattern in blocked_patterns:
        if re.search(pattern, user_query):
            return "[Input blocked: potentially unsafe content detected.]"
    return user_query

# Append message to chat history
def add_to_history(role, content):
    st.session_state.chat_session.history.append({
        "author": {"role": role},
        "content": {"parts": [content]}
    })

# Fetch response securely
def fetch_gemini_response(user_query):
    clean_query = sanitize_input(user_query)
    if clean_query.startswith("[Input blocked"):
        logging.warning("Blocked unsafe input attempt.")
        return clean_query

    logging.info(f"User Query: {clean_query}")
    try:
        response = st.session_state.chat_session.send_message(clean_query)
        return response
    except Exception as e:
        logging.error("Gemini API call failed", exc_info=True)
        return "⚠️ An error occurred while contacting Gemini. Try again."