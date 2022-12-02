with open('list.txt') as f: 
    lines=f.readlines()
    sum = 0
    totals = []
    empty = 0
# Part One
    for line in lines:
        if line.strip():
           sum += int(line.strip())
        else: 
            empty += 1
            totals.append(sum)
            print('0')
            sum=0
    
    print(max(totals))
# Part Two
    totals.sort(reverse=True)
    print(totals[0]+totals[1]+totals[2])
    
f.close()