import sys

lines = [6, "bleu", "jaune", "rouge", "rouge", "jaune", "rouge"]
N = lines[0]
colors = lines[1:]
result = dict((c, colors.count(c)) for c in colors)
sorted = list(dict(
    sorted(
        result.items(), key=lambda x: x[1], reverse=True)).keys())
print(" ".join(sorted[0:2]))

