import streamlit as st
from model import LLM
from common.config import Config

# Set page configuration
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot with llama-cpp-python")

# Initialize the model (only once)
@st.cache_resource
def load_model():
    model = LLM(config=Config())
    return model

# Get or initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    role: str = message["role"]
    content: str = message["content"]
    with st.chat_message(role):
        st.write(content)

# Get user input
user_input = st.chat_input("Ask something:")

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            model = load_model()
            response = model.generate(user_input)
            st.write(response)
    
    # Add AI response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})