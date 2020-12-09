# because i have a stinking suspicion that this bytecode is going to come back eventually
# and also because bytecode interpreters are fun

LOOPED = "LOOPED"
FINISHED = "FINISHED"

class VM:
    def __init__(self):
        self.ip = 0
        self.acc = 0
        self.visited = []
        
    def run(self, instrs):
        while True:
            if self.ip in self.visited:
                return (LOOPED, self.visited, self.acc)
            elif self.ip == len(instrs):
                return (FINISHED, self.visited, self.acc)
            else:
                self.visited.append(self.ip)

            (op, val) = instrs[self.ip]
            if op == "jmp":
                self.ip += val
            elif op == "acc":
                self.acc += val
                self.ip += 1
            elif op == "nop":
                self.ip += 1
            else:
                raise Exception(f"Invalid instr {[op, val]}")

def parse(line):
    op = line.split(" ")[0]
    val = line.split(" ")[1]
    sign = val[0]
    val = int(val[1:])
    if sign == "-":
        val = -1 * val 
    
    return (op, val)

def interpret(text):
    vm = VM()
    (result, visited, acc) = vm.run([parse(line) for line in text.split("\n")])
    if result == LOOPED:
        print(f"> Looped: acc = {acc}")
    else:
        print(f"> Execution finished: acc = {acc}")
    
    return (result, visited, acc)

# from input import x

# def part1():
#     (_, _, acc) = interpret(x)
#     print(acc)

# def part2():
#     instrs = x.split("\n")
#     (_, visited, _) = interpret(x)

#     for ip in visited:
#         instr = instrs[ip]
#         op = instr.split(" ")[0]
#         val = instr.split(" ")[1]
#         sign = val[0]
#         val = int(val[1:])

#         new_instrs = instrs.copy()
#         if op == "jmp":
#             new_instrs[ip] = "nop +0"
#         elif op == "nop":
#             new_instrs[ip] = "jmp " + sign + str(val)
#         else:
#             continue
#         print(f"switched {instrs[ip]} to {new_instrs[ip]}")
#         (result, _, acc) = interpret("\n".join(new_instrs))
#         if result == FINISHED:
#             print(acc)
#             return

# part1()
# part2()