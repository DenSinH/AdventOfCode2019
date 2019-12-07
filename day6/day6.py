import re

orbits = [re.search(r"(.*)\)(.*)", line).groups() for line in open("input.txt").readlines()]
conn = {orbit[0]: [o[1] for o in orbits if o[0] == orbit[0]] for orbit in orbits}

l = lambda o: len(conn.get(o, [])) + sum((l(_o) for _o in conn.get(o, [])))
print("PART 1", sum((l(o) for o in conn)))

s = lambda o: set(conn.get(o, [])).union(*[s(_o) for _o in conn.get(o, [])])
d = lambda o, f: 1 if f in conn.get(o, []) else 1 + sum((d(_o, f) for _o in conn.get(o, []) if search(_o, (f,))))


def search(start="COM", find=("YOU", "SAN")):
    if len(set(find) & s(start)) == len(find):
        if not any(search(orbit) for orbit in conn.get(start, [])):
            if len(find) == 2:
                print(d(start, "YOU") + d(start, "SAN") - 2)
        return True
    else:
        return False


print("PART 2",)
search()
