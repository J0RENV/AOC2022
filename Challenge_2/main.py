

with open('input.txt') as f: 
    lines=f.readlines()
    #print(lines)
    score = 0
    score2 = 0

    for line in lines:
        splitstring = line.split(" ")
        """
        if splitstring[1].strip() == "X":
            print("yes")
        else:
            print("no") 
        """
# PART 1   
        if splitstring[0] == "A":
            if splitstring[1].strip() == "X":
                score += (3+1) #draw
            elif splitstring[1].strip() == "Y":
                score += (6+2) #win
            else:
                score += (0+3) #loose
        elif splitstring[0] == "B":
            if splitstring[1].strip() == "X":
                score += (0+1) #loose
            elif splitstring[1].strip() == "Y":
                score += (3+2) #draw
            else:
                score += (6+3) #win 
        elif splitstring[0] == "C":
            if splitstring[1].strip() == "X":
                score += (6+1) #win
            elif splitstring[1].strip() == "Y":
                score += (0+2) #loose
            else:
                score += (3+3) #draw 
        else:
            print("NDN")
    # print(score)
# PART 2
        if splitstring[0] == "A":
            if splitstring[1].strip() == "X":
                score2 += (0+3) #loose
            elif splitstring[1].strip() == "Y":
                score2 += (3+1) #draw
            else:
                score2 += (6+2) #win
        elif splitstring[0] == "B":
            if splitstring[1].strip() == "X":
                score2 += (0+1) #loose
            elif splitstring[1].strip() == "Y":
                score2 += (3+2) #draw
            else:
                score2 += (6+3) #win 
        elif splitstring[0] == "C":
            if splitstring[1].strip() == "X":
                score2 += (0+2) #loose
            elif splitstring[1].strip() == "Y":
                score2 += (3+3) #draw
            else:
                score2 += (6+1) #win 
        else:
            print("NDN")
    print(score2)

f.close()