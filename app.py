# app.py
import streamlit as st
import pandas as pd
from models_data import MODELS
from utils import extract_text
import time  # Import time for tracking


st.set_page_config(page_title="AI Budget Pro", layout="centered")
st.title("💰 AI Token Budget Estimator")

text_input = st.text_area("Paste your content:", height=150)
uploaded_file = st.file_uploader("Upload any file:")

if st.button("Calculate Estimates", type="primary"):
    content = text_input


    start_time = time.perf_counter() # Start timer
    
    content = text_input
    if uploaded_file:
        with st.spinner("Processing file..."):
            content = extract_text(uploaded_file)
            
    if content:
        # 1. Metrics Calculation
        word_count = len(content.split())
        token_count = int(word_count * 1.3) # Estimating 1 word = 1.3 tokens
        
        # 2. End timer and calculate duration
        end_time = time.perf_counter()
        processing_time = end_time - start_time
        
        # 3. Display Metrics in a clean row
        m1, m2, m3 = st.columns(3)
        m1.metric("Words", f"{word_count:,}")
        m2.metric("Est. Tokens", f"{token_count:,}")
        m3.metric("Process Time", f"{processing_time:.4f}s")
    

    if uploaded_file:
        with st.spinner("Processing file..."):
            content = extract_text(uploaded_file)
            
    if content:
        # Simple token estimation
        token_count = len(content.split()) * 1.3
        results = []
        for name, specs in MODELS.items():
            cost = ((token_count * 0.75 / 1_000_000) * specs["in"]) + \
                   ((token_count * 0.25 / 1_000_000) * specs["out"])
            results.append({"Model": name, "Est. Cost ($)": cost, "Strength": specs["strength"]})
        
        # Display and Sort
        df = pd.DataFrame(results).sort_values(by="Est. Cost ($)")
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        best = df.iloc[0]
        st.success(f"💡 Recommended: **{best['Model']}** is best value at **${best['Est. Cost ($)']:.6f}**.")
    else:
        st.warning("Please provide input text or a file.")