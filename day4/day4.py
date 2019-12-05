import re

[m, M] = [int(n) for n in re.findall(r"(\d+)(?:-)(\d+)", input("input"))[0]]

f = lambda l, n=0: [str(i) + j for i in range(l, 10) for j in f(i, n + 1) if int(str(i) + j) <= M] if n < 6 else [""]

print("PART 1", sum(1 for n in f(int(str(m)[0])) if m <= int(n) and re.match(r"(.*?)(\d)\2", n)))
print("PART 2", sum(1 for n in f(int(str(m)[0])) if m <= int(n) and
                    (re.match(r"^(.*?)(\A|\d)(?!(\2\d|\d\2))(\d)(\4)(?!\4)", n) or re.match(r"(\d)(\1)(?!\1)", n))))
