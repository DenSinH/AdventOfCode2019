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

    def __init__(self):
        self.program = Program([int(n) for n in open("input.txt", "r").readline().split(",")])
        self.index = 0
        self.on = True

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
            self.program[self.index + 1] = int(input("input: "))
            self.index += 2
        elif opcode == 4:
            output = self.program[self.index + 1, params[1]]
            print("OUTPUT", output)
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
            self.on = False

        else:
            raise ValueError("Unknown opcode: " + str(opcode))

        self.index %= len(self.program)


ic = IntCode()
while ic.on:
    ic.step()
