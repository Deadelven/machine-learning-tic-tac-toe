#checkvictory
o = "O"
e = "-"
x = "X"
victor = "none"
def CheckVictory(grid):
    global victor
    victor = "none"
    global x
    global o
    if(grid[0]== x and grid[1] == x and grid[2]== x) :
        Defeat()
        return False
    if(grid[3]== x and grid[4]== x and grid[5]== x) :
        Defeat()
        return False
    if(grid[6]== x and grid[7]== x and grid[8]== x) :
        Defeat()
        return False
    if(grid[0]== x and grid[3]== x and grid[6]== x) :
        Defeat()
        return False
    if(grid[1]== x and grid[4]== x and grid[7]== x) :
        Defeat()
        return False
    if(grid[2]== x and grid[5]== x and grid[8]== x) :
        Defeat()
        return False
    if(grid[0]== x and grid[4]== x and grid[8]== x) :
        Defeat()
        return False
    if(grid[2]== x and grid[4]== x and grid[6]== x) :
        Defeat()
        return False


    if(grid[0]== o and grid[1]== o and grid[2]== o) :
        Victory()
        return False
    if(grid[3]== o and grid[4]== o and grid[5]== o) :
        Victory()
        return False
    if(grid[6]== o and grid[7]== o and grid[8]== o) :
        Victory()
        return False
    if(grid[0]== o and grid[3]== o and grid[6]== o) :
        Victory()
        return False
    if(grid[1]== o and grid[4]== o and grid[7]== o) :
        Victory()
        return False
    if(grid[2]== o and grid[5]== o and grid[8]== o) :
        Victory()
        return False
    if(grid[0]== o and grid[4]== o and grid[8]== o) :
        Victory()
        return False
    if(grid[2]== o and grid[4]== o and grid[6]== o) :
        Victory()
        return False


    return True


def Victory():
    print("o wins")
    global victor
    victor = "O"
    
def Defeat():
    print("x wins")
    global victor
    victor = "X"

def CheckVictor():
    global victor
    if victor == "X":
        return True
    else:
        return False


def CheckMove(grid , move):
	global e
	global x
	global o
	if grid[move] == e:
		return True
	else:
		return False
	
	
