####################################SNAKE#####################################

from Tkinter import *

from random import *

def mousePressedSnake(canvas, event):
    redrawAllSnake(canvas)

def keyPressedSnake(canvas, event):
    canvas.data.ignoreNextTimerEvent = True
    if event.keysym == "Left":
        moveSnake(canvas, 0, -1)
    elif event.keysym == "Down":
        moveSnake(canvas, 1, 0)
    elif event.keysym == "Right":
        moveSnake(canvas, 0, 1)
    elif event.keysym == "Up":
        moveSnake(canvas, -1, 0)
    elif event.keysym == "q":
        gameOver(canvas) #is it this simple, really?
    elif event.keysym == "r":
        initSnake(canvas)
    elif event.keysym == "plus" or event.keysym == "equal":
        if canvas.data.speed > 25:
            canvas.data.speed -= 25
            canvas.data.scoreIncrement +=2
            # I made the timer keep going while these weird things happen b/c it was weird otherwise
            canvas.data.ignoreNextTimerEvent = False
    elif event.keysym == "-":
        canvas.data.speed +=25
        canvas.data.scoreIncrement -=2
        canvas.data.ignoreNextTimerEvent = False
    #ROYGBCV because tkinter doesn't like indigo well you know what THATS FINE
    elif event.keysym == "1":
        canvas.data.rainbows = "red"
        canvas.data.ohboy ==False
        canvas.data.ignoreNextTimerEvent = False
    elif event.keysym == "2":
        canvas.data.rainbows = "orange"
        canvas.data.ohboy ==False
        canvas.data.ignoreNextTimerEvent = False
    elif event.keysym == "3":
        canvas.data.rainbows = "yellow"
        canvas.data.ohboy ==False
        canvas.data.ignoreNextTimerEvent = False
    elif event.keysym == "4":
        canvas.data.rainbows = "green"
        canvas.data.ohboy ==False
        canvas.data.ignoreNextTimerEvent = False
    elif event.keysym == "5":
        canvas.data.rainbows = "blue"
        canvas.data.ohboy ==False
        canvas.data.ignoreNextTimerEvent = False
    elif event.keysym == "6":
        canvas.data.rainbows = "cyan"
        canvas.data.ohboy ==False
        canvas.data.ignoreNextTimerEvent = False
    elif event.keysym == "7":
        canvas.data.rainbows = "violet"
        canvas.data.ohboy ==False
        canvas.data.ignoreNextTimerEvent = False
    redrawAllSnake(canvas)

def gameOver(canvas):
    canvas.data.isGameOver = True

def timerFiredSnake(canvas):
    ignoreThisTimerEvent = canvas.data.ignoreNextTimerEvent
    canvas.data.ignoreNextTimerEvent = False
    if ignoreThisTimerEvent == False and canvas.data.isGameOver == False:
        moveSnake(canvas, canvas.data.snakeDrow, canvas.data.snakeDcol)
    canvas.data.ignoreNextTimerEvent == False
    delay = canvas.data.speed
    def f():
        timerFiredSnake(canvas)
    canvas.after(delay, f)
    redrawAllSnake(canvas)

def redrawAllSnake(canvas):
    color = canvas.data.rainbows
    score = canvas.data.snakeScore
    canvas.delete(ALL)
    drawSnakeBoard(canvas)
    if canvas.data.snakeScore < 500:
        canvas.create_text(10, 10, text = str(score) + ".", font = ("Baskerville", 25, "bold"), anchor = NW,
                           fill= color)
        canvas.create_text(10, 10, text = str(score) +".", font = ("Baskerville", 24, "bold"), anchor = NW,
                           fill = "white")
    if canvas.data.snakeScore > 500:
        #if you score above 500 he gets excited. 
        canvas.create_text(10, 10, text = str(score) + "!", font = ("Baskerville", 25, "bold"), anchor = NW,
                       fill= color)
        canvas.create_text(10, 10, text = str(score) +"!", font = ("Baskerville", 24, "bold"), anchor = NW,
                       fill = "white")
    if canvas.data.isGameOver == True:
        # also his name is Hamish
        color = canvas.data.rainbows
        xAnchor = canvas.data.canvasWidth/2
        yAnchor = canvas.data.canvasHeight/2
        #the snake, I mean.
        canvas.create_text(xAnchor, yAnchor, text = "Nope.", font = ("comic sans", 32, "bold"),
                           fill = color)
        canvas.create_text(xAnchor, yAnchor, text = "Nope.", font = ("comic sans", 31, "bold",),
                           fill = "white")

def initSnake(canvas):
    #numbers and things and stuff for reasons that are important
    canvas.data.isGameOver = False
    canvas.data.snakeScore = 0
    canvas.data.speed = 150
    canvas.data.scoreIncrement = 1
    canvas.data.rainbows = "green"
    canvas.data.timerColorCount = 0
    printInstructions()
    loadSnakeBoard(canvas)
    drawSnakeBoard(canvas)
    redrawAllSnake(canvas)

def findSnakeHead(canvas):
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = 0
    headCol = 0
    for row in range(rows):
        for col in range(cols):
            if snakeBoard[row][col] > snakeBoard[headRow][headCol]:
                headRow = row
                headCol = col
    canvas.data.headRow = headRow
    canvas.data.headCol = headCol
            

def printInstructions():
    print "Snake."
    print "Awesome."
    print "Coolest."
    print "You know what to do."
    print "Go hard or go home."
    print "+ does stuff"
    print "so does -"
    print "and numbers are fun too"
    print "have a"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n" # [REDACTED]
    print "blast."

def loadSnakeBoard(canvas):
    rows = canvas.data.rows
    cols = canvas.data.cols
    snakeBoard = [ ]
    for row in xrange(rows): snakeBoard += [[0]* cols]
    snakeBoard[rows/2][cols/2] = 1
    canvas.data.snakeBoard = snakeBoard
    findSnakeHead(canvas)
    placeFood(canvas)
    canvas.data.snakeDrow = 0
    canvas.data.snakeDcol = -1
    canvas.data.ignoreNextTimerEvent = False

def removeTail(canvas):
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if snakeBoard[row][col] > 0:
                snakeBoard[row][col] -= 1

def placeFood(canvas):
    rows = canvas.data.rows
    cols = canvas.data.cols
    snakeBoard = canvas.data.snakeBoard
    while True:
        foodRow = randint(0, rows-1)
        foodCol = randint(0, cols-1)
        if snakeBoard[foodRow][foodCol] == 0:
            break
    snakeBoard[foodRow][foodCol] = -1
        

def moveSnake(canvas, drow, dcol):
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols  = len(snakeBoard[0])
    headRow = canvas.data.headRow
    headCol = canvas.data.headCol
    newHeadRow = headRow + drow
    newHeadCol = headCol + dcol
    if newHeadRow < 0 or newHeadRow >= rows or newHeadCol < 0 or newHeadCol >= cols:
        #out of bounds oops
        gameOver(canvas)
    elif  snakeBoard[newHeadRow][newHeadCol] > 0:
        #stophittingyourself.gif
        gameOver(canvas)
    elif snakeBoard[newHeadRow][newHeadCol] == -1:
        snakeBoard[newHeadRow][newHeadCol] = snakeBoard[headRow][headCol] +1
        canvas.data.headRow = newHeadRow
        canvas.data.headCol = newHeadCol
        canvas.data.snakeScore += canvas.data.scoreIncrement
        placeFood(canvas)
        canvas.data.snakeDrow = drow
        canvas.data.snakeDcol = dcol
        redrawAllSnake(canvas)
    else:
        snakeBoard[newHeadRow][newHeadCol] = snakeBoard[headRow][headCol] +1
        canvas.data.headRow = newHeadRow
        canvas.data.headCol = newHeadCol
        removeTail(canvas)
        canvas.data.snakeDrow = drow
        canvas.data.snakeDcol = dcol
        redrawAllSnake(canvas)

def drawSnakeBoard(canvas):
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeBoardGrid(canvas, snakeBoard, row, col)

def drawSnakeBoardGrid(canvas, snakeBoard, row, col):
    color = canvas.data.rainbows
    margin = 5 # how fancy 
    gridSize = 30 # can you make this work without a margin I don't like the margin
    left = margin + col * gridSize
    right = left + gridSize
    top = margin + row * gridSize
    bottom = top + gridSize
    canvas.create_rectangle(left, top, right, bottom, fill = "black", outline = color)
    if snakeBoard[row][col] > 0:
        canvas.create_rectangle(left, top, right, bottom, fill = "white", outline = color)
    if snakeBoard[row][col] == -1:
        canvas.create_rectangle(left, top, right, bottom, fill = "white", outline = color)
    
    


def runSnake(rows, cols):
    # create the root and the canvas
    root = Tk()
    margin = 5
    gridSize = 30
    canvasHeight = 2*margin + rows* gridSize
    canvasWidth = 2*margin + cols*gridSize
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.rows = rows
    canvas.data.cols = cols
    canvas.data.margin = margin
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    canvas.data.ignoreNextTimerEvent = False
    canvas.data.isGameOver = False
    initSnake(canvas)
    # set up events
    root.bind("<Button-1>", lambda event: mousePressedSnake(canvas, event))
    root.bind("<Key>", lambda event: keyPressedSnake(canvas, event))
    timerFiredSnake(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

runSnake(20, 30)


