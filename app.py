import streamlit as st
from io import StringIO
import logic # Import your logic file

st.set_page_config(page_title="AI Budget Buddy", layout="wide")

# Sidebar for file upload
with st.sidebar:
    st.header("Input Options")
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    
text_input = st.text_area("Or paste your text here:")

# Trigger button
if st.button("Start Processing"):
    content = ""
    if uploaded_file is not None:
        content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    elif text_input:
        content = text_input
    
    if content:
        with st.spinner("Calculating..."):
            costs = logic.calculate_costs(content)
            st.table(costs)
    else:
        st.warning("Please provide text or upload a file.")