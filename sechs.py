input= open("./inputs/sechs.txt").readline().strip()
 

chars = []
ctr=0
for i in input:
    ctr+=1
    chars.append(i)
    if len(chars)>14:
        chars.pop(0)
    
    if(len(set(chars))==14): 
        print(ctr)
        break
    
    
    
print(ctr)