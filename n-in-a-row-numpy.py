import numpy as np

# useful function for counting in array
def count(array,variable):  # counts occurrence of variable in array
    number = 0
    for row in range(array.shape[0]):           # iterating trough rows
        for column in range(array.shape[1]):    # iterating through column in this row
            if array[row,column] == variable:   # if variable is found
                number += 1                     # count one up
    return number       # function returns number of variables in given array
# useful function for generating array of strings
def generatestrarray(width, height, string):
    array = np.empty([width, height], dtype='object')
    for row in range(array.shape[0]):           # iterating trough rows
        for column in range(array.shape[1]):    # iterating through column in this row
            array[row, column] = string         # set cell to given string
    return array    # return filled array
# formatting class
class formatting:       # class containing strings used for formatting
    blue = '\033[94m'   # code for starting blue text
    red = '\033[91m'    # code for starting red text
    green = '\033[2;32m'# code for starting green text
    yellow = '\033[93m' # code for starting yellow text
    purple = '\033[95m' # code for starting purple text
    end = '\033[0m'     # code for ending current formatting
    pagebreak = 25 * '\n'   # pagebreak

# player class
class player:   # class containing the players functions
    def __init__(self,name,symbol,color):           # constructor
        self.symbol = color+symbol+formatting.end   # symbol is the character that is placed in a field by the player
        self.color = color                          # the players color code
        self.name = color+name+formatting.end       # name of the player plus color codes as it will be displayed
    def place(self):    # places the players symbol
        try:
            x = int(input('Enter '+formatting.blue+'x coordinate'+formatting.end+' for '+self.name+':')) - 1  # input x-coordinate with index starting at 1
            y = int(input('Enter '+formatting.red+'y coordinate'+formatting.end+' for '+self.name+':')) - 1   # input y-coordinate with index starting at 1
            if game.map[y,x] == game.freefield: # if field is free
                game.map[y,x] = self.symbol     # place symbol on map
            else:   # restart function if field is taken
                print(formatting.yellow+'This field is already taken. Try again.'+formatting.end)
                self.place()
        except (IndexError, ValueError): # excepting errors occurring when input is not correct
            print(formatting.yellow+'Sorry, but this is not a correct input. Please try again.'+formatting.end)
            self.place()    # restart function if error caused by input
    def checkforwin(self):  # method to check for a win
        print(formatting.pagebreak)     # scroll old map out of the users view
        won = False     # var to indicate if player has won
        inrows = []     # list of all combinations of symbols in a rows horizontally, vertically and diagonal (inrow) to check for a win
        for positionheight in range(game.height):   # iterate through column
            for positionwidth in range(game.width): # iterate through rows
                horizontallist = []     # lists the symbols of each inrow will be added
                verticallist = []
                diagonalrightlist = []
                diagonalleftlist = []
                for step in range(game.inarow): # stepping inarow times
                    try:
                        horizontallist.append(game.map[positionheight,positionwidth+step])  # getting next step for inrow horizontally
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing ang go on because these cases dont met winning conditions
                    try:
                        verticallist.append(game.map[positionheight + step, positionwidth]) # getting next step for inrow down
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing ang go on because these cases dont met winning conditions
                    try:
                        diagonalrightlist.append(game.map[positionheight + step, positionwidth + step]) # getting next step for inrow diagonally left
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing ang go on because these cases dont met winning conditions
                    try:
                        diagonalleftlist.append(game.map[positionheight + step, positionwidth - step])  # getting next step for inrow diagonally right
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing and go on because these cases dont met winning conditions
                inrows.extend([horizontallist,verticallist,diagonalrightlist,diagonalleftlist])
        for inrow in inrows:    # iterating through all possible combinations of rows to check
            if inrow.count(self.symbol) == len(inrow) and len(inrow) == game.inarow:
                won = True      # if the inrow only consists on the players symbol and is inarow long the player wins
        if won:                         # routine to start if player has won
            print(self.name+formatting.yellow+' won!'+formatting.end)    # print winners name
            game.map.fill(self.symbol)  # fill map with winner's symbol to break mainloop
        else:   # nobody has won yet
            print('Nobody has won yet.')

# game class
class game:     # class containing all game assets and mainloop
    def __init__(self,width,height,inarow,freefield):    # constructor
        self.width = width      # width of map
        self.height = height    # height of map
        self.inarow = inarow    # symbols in a row needed to win
        self.freefield = freefield  # symbol that is displayed when the field is free
        self.map = generatestrarray(width,height,freefield)     # map containing whitespaces is generated by function
    def printmap(self):     # function to print the map
        print('    ┎' + (self.width - 1) * '───┬' + '───┐')     # print the first line of the box around the map
        print('    ┃ '+formatting.blue+(formatting.end+' │ '+formatting.blue).join(map(str, list(range(1, self.width+1))))+formatting.end+' │')  # print top of board by printing column numbers separated by |
        print('┍━━━╋'+(self.width - 1)*'━━━┿'+'━━━┥')           # print separator between top line and map
        rownr = 1  # number of current row
        for row in self.map.tolist():    # iterating through rows of map except last
            print('│ '+formatting.red+str(rownr)+formatting.end+' ┃ '+' │ '.join(row)+' │')  # printing all fields in a row separated by a │ with line number
            if rownr == len(self.map.tolist()):                     # if last row:
                print('└───┸' + (self.width - 1) * '───┴' + '───┘') # print last line
                break   # end loop before a standard line can be placed under last line
            print('├───╂' + (self.width - 1) * '───┼' + '───┤')     # printing separator with dynamic length after each row except for the last
            rownr += 1  # set number to of next row
    def play(self):     # function containing mainloop
        print('Welcome to a fun game of TicTacToe')   # welcome to play my game
        print('To win you have to place',game.inarow,'of your Symbols in a vertical, horizontal or diagonal row.')
        print('Currently',player1.name,'('+player1.symbol+')','is playing against',player2.name,'('+player2.symbol+')'+'.\n')
        self.printmap()                 # print first map
        while count(self.map, self.freefield) > 0:   # the game runs until all fields are filed
            if count(self.map, self.freefield) % 2:  # player1 plays when number of free fields is even
                player1.place()         # letting player1 place his symbol
                player1.checkforwin()   # checking if player1 has won
                self.printmap()         # print the map
            else:                       # same for player2, he plays when number of free fields is uneven
                player2.place()         # letting player2 place his symbol
                player2.checkforwin()   # checkin if player2 has won
                self.printmap()         # print the the map

# setup
player1 = player(name='Alice', symbol='☓', color=formatting.purple) # object player one
player2 = player(name='Bob', symbol='○', color=formatting.green)    # object player two
game = game(width=5, height=5, inarow=3, freefield=' ')             # game instance
game.play()                                                         # start the game