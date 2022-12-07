rawinput = open("./inputs/vier.txt").read()

pairs = []
for i in rawinput.split("\n"):
    pairs.append(i.split(","))



sum = 0
for pair in pairs:
    
    range1Start, range1Stop = int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1
    range2Start, range2Stop = int(pair[1].split("-") [0]), int(pair[1].split("-")[1])+1

    range1 = range(range1Start, range1Stop)
    range2 = range(range2Start, range2Stop)
    

    r1Nums = []
    for r1 in range1:
        r1Nums.append(r1)

    r2Nums = []
    for r2 in range2:
        r2Nums.append(r2)


    biggerRange = r1Nums if (range1Start > range2Start and range1Stop > range2Stop) else r2Nums
    smallerRange = r1Nums if (range1Start < range2Start and range1Stop < range2Stop) else r2Nums

    neededMatches = len(biggerRange)
    matches = 0
    for i in biggerRange:
        if i in smallerRange: matches+=1

    
    if matches != 0: sum+=1

  

print(sum)

