with open('input.txt') as f: 
    lines=f.readlines()
    sol=0
    lc=0
    
# PART ONE   
    for line in lines:    
        line = line.strip()
        
        # Divide in two
        sl1=line[0:len(line)//2]
        sl2=line[(len(line)//2):len(line)]
        a=list(set(sl1)&set(sl2))

        for i in a:
            #print(i)
            if (ord(i) > 96):
                sol += (ord(i)-96)
            else:
                sol += (ord(i)-38)
    print(sol)    
# PART TWO
    sol = 0
    lc = 0
    for line in lines:
        # Group lines per three and on third line, check for common character
        if (lc%3)==0:
            sl1 = line.strip()
        elif (lc%3)==1:
            sl2 = line.strip()
        elif (lc%3)==2:
            a=list(set(sl1)&set(sl2)&set(line.strip()))

            for i in a:
                if (ord(i) > 96):
                    sol += (ord(i)-96)
                else:
                    sol += (ord(i)-38)
        else:
            print("error")
        lc +=  1
    print(sol)

f.close()