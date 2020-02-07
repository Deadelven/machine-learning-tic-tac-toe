#checkvictory
o = "O"
x = "X"

def CheckVictory(grid):
    global x
    global o
    if(grid[0]== x and grid[1] == x and grid[2]== x) :
        Defeat()
    if(grid[3]== x and grid[4]== x and grid[5]== x) :
        Defeat()
    if(grid[6]== x and grid[7]== x and grid[8]== x) :
        Defeat()
    if(grid[0]== x and grid[3]== x and grid[6]== x) :
        Defeat()
    if(grid[1]== x and grid[4]== x and grid[7]== x) :
        Defeat()
    if(grid[2]== x and grid[5]== x and grid[8]== x) :
        Defeat()
    if(grid[0]== x and grid[4]== x and grid[8]== x) :
        Defeat()
    if(grid[2]== x and grid[4]== x and grid[6]== x) :
        Defeat()


    if(grid[0]== o and grid[1]== o and grid[2]== o) :
        Victory()
    if(grid[3]== o and grid[4]== o and grid[5]== o) :
        Victory()
    if(grid[6]== o and grid[7]== o and grid[8]== o) :
        Victory()
    if(grid[0]== o and grid[3]== o and grid[6]== o) :
        Victory()
    if(grid[1]== o and grid[4]== o and grid[7]== o) :
        Victory()
    if(grid[2]== o and grid[5]== o and grid[8]== o) :
        Victory()
    if(grid[0]== o and grid[4]== o and grid[8]== o) :
        Victory()
    if(grid[2]== o and grid[4]== o and grid[6]== o) :
        Victory()

def Victory():
    print("Victory")
    
def Defeat():
    print("Defeat")

