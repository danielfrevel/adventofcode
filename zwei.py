rawinput = open("./inputs/zwei.txt").read()

input = []
for i in rawinput.split("\n"):
    input.append(i.split(" "))

rules = {
    "A":"B" ,
    "B":"C" ,
    "C":"A" 
}

losingRules = {
    "A":"C",
    "B":"A",
    "C":"B" 
}

sum = 0
for i in input:
    enemy = i[0]
    requiredOut = i[1]
    winning_move = rules[enemy]
    losing_move = losingRules[enemy]

    if requiredOut == "X": me = losing_move #l
    if requiredOut == "Y": me = enemy #d
    if requiredOut == "Z": me = winning_move #w

    if me == winning_move:
        sum+=6
    if enemy == me: 
        sum+=3

    if me == "A": sum+= 1
    if me == "B": sum+= 2
    if me == "C": sum+= 3

print(sum)
    
    