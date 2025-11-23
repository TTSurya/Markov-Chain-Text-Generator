import random
from collections import defaultdict, Counter

# ============================
# SETTINGS
# ============================
INPUT_TEXT = "ip.txt"
K = 2
GEN_LEN = 40
SEED = 42

PROB_THRESHOLD = 0.0    # only show probs >= this
SHOW_TRANSITIONS = True
# ============================


class MarkovChain:
    def __init__(self, k=1):
        self.k = k
        self.chain = {}

    def train(self, tokens):
        temp = defaultdict(Counter)
        for i in range(len(tokens) - self.k):
            state = tuple(tokens[i:i + self.k])
            nxt = tokens[i + self.k]
            temp[state][nxt] += 1

        for state, counter in temp.items():
            total = sum(counter.values())
            words = list(counter.keys())
            probs = [counter[w] / total for w in words]

            cumulative = []
            s = 0
            for p in probs:
                s += p
                cumulative.append(s)

            # store cumulative and raw probabilities
            self.chain[state] = (words, cumulative, probs)

    def next_word(self, state, rng):
        if state not in self.chain:
            return None
        words, cum, _ = self.chain[state]
        r = rng.random()
        for i, c in enumerate(cum):
            if r <= c:
                return words[i]


def generate_text(tokens, k, length, seed, chain):
    rng = random.Random(seed)
    state = tuple(tokens[:k])
    out = list(state)

    for _ in range(length):
        nxt = chain.next_word(state, rng)
        if nxt is None:
            break
        out.append(nxt)
        state = tuple(out[-k:])

    text = " ".join(out)
    if not text.endswith("."):
        text += "."
    return text


def print_transition_table(chain, threshold):
    print("\n=== MARKOV CHAIN TABLE (filtered) ===")
    print(f"{'STATE':35} | {'NEXT WORD':15} | PROB")
    print("-" * 65)

    for state, (words, _, probs) in chain.items():
        for w, p in zip(words, probs):
            if p >= threshold:
                state_str = " ".join(state)
                print(f"{state_str:35} | {w:15} | {p:.2f}")

    print("-" * 65)
    print()


# ============================
# MAIN
# ============================
with open(INPUT_TEXT, "r", encoding="utf-8") as f:
    tokens = f.read().split()

mc = MarkovChain(K)
mc.train(tokens)

if SHOW_TRANSITIONS:
    print_transition_table(mc.chain, PROB_THRESHOLD)

print("=== GENERATED TEXT ===")
print(generate_text(tokens, K, GEN_LEN, SEED, mc))
