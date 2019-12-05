import re
import numpy as np

dirs = {
    "R": np.array((1, 0)),
    "L": np.array((-1, 0)),
    "U": np.array((0, 1)),
    "D": np.array((0, -1))
}

found = [{}, {}]
path = lambda start, step, count, found: {str(start + n * dirs[step[0]]): count + n for n in range(int(step[1:])) if str(start + n * dirs[step[0]]) not in found}
for i, wire in enumerate(re.findall(r"[LRUD]\d+", line) for line in open("input.txt", "r").readlines()):
    count = 0
    start = np.array((0, 0))
    for step in wire:
        found[i].update(path(start, step, count, found))
        start += int(step[1:]) * dirs[step[0]]
        count += int(step[1:])

dist = lambda point: np.sum(np.abs(np.fromstring(point[1:-1], sep=" ")))
sol = min((set(found[0]) & set(found[1])) - {"[0 0]"}, key=dist)
print(sol, dist(sol))
print(min(found[0][pos] + found[1][pos] for pos in set(found[0]) & set(found[1]) - {"[0 0]"}))
