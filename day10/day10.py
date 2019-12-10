from math import gcd, atan2, pi


def see(pos, asteroids):
    if asteroids[pos[1]][pos[0]] != "#":
        return 0
    for dy in range(-pos[1], len(asteroids) - pos[1]):
        for dx in range(-pos[0], len(asteroids[0]) - pos[0]):
            if gcd(dx, dy) != 1:
                continue
            yield int(any(asteroids[pos[1] + d*dy][pos[0] + d*dx] == "#" for d in range(1, len(asteroids)) if 0 <= pos[1] + d*dy < len(asteroids) and 0 <= pos[0] + d*dx < len(asteroids[0])))


pos, p1 = (lambda asteroids: max([((x, y), sum(see((x, y), asteroids))) for y in range(len(asteroids)) for x in range(len(asteroids[0]))],
                                 key=lambda o: o[1]))(open("input.txt", "r").readlines())
print("PART 1", p1)


def vaporize(pos, asteroids):
    c = 0
    directions = [(dx, dy) for dx in range(-len(asteroids[0]), len(asteroids[0])) for dy in range(-len(asteroids), len(asteroids))
                  if gcd(dx, dy) == 1 and not dx == dy == 0]
    while True:
        for (dx, dy) in sorted(directions, key=lambda _d: atan2(*_d) % (2 * pi)):
            for d in range(1, len(asteroids)):
                px, py = pos[0] + d*dx, pos[1] - d*dy
                try:
                    if 0 <= px < len(asteroids[0]) and 0 <= py < len(asteroids):
                        if asteroids[py][px] == "#":
                            asteroids[py][px] = "."
                            c += 1
                            if c == 200:
                                return px, py
                            break
                except IndexError:
                    break


print("PART 2", (lambda x, y: 100*x + y)(*vaporize(pos, [list(l) for l in open("input.txt", "r").readlines()])))
