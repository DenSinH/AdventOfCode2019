from pprint import pprint


class Program(object):

    def __init__(self, program):
        self.program = {i: program[i] for i in range(len(program))}
        self.rel = 0

    def __getitem__(self, index):
        if index[1] == 0:
            return self.program.get(self.program.get(index[0], 0), 0)
        elif index[1] == 1:
            return self.program.get(index[0], 0)
        elif index[1] == 2:
            return self.program.get(self.rel + self.program.get(index[0], 0), 0)
        else:
            raise ValueError("Invalid mode for get: " + str(index[1]))

    def __setitem__(self, key, value):
        if key[1] == 0:
            self.program[self.program.get(key[0], 0)] = value
        elif key[1] == 2:
            self.program[self.rel + self.program.get(key[0], 0)] = value
        else:
            raise ValueError("Invalid mode for set: " + str(key[1]))

    def __len__(self):
        return len(self.program)

    def __repr__(self):
        return str(self.program)


class IntCode(object):

    def __init__(self, inp=None):
        self.program = Program([int(n) for n in open("input.txt", "r").readline().split(",")])
        self.index = 0
        self.status = "running"
        self.out = None
        self.inp = inp

    def step(self, debug=False):
        opcode = self.program[self.index, 1] % 100
        params = [999] + [int(i) for i in str(self.program[self.index, 1]).zfill(5)[:-2]][::-1]

        if debug:
            print(opcode, params[1:])

        if opcode == 1:
            self.program[self.index + 3, params[3]] = self.program[self.index + 1, params[1]] + self.program[self.index + 2, params[2]]
            self.index += 4
        elif opcode == 2:
            self.program[self.index + 3, params[3]] = self.program[self.index + 1, params[1]] * self.program[self.index + 2, params[2]]
            self.index += 4
        elif opcode == 3:
            if self.inp is not None:
                self.program[self.index + 1, params[1]] = self.inp
                self.inp = None
                self.index += 2
            else:
                self.status = "input"
        elif opcode == 4:
            output = self.program[self.index + 1, params[1]]
            print(output)
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
                self.program[self.index + 3, params[3]] = 1
            else:
                self.program[self.index + 3, params[3]] = 0
            self.index += 4
        elif opcode == 8:
            if self.program[self.index + 1, params[1]] == self.program[self.index + 2, params[2]]:
                self.program[self.index + 3, params[3]] = 1
            else:
                self.program[self.index + 3, params[3]] = 0
            self.index += 4
        elif opcode == 9:
            self.program.rel += self.program[self.index + 1, params[1]]
            self.index += 2

        elif opcode == 99:
            self.status = "stopped"

        else:
            raise ValueError("Unknown opcode: " + str(opcode))

    def input(self, inp):
        self.inp = inp
        self.status = "running"

    def run(self, *args, debug=False):
        _i = 0
        while self.status != "stopped" and (_i < len(args) or self.inp is not None or len(args) == 0):
            if self.status == "input":
                self.input(args[_i])
                _i += 1

            while self.status == "running":
                self.step(debug)
                if debug:
                    print(self.index, self.program.rel)
                    input()

        return self.out


if __name__ == "__main__":
    for i in (1, 2):
        ic = IntCode(i)
        ic.run()
