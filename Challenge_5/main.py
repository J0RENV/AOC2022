import copy

with open('input.txt') as f: 
    lines = f.readlines()
    inputStack = []
    stack = []
    moves = []
    lc = 0
    boolstack = True
    sol1 = ''
    sol2 = ''
 
# Convert input to 'stack'
    for line in lines:
        if boolstack:
            if line.strip():
                inputStack.append([])
                for i in range(0, len(line), 4):
                    inputStack[lc].append(line[i+1])
                lc+=1  
            else:
                boolstack=False
                inputStack.pop(-1)
        else:
            instruct=line.split(" ")
            moves.append([int(instruct[1]),int(instruct[3])-1,int(instruct[5].strip())-1])        
    
    stackNo=max(len(elem) for elem in inputStack)
    stackH=len(inputStack) 

# Transform list:
    for i in range (0,stackNo):
        stack.append([])
        for j in range(stackH-1,-1,-1):
            if not(inputStack[j][i]==' '):
                stack[i].append(inputStack[j][i])

# PART ONE
    stack1 = copy.deepcopy(stack)
    for i in range(0,len(moves)):
        if (len(stack1[moves[i][1]])) >= (moves[i][0]):
            for j in range(0,moves[i][0]):
                stack1[moves[i][2]].append(stack1[moves[i][1]].pop())

    for i in range(0,stackNo):
        sol1 += (stack1[i][-1])
    print("Solution to part one is:", sol1)

# PART TWO
    for i in range(0,len(moves)):
        if (len(stack[moves[i][1]])) >= (moves[i][0]):
            stack[moves[i][2]].extend(stack[moves[i][1]][-abs(moves[i][0]):])
            stack[moves[i][1]]=stack[moves[i][1]][:-abs(moves[i][0])]

    for i in range(0,stackNo):
        sol2 += (stack[i][-1])
    print("Solution to part two is:", sol2)

f.close()