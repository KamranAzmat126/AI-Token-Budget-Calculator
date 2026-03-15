import tiktoken

def calculate_costs(text):
    enc = tiktoken.get_encoding("cl100k_base")
    token_count = len(enc.encode(text))
    
    # Model pricing (Input/Output per 1M tokens)
    models = {
        "Gemini 3 Flash": {"in": 0.10, "out": 0.40},
        "GPT-5 Mini": {"in": 0.15, "out": 0.60}
    }
    
    results = []
    for name, price in models.items():
        total = ((token_count / 1_000_000) * price["in"]) + \
                (((token_count * 0.5) / 1_000_000) * price["out"])
        results.append({"Model": name, "Cost": f"${total:.5f}"})
    return results