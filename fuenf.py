#             [G] [W]         [Q]    
# [Z]         [Q] [M]     [J] [F]    
# [V]         [V] [S] [F] [N] [R]    
# [T]         [F] [C] [H] [F] [W] [P]
# [B] [L]     [L] [J] [C] [V] [D] [V]
# [J] [V] [F] [N] [T] [T] [C] [Z] [W]
# [G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
# [R] [J] [S] [Z] [R] [S] [D] [L] [J]
#  1   2   3   4   5   6   7   8   9 

from dataclasses import dataclass


rawinput = open("./inputs/fuenf.txt").read()

stacks=[[],
["R","G","J","B","T","V","Z"],
["J","R","V","L"],
["S","Q","F"],
["Z","H","N","L","F","V","Q","G"],
["R","Q","T","J","C","S","M","W"],
["S","W","T","C","H","F"],
["D","Z","C","V","F","N","J"],
["L","G","Z","D","W","R","F","Q"],
["J","B","W","V","P"]]

@dataclass
class Instruction:
    count: int
    start: int 
    end: int    


def rearrange(instruction:Instruction):

    # task1
    # for i in range(instruction.count): 
    #     stacks[instruction.end].append(stacks[instruction.start].pop())

    items = []
    for i in range(instruction.count):
        items.append(stacks[instruction.start].pop())

    items.reverse()
    for i in range(instruction.count):
        stacks[instruction.end].append(items[i])


input = []
for i in rawinput.split("\n"):
    input.append(i.split("\n"))


instructions = []
for rowRaw in input: 
    row:str = rowRaw[0]
    row = row.replace("move","").replace("from","").replace("to","")
    values = row.split("  ")

    instructions.append(Instruction(int(values[0]), int(values[1]), int(values[2])))


for i in instructions:
    rearrange(i)


for stack in stacks:
    if(len(stack) == 0):continue
    print(stack.pop())