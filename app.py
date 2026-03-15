import streamlit as st
import pandas as pd
from models_data import MODELS

st.set_page_config(page_title="AI Budget Estimator", layout="wide")
st.title("💰 AI Model Budget & Comparison")

text = st.text_area("Paste your content:", height=150)

if st.button("Calculate Estimates"):
    if text:
        # 1. Estimate tokens (rule of thumb: 1 word ≈ 1.3 tokens)
        token_count = len(text.split()) * 1.3
        
        # 2. Calculate Costs
        results = []
        for name, specs in MODELS.items():
            cost = ((token_count * 0.75 / 1_000_000) * specs["in"]) + \
                   ((token_count * 0.25 / 1_000_000) * specs["out"])
            results.append({
                "Model": name,
                "Est. Cost ($)": cost,
                "Strength": specs["strength"]
            })
        
        # 3. Create DataFrame and Sort by Cost
        df = pd.DataFrame(results)
        df = df.sort_values(by="Est. Cost ($)", ascending=True)
        
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # 4. Smart Recommendation Tip
        cheapest = df.iloc[0]
        st.success(f"💡 Budget Tip: For your current input, **{cheapest['Model']}** is the most cost-effective option at ${cheapest['Est. Cost ($)']:.6f}.")
    else:
        st.warning("Please enter text to analyze.")