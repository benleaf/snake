#run the actual file for the game to work, the shell wont work

import random, msvcrt, time #just the regular defult python inports

snakeX = [0,1,2]
snakeY = [0,0,0]
foodX = 2
foodY = 0
score = 0
boardX = 30#defines the dimentions of the play area
boardY = 14#
snakeMoveY = 0
snakeMoveX = 1
finished = False
direction = [1,0]

def drawScore(score):
    print("score:",score)
    
def drawGrid(snakeX,snakeY,foodX,foodY,boardY,boardX):#sistomaticly prints out a grid of "-" when procedure finds the
    for y in range (boardY):                          #co-ordenets of a segment of the snake it will print "H" and
        for x in range (boardX):                      #when x and y are = to that of the food it will print "$"
            snakeSpot = False
            for i in range(len(snakeX)):
                if y == snakeY[i] and x == snakeX[i]:
                    print("H",end='')
                    snakeSpot = True
                    break
            if y == foodY and x == foodX:
                print("$",end='')
            elif snakeSpot == False:
                print("-",end='')
        print("")

   
def getFoodLoc(foodX,foodY,snakeX,snakeY,boardY,boardX): #makes sure that the food is not being placed on the snake
    foodXY = []                                          #when sutable position  is found the function will retern the 
    clear = False                                        #co-ordenets that the food will be placed on
    while clear == False:
        for i in range(len(snakeX)):
            if foodY == snakeY[i] and foodX == snakeX[i]:
                clear = False
                break
            else:
                clear = True
        if clear == False:
            foodX = random.randrange(0,boardX)
            foodY = random.randrange(0,boardY)
    foodXY.append(foodX)
    foodXY.append(foodY)
    return foodXY
            
def placeFoodX(foodXY): #placeFoodX and Y unpack the list foodXY so that the values can be uesed
    foodX = foodXY[0]
    return foodX

def placeFoodY(foodXY):
    foodY = foodXY[1]
    return foodY

def snakeMotion(snakeX,snakeY,snakeMoveY,snakeMoveX,score):#removes the back of the snake and adds to the frount
    snakeX.pop(0)                                          #when the snake eats a "$" an additional values is added
    snakeY.pop(0)                                          #to the frount of the snake
    snakeX.append((snakeX[(len(snakeX))-1])+ snakeMoveX)
    snakeY.append((snakeY[(len(snakeY))-1])+ snakeMoveY)
    if foodY == snakeY[(len(snakeY))-1] and foodX == snakeX[(len(snakeX))-1]:
        score = score + 1
        snakeX.insert((len(snakeY))-1,snakeX[(len(snakeX))-1])
        snakeY.insert((len(snakeY))-1,snakeY[(len(snakeY))-1])
    return score
def clear(boardY):
    print("\n" * (boardY + 2))

def keybordInput(snakeMoveY,snakeMoveX):#uses msvcrt to regiter a keybord input and uses it to change the direction
    direction.pop(1)                    #of the snake
    direction.pop(0)
    if msvcrt.kbhit():
         char = msvcrt.getch()
         if char == b'w' and snakeMoveY != 1:
             snakeMoveX = 0
             snakeMoveY = -1
         if char == b's'and snakeMoveY != -1:
             snakeMoveX = 0
             snakeMoveY = 1
         if char == b'a' and snakeMoveX != 1:
             snakeMoveX = -1
             snakeMoveY = 0
         if char == b'd' and snakeMoveX != -1:
             snakeMoveX = 1
             snakeMoveY = 0
    direction.append(snakeMoveX)
    direction.append(snakeMoveY)
    return direction
        
def directionX(direction):#unpakes the list direction to return snakeMoveX
    snakeMoveX = direction[0]
    return snakeMoveX
    
def directionY(direction):#unpakes the list direction to return snakeMoveY
    snakeMoveY = direction[1]
    return snakeMoveY

def isGameOver(boardX,boardY,snakeX,snakeY,finished):#registers to see if the head of the snake is on the edge or inside the body of the snake
    if (snakeX[len(snakeX)-1] < 0) or (snakeY[len(snakeY)-1] < 0) or (snakeX[len(snakeX)-1] > boardX-1) or (snakeY[len(snakeY)-1] > boardY-1):
        finished = True     
    for i in range((len(snakeY))-3):
        if snakeY[i] == snakeY[len(snakeY)-1] and snakeX[i] == snakeX[len(snakeX)-1]:
            finished = True
    return finished




clear(boardY)#sets up the screan so that the user will understand what is going on and can controle the start of the game
drawGrid(snakeX,snakeY,foodX,foodY,boardY,boardX) 
input("press any key to start") 
while finished == False:
    clear(boardY)
    direction = keybordInput(snakeMoveY,snakeMoveX)
    snakeMoveX = directionX(direction)
    snakeMoveY = directionY(direction)
    score = snakeMotion(snakeX,snakeY,snakeMoveY,snakeMoveX,score)
    drawScore(score)
    foodXY = getFoodLoc(foodX,foodY,snakeX,snakeY,boardY,boardX)
    foodY = placeFoodY(foodXY)
    foodX = placeFoodX(foodXY)
    drawGrid(snakeX,snakeY,foodX,foodY,boardY,boardX)#prints out the grid
    finished = isGameOver(boardX,boardY,snakeX,snakeY,finished)
    time.sleep(0.1)##########################################################controles the refresh rate / dificaltly
print("game over")#you can only louse snake :(
time.sleep(5)#lets the user see their mistake for 5 seconds

