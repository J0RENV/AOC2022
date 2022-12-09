import time

def read_input():
    with open('input.txt') as f: 
        grid=[]
        lines = f.readlines()
        for line in lines:
            grid.append(list(map(int,line.strip())))
        return grid
    f.close()

def find_visible(grid,grid_rot):
    h = len(grid)
    w = len(grid[0])
    sol=0

    for y in range(1,(h-1)):
        
        for x in range(1,(w-1)):
            if grid[y][x] > max(grid[y][0:x]) or grid[y][x] > max(grid[y][x+1:len(grid[y])]):
                sol+= 1
            else:
                if grid_rot[x][y] > max(grid_rot[x][0:y]) or grid_rot[x][y] > max(grid_rot[x][y+1:len(grid_rot[x])]):
                    sol+= 1
    return sol

def find_scenic_score(grid):
    h = len(grid)
    w = len(grid[0])

    scores=[]
    sol=0
    for y in range(1,(h-1)):
        for x in range(1,(w-1)):
            l=0
            r=0
            u=0
            d=0
            #Look left
            for i in range(x-1,-1,-1):
                if grid[y][i]>=grid[y][x]:
                    l+=1
                    break
                else:
                    l+=1            

            #Look right
            for i in range(x+1,w):
                if grid[y][i]>=grid[y][x]:
                    r+=1
                    break
                else:
                    r+=1            

            #Look up
            for i in range(y-1,-1,-1):
                if grid[i][x]>=grid[y][x]:
                    u+=1
                    break
                else:
                    u+=1            

            #Look right
            for i in range(y+1,h):
                if grid[i][x]>=grid[y][x]:
                    d+=1
                    break
                else:
                    d+=1 

            #Look down
            print("number: %d , x: %d, y: %d, l: %d, r: %d, u: %d, d: %d"%(grid[y][x],x,y,l,r,u,d))

            scores.append(l*r*u*d)
    print(scores)
    return max(scores)

if __name__ == "__main__":
    start_time = time.time()
    grid = read_input()
    grid_rot=list(zip(*grid))

# Part one
    sol1=(len(grid)-1)*2+(len(grid[0])-1)*2 # calculate perimeter trees
    sol1+=find_visible(grid,grid_rot) # count visible trees inside perimeter

# Part two
    sol2 = find_scenic_score(grid)
    
    print("Solution 1: %d trees" % sol1)
    print("Solution 2: %d " % sol2)
    print("Finished in %.5s seconds" % (time.time() - start_time))