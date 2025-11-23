import random

# 5-ary alphabet
alphabet = ["a", "b", "c", "d", "e"]

# biased transition matrix (dict-of-dicts)
T = {
    "a": {"a": 0.50, "b": 0.20, "c": 0.10, "d": 0.10, "e": 0.10},
    "b": {"a": 0.10, "b": 0.50, "c": 0.20, "d": 0.10, "e": 0.10},
    "c": {"a": 0.20, "b": 0.10, "c": 0.40, "d": 0.20, "e": 0.10},
    "d": {"a": 0.25, "b": 0.25, "c": 0.10, "d": 0.30, "e": 0.10},
    "e": {"a": 0.10, "b": 0.10, "c": 0.10, "d": 0.20, "e": 0.50},
}

# flatten each row into a sampling table
choices = {s: (list(T[s].keys()), list(T[s].values())) for s in alphabet}

def generate_markov_text(n_words=10000, seed=42):
    random.seed(seed)
    
    # start anywhere
    current = random.choice(alphabet)
    out = [current]

    for _ in range(n_words - 1):
        symbols, probs = choices[current]
        nxt = random.choices(symbols, probs)[0]
        out.append(nxt)
        current = nxt

    # break lines every 50 tokens
    lines = []
    for i in range(0, len(out), 50):
        lines.append(" ".join(out[i:i+50]))
    return "\n".join(lines)

# print the generated text
print(generate_markov_text())
