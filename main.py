import streamlit as st
import random
from utils.validator import validate_code
from utils.feedback import get_feedback
import os

# Load buggy snippets

def load_snippets():
    base_path = os.path.dirname(__file__)  # Gets the directory of main.py
    snippets_path = os.path.join(base_path, "snippets")
    snippets = {}
    for file in os.listdir(snippets_path):
        if file.endswith(".py"):
            with open(os.path.join(snippets_path, file), "r") as f:
                snippets[file] = f.read()
    return snippets

# Load mentor quotes
def load_quotes():
    import json
    with open("mentor_mode/quotes.json", "r") as f:
        return json.load(f)

# App UI
st.set_page_config(page_title="Code Debugging Tutor", layout="centered")
st.title("🐞 Code Debugging Tutor")
st.subheader("Fix the bug and become a debugging ninja!")

snippets = load_snippets()
quotes = load_quotes()
selected_file = st.selectbox("Choose a buggy snippet:", list(snippets.keys()))
st.code(snippets[selected_file], language="python")

user_fix = st.text_area("🔧 Your Fix (Edit the code here):", height=200)

if st.button("🧪 Run & Validate"):
    st.write("🔍 Button clicked!")  # Debug print
    result, error = validate_code(user_fix)
    if result:
        st.success("✅ Great job! The code runs correctly.")
        st.balloons()
        st.markdown(f"**Mentor says:** _{random.choice(quotes)}_")
    else:
        st.error("❌ Still buggy. Here's what went wrong:")
        st.code(error)
        st.markdown(get_feedback(error))
        