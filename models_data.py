# models_data.py

# Prices are in USD per 1 Million tokens
# "in": input cost per 1M tokens
# "out": output cost per 1M tokens

MODELS = {
    "GPT-5.4": {"in": 2.50, "out": 15.00, "strength": "Generalist Powerhouse"},
    "GPT-5.3 Codex": {"in": 2.00, "out": 12.00, "strength": "Specialized Coding"},
    "Claude Opus 4.6": {"in": 5.00, "out": 25.00, "strength": "Complex Reasoning & Depth"},
    "Claude Sonnet 4.6": {"in": 3.00, "out": 15.00, "strength": "Balanced Performance"},
    "Claude Haiku 4.5": {"in": 0.80, "out": 4.00, "strength": "Speed & Efficiency"},
    "Gemini 3.1 Pro": {"in": 2.00, "out": 12.00, "strength": "Long Context & Multimodal"},
    "Gemini 3 Flash": {"in": 0.10, "out": 0.40, "strength": "Ultra-Low Cost"},
    "Gemini 3 Flash-Lite": {"in": 0.07, "out": 0.30, "strength": "Massive Volume Scaling"},
    "Llama 4 Scout": {"in": 0.20, "out": 0.60, "strength": "Edge/Local Efficiency"},
    "Llama 4 Maverick": {"in": 0.30, "out": 0.90, "strength": "General Open-Weight"},
    "Llama 4 Behemoth": {"in": 0.60, "out": 1.80, "strength": "Large-Scale Reasoning"},
    "Grok 4.20": {"in": 2.00, "out": 10.00, "strength": "Real-time Awareness"},
    "DeepSeek V3.2": {"in": 0.27, "out": 0.42, "strength": "Cost-Efficient Reasoning"},
    "DeepSeek R1": {"in": 0.60, "out": 2.30, "strength": "Advanced Reasoning"},
    "Qwen 3.5": {"in": 0.40, "out": 1.50, "strength": "Multilingual Coding"},
    "Qwen 3.5 Max": {"in": 1.00, "out": 5.00, "strength": "High-Performance Reasoning"},
    "Mistral Large 2": {"in": 2.00, "out": 6.00, "strength": "Logic & Structure"},
    "Mixtral": {"in": 0.50, "out": 1.50, "strength": "MoE Efficiency"},
    "Phi-4": {"in": 0.20, "out": 0.60, "strength": "Small Model Efficiency"},
    "Kimi K2.5": {"in": 0.30, "out": 1.00, "strength": "Long Context"},
    "MiniMax M2.5": {"in": 0.40, "out": 1.20, "strength": "Conversational Nuance"},
    "MiMo-V2-Flash": {"in": 0.15, "out": 0.50, "strength": "Coding Speed"},
    "Command R+": {"in": 1.00, "out": 3.00, "strength": "RAG Specialized"},
    "Falcon 3": {"in": 0.50, "out": 1.50, "strength": "Open Foundation"},
    "GLM-5": {"in": 0.80, "out": 2.50, "strength": "Robust Reasoning"},
}