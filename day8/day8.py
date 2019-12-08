inp = open("input.txt", "r").read().strip()
layers = [inp[i:i+150] for i in range(0, len(inp), 150)]
print("PART 1", (lambda l: l.count("1") * l.count("2"))(min(layers, key=lambda l: l.count("0"))))

for i in range(0, 150, 25):
    l = ""
    for j in range(25):
        l += " X"[int([layer[i + j] for layer in layers if layer[i + j] != "2"][0])]
    print(l)
