with open("input.txt", "r") as f:
    prog = [int(n) for n in f.readline().split(",")]

for noun in range(100):
    for verb in range(100):
        program = [prog[0], noun, verb] + prog[3:]
        i = 0
        try:
            while True:
                if program[i] == 99:
                    break

                program[program[i + 3]] = (lambda a, b: a + b, lambda a, b: a * b)[program[i] - 1](
                    program[program[i + 1]], program[program[i + 2]])
                i += 4

            if (noun, verb) == (12, 2):
                print(f"Part 1: {program[0]}")
            if program[0] == 19690720:
                print(f"Part 2: {100 * noun + verb}")
        except IndexError:
            pass