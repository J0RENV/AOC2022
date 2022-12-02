with open('list.txt') as f: 
    lines=f.readlines()
    sum = 0
    totals = []
    empty = 0

    for line in lines:
        if line.strip():
           sum += int(line.strip())
        else: 
            empty += 1
            totals.append(sum)
            print('0')
            sum=0
    
    print(totals)
    print(len(totals))
    print(len(lines))
    print(empty)
    print(max(totals))
    print()
    totals.sort(reverse=True)
    print(totals[0]+totals[1]+totals[2])
f.close()