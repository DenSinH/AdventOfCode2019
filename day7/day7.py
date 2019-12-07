import itertools as it

class Program(object):

    def __init__(self, program):
        self.program = program

    def __getitem__(self, index):
        if index[1] == 0:
            return self.program[self.program[index[0]]]
        elif index[1] == 1:
            return self.program[index[0]]
        else:
            raise ValueError("Invalid mode: " + str(index[1]))

    def __setitem__(self, key, value):
        self.program[self.program[key]] = value

    def __len__(self):
        return len(self.program)


class IntCode(object):

    def __init__(self, inp=None):
        self.program = Program([int(n) for n in open("input.txt", "r").readline().split(",")])
        self.index = 0
        self.status = "running"
        self.out = None
        self.inp = inp

    def step(self):
        opcode = self.program[self.index, 1] % 100
        params = [999] + [int(i) for i in str(self.program[self.index, 1]).zfill(5)[:-2]][::-1]
        if opcode == 1:
            self.program[self.index + 3] = self.program[self.index + 1, params[1]] + self.program[self.index + 2, params[2]]
            self.index += 4
        elif opcode == 2:
            self.program[self.index + 3] = self.program[self.index + 1, params[1]] * self.program[self.index + 2, params[2]]
            self.index += 4
        elif opcode == 3:
            if self.inp is not None:
                self.program[self.index + 1] = self.inp
                self.inp = None
                self.index += 2
            else:
                self.status = "input"
        elif opcode == 4:
            output = self.program[self.index + 1, params[1]]
            self.out = int(output)
            self.index += 2
        elif opcode == 5:
            if self.program[self.index + 1, params[1]] != 0:
                self.index = int(self.program[self.index + 2, params[2]])
            else:
                self.index += 3
        elif opcode == 6:
            if self.program[self.index + 1, params[1]] == 0:
                self.index = int(self.program[self.index + 2, params[2]])
            else:
                self.index += 3
        elif opcode == 7:
            if self.program[self.index + 1, params[1]] < self.program[self.index + 2, params[2]]:
                self.program[self.index + 3] = 1
            else:
                self.program[self.index + 3] = 0
            self.index += 4
        elif opcode == 8:
            if self.program[self.index + 1, params[1]] == self.program[self.index + 2, params[2]]:
                self.program[self.index + 3] = 1
            else:
                self.program[self.index + 3] = 0
            self.index += 4

        elif opcode == 99:
            self.status = "stopped"

        else:
            raise ValueError("Unknown opcode: " + str(opcode))

        self.index %= len(self.program)

    def input(self, inp):
        self.inp = inp
        self.status = "running"

    def run(self, *args):
        _i = 0
        while self.status != "stopped" and (_i < len(args) or self.inp is not None):
            if self.status == "input":
                self.input(args[_i])
                _i += 1

            while self.status == "running":
                self.step()

        return self.out


if __name__ == "__main__":
    m = 0
    for sequence in it.permutations(range(5)):
        out = 0
        for i in sequence:
            out = IntCode().run(i, out)
            i += 1
        m = max(m, out)

    print(m)

    m = 0
    for sequence in it.permutations(range(5, 10)):
        ics = {l: IntCode() for l in "ABCDE"}
        out = 0
        for i, a in enumerate("ABCDE"):
            out = ics[a].run(sequence[i], out)

        while not all(ics[a].status == "stopped" for a in ics):
            for a in "ABCDE":
                out = ics[a].run(out)

        m = max(m, ics["E"].out)

    print(m)
