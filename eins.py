
inputs = open("./inputs/eins.txt", "r")

highest=0
ctr = 0
# for i in inputs:
ctr+=1
i = inputs.read()

realInputs = i.splitlines()

elves = []

sum=0
for rp in realInputs:
    if(rp == ""):
        elves.append(sum)
        sum = 0
        continue
    sum = sum + int(rp)
    if sum > highest:
        highest = sum


elves.sort()

result = 0
for elve in elves[-3:]:
    result +=elve

print(result)


#part 1 70116





# test = inputs.read()
# print(test)