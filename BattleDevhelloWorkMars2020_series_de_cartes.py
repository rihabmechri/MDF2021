lines = ["10", "5", "3", "3", "4", "9", "9", "9", "9", "9", "6"]
N = lines[0]
history = lines[1:]
L = [1]
h = history[0]
j = 0
for i in range(1, len(history)):
    if h == history[i]:
        L[j] += 1
    else:
        L.append(1)
        h = history[i]
        j += 1
print(max(L))
