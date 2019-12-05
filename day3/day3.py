import re
import numpy as np
from pprint import pprint

dirs = {
    "R": np.array((1, 0)),
    "L": np.array((-1, 0)),
    "U": np.array((0, 1)),
    "D": np.array((0, -1))
}

found = [{}, {}]
dist = {}
path = lambda start, step, count, found: ({(start + n * dirs[step[0]]).tostring(): count + n for n in range(int(step[1:])) if (start + n * dirs[step[0]]).tostring() not in found},
                                          {(start + n * dirs[step[0]]).tostring(): np.sum(np.abs(start + n * dirs[step[0]])) for n in range(int(step[1:]))})
for i, wire in enumerate(re.findall(r"[LRUD]\d+", line) for line in open("input.txt", "r").readlines()):
    count = 0
    start = np.array((0, 0))
    for step in wire:
        res = path(start, step, count, found)
        for pos in res[0]:
            found[i][pos] = res[0][pos]
            dist[pos] = res[1][pos]
        start += int(step[1:]) * dirs[step[0]]
        count += int(step[1:])

sol = min((pos for pos in (set(found[0]) & set(found[1]) - {np.array([0, 0]).tostring()})), key=lambda pos: dist[pos])
print("PART 1", dist[sol])
print("PART 2", min(found[0][pos] + found[1][pos] for pos in set(found[0]) & set(found[1]) - {np.array([0, 0]).tostring()}))
