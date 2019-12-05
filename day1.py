print(sum(int(int(n) / 3) - 2 for n in open("input.txt", "r").readlines()))
f = lambda n: int(n / 3) - 2 + (f(int(n / 3) - 2) if n > 32 else 0)
print(sum(f(int(n)) for n in open("input.txt", "r").readlines()))
