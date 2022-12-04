with open('input.txt') as f: 
    lines=f.readlines()
    sol1 = 0
    sol2 = 0
 
    for line in lines:
        splitstring1,splitstring2 = line.split(",")
        
        #Determine set 1
        s1,s2 = splitstring1.split("-")
        sec1=set(range(int(s1),int(s2)+1))

        #Determine set 2
        s1,s2 = splitstring2.split("-")
        sec2=set(range(int(s1),int(s2)+1))

# PART ONE  
        if sec1.issubset(sec2) or sec2.issubset(sec1):
            sol1 += 1

# PART TWO
        a=(sec1&sec2)
        if len(a):
            sol2 += 1

    print("Solution to part one is:", sol1)
    print("Solution to part two is:", sol2)

f.close()