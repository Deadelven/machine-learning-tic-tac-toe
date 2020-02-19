import random
import keras
import pickle
import glob
import h5py
from createmodel import createModel
from gridcontrol import CheckVictory
from gridcontrol import CheckVictor

#run train vs random untill x wins. then h5py save weights of random.
#randomise weights

print("Lets Play Tic Tac Toe")

e = "-"
x = "X"
o = "O"
grid = [e,e,e,e,e,e,e,e,e]
turncount = 0
invalidturnx = 0

def Disp():
    print("------")
    print(grid[0]+" "+grid[1]+" "+grid[2])
    print(grid[3]+" "+grid[4]+" "+grid[5])
    print(grid[6]+" "+grid[7]+" "+grid[8])
    print("------")    

def Playrand():
    print("Play")
    global grid
    global o
    global e
    move = 0
    while move == 0:    
        xcon = random.randrange(0,9)
        if(grid[xcon] == e):
            grid[xcon] = o
            move = 1
            break


def turnx(pos):
    global grid
    global x
    global e
    print("turnx ")
    if grid[pos] == e:
        grid[pos] = x
        return 1
    else:
        return 0
def endGame(winloss):
    if winloss == True:
        #save model
        print("WinTrue")
    if winloss == False:
        print("WinFalse")
        #Generate new model
        #Start new game
        global grid
        grid = [e,e,e,e,e,e,e,e,e]
        global turncount
        turbcount = 0
        global invalidturnx
        invalidturnx = 0
        #aivsrandom()
 
def aivsrandom():
    global grid
    global e
    global x
    global o
    global turncount
    global invalidturnx

    
    while CheckVictory(grid):
        CheckVictory(grid)
        invalidturnx = 0
        
        print("turncount")
        px = createModel()
        gridx =[]
        print("gridx")
        for val in  grid:
            if val == e:
                gridx.append(0)
            elif val== x:
                gridx.append(1)
            elif val == o:
                gridx.append(-1)
        
        print("turncount")
        if( turncount % 2 )!=0:
            invalidturnx = 0
            placeFail = True
            #print("putwhileloophere")
            while(placeFail):
                while(invalidturnx<9):
                    #print("inside the loop")
                    pxgrid= []
                    pxgrid.append([gridx[0],gridx[1],gridx[2],gridx[3],gridx[4],gridx[5],gridx[6],gridx[7],gridx[8],turncount,invalidturnx])
                    #print("predictmove")
                    #predict move. take move
                    xxp = px.predict(pxgrid)
                    #print("1")
                    print(xxp)
                    xxpmax = max(xxp[0])
                    print ("Xpmax == %s"% (xxpmax))
                    #print("2")
                    valcount = 0
                    for val in xxp[0]:
                        #invalidturn
                        if val == xxpmax:
                            if grid[valcount] != e:
                                grid[valcount] = x
                                Disp()
                                turncount += 1
                                invalidturnx = 10
                                PlaceFail = False
                                print("PlaceSuccess")
                            else:
                                print("invalidTurn %s" % (invalidturnx))
                                invalidturnx += 1
                                valcount += 1
                
            
        else:
            turncount +=1
            Playrand()
            
            print("break")
            Disp()
        
        
    
    
    
    
    
    print("runsuccess")
    endGame(CheckVictory(grid))
    

aivsrandom()
