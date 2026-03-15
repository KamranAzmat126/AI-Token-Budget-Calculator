import streamlit as st
import tiktoken
from io import StringIO

# Page Config
st.set_page_config(page_title="AI Budget Pro", layout="centered")

# Custom CSS for a clean, non-Streamlit look
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-container { background: white; padding: 2rem; border-radius: 10px; border: 1px solid #e0e0e0; }
    </style>
""", unsafe_allow_html=True)

st.title("💰 AI Token Budget Estimator")

# Initialize session state to store data across reruns
if 'results' not in st.session_state:
    st.session_state.results = None
if 'token_count' not in st.session_state:
    st.session_state.token_count = 0

# Central Input Container
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        text_input = st.text_area("Paste your content:", height=150)
    with col2:
        uploaded_file = st.file_uploader("Or upload a file:", type=["txt"])

    if st.button("Calculate Estimates", type="primary"):
        # Logic to handle content
        content = ""
        if uploaded_file is not None:
            content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
        else:
            content = text_input
        
        if content:
            # Calculation
            enc = tiktoken.get_encoding("cl100k_base")
            st.session_state.token_count = len(enc.encode(content))
            word_count = len(content.split())
            
            # Logic: Mock data for models
            st.session_state.results = [
                {"Model": "Gemini 2.5 Pro", "Tokens": st.session_state.token_count, "Words": word_count, "Est. Cost": "$0.05"},
                {"Model": "Claude Sonnet 4.6", "Tokens": st.session_state.token_count, "Words": word_count, "Est. Cost": "$0.12"},
            ]
        else:
            st.warning("Please provide text or upload a file.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Results & Tips
if st.session_state.results:
    st.subheader("Analysis Results")
    st.dataframe(st.session_state.results, use_container_width=True)
    
    st.divider()
    st.subheader("💡 Expert Optimization Tip")
    if st.session_state.token_count > 100000:
        st.info("Large dataset detected: **Gemini 2.5 Pro** offers the most efficient cost-per-token for massive context windows.")
    else:
        st.info("Compact content: **GPT-5 Nano** is recommended for low-latency, budget-friendly processing.")