import streamlit as st
import tiktoken

# Page Config
st.set_page_config(page_title="AI Budget Buddy", page_icon="💰")

# Title and Description
st.title("💰 AI Task-to-Cost Calculator")
st.write("Estimate how much your AI prompt will cost across different models (March 2026 Rates).")

# Input Box
user_text = st.text_area("Paste your text here:", height=200, placeholder="Type or paste text to analyze...")

if user_text:
    # 1. Calculation Logic
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = len(enc.encode(user_text))
    words = len(user_text.split())

    # 2. Display Metrics
    col1, col2 = st.columns(2)
    col1.metric("Token Count", tokens)
    col2.metric("Word Count", words)

    # 3. Pricing Table (2026 Data)
    models = {
        "GPT-5.4 (Flagship)": {"in": 10.0, "out": 30.0},
        "GPT-5 Mini": {"in": 0.15, "out": 0.60},
        "Claude 4.6 Sonnet": {"in": 3.0, "out": 15.0},
        "Gemini 3 Flash": {"in": 0.10, "out": 0.40},
        "DeepSeek V4": {"in": 0.14, "out": 0.28}
    }

    st.subheader("Estimated Costs (USD)")
    
    # Create a nice table
    results = []
    for name, price in models.items():
        in_cost = (tokens / 1_000_000) * price["in"]
        # Estimate output as 50% of input
        out_cost = ((tokens * 0.5) / 1_000_000) * price["out"]
        total = in_cost + out_cost
        results.append({"Model": name, "Total Est. Cost": f"${total:.5f}", "Price Tier": "High" if total > 0.01 else "Budget"})

    st.table(results)
    
    st.info("💡 Tip: Switching to Gemini 3 Flash could save you significant costs for high-volume tasks.")