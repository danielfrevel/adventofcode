inputs = open("./inputs/drei.txt").read()

def find_prio(char):
    asciival= ord(char)


    if(char.isupper()): return asciival - 64 + 26
    
    return asciival - 96

ctr= 0
batches = []
batch = []
for i in inputs.split("\n"):
    ctr+=1
    batch.append(i) 
    if(ctr>2):
        ctr=0
        batches.append(batch)
        batch = []


sum = 0
for batch in batches:
    first = set(batch[0])
    second = set(batch[1])
    third = set(batch[2])

    commontypes = first & second & third
    for ct in commontypes:
        sum+=find_prio(ct)

print(sum)

print(batches[0])


    
#     commontypes = first&second&third   




    
    
