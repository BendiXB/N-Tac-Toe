import numpy as np

# usefull function
def count(array,variable):  # counts occurrence of variable in array
    number = 0
    for row in range(array.shape[0]): # iterating trough rows
        for column in range(array.shape[1]): # iterating through column in this row
            if array[row,column] == variable:  # if variable is found
                number += 1  # count one up
    return number   # function returns number of variables in given array

# player class
class player:   # class containing the players functions
    def __init__(self,name,symbol): # constructor
        self.symbol = symbol    # symbol is the character that is placed in a field by the player
        self.name = name    # name of the player
    def place(self):    # places the players symbol
        try:
            x = int(input('Enter x position for '+self.name+':')) - 1   # input x-coordinate with index starting at 1
            y = int(input('Enter y position for '+self.name+':')) - 1   # input y-coordinate with index starting at 1
            if game.map[y,x] == 0:  # if field is not taken
                game.map[y,x] = self.symbol # place symbol on map
            else:   # restart function if field is taken
                print('This field is already taken. Try again.')
                self.place()
        except (IndexError, ValueError): # excepting errors occurring when input is not correct
            print('Sorry, but this is not a correct input. Please try again.')
            self.place()    # restart function if error caused by input
    def checkforwin(self):  # method to check for a win
        print(20*'\n')      # scroll old map out of the users view
        won = False     # var to indicate if player has won
        inrows = []     # list of all combinations of symbols in a rows horisontaly, verticaly and diagonal (inrow) to check for a win
        for positionheight in range(game.height):   # iterate through column
            for positionwidth in range(game.width): # iterate through rows
                horizontallist = []     # lists the symbols of each inrow will be added
                verticallist = []
                diagonalrightlist = []
                diagonalleftlist = []
                for step in range(game.inarow): # stepping inarow times
                    try:
                        horizontallist.append(game.map[positionheight,positionwidth+step])  # getting next step for inrow horisontaly
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing ang go on because these cases dont met winning conditions
                    try:
                        verticallist.append(game.map[positionheight + step, positionwidth]) # getting next step for inrow horisontaly
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing ang go on because these cases dont met winning conditions
                    try:
                        diagonalrightlist.append(game.map[positionheight + step, positionwidth + step]) # getting next step for inrow horisontaly
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing ang go on because these cases dont met winning conditions
                    try:
                        diagonalleftlist.append(game.map[positionheight + step, positionwidth - step])  # getting next step for inrow horisontaly
                    except IndexError:  # excepting the case that a inrow goes out of board
                        pass            # do nothing ang go on because these cases dont met winning conditions
                inrows.extend([horizontallist,verticallist,diagonalrightlist,diagonalleftlist])
        for inrow in inrows:    # iterating through all possible combinations of rows to check
            if inrow.count(self.symbol) == len(inrow) and len(inrow) == game.inarow:
                won = True  # if the inrow only consists on the players symbol and is inarow long the player wins
        if won: # routine to start if player has won
            print(self.name,' won!')    # print winners name
            game.map.fill(self.symbol)  # fill map with winner's symbol to break mainloop
        else:   # nobody has won yet
            print('Nobody has won yet.')

# game class
class game:     # class containing all game assets and mainloop
    def __init__(self,width,height,inarow):    # constructor
        self.width = width      # width of map
        self.height = height    # height of map
        self.inarow = inarow    # symbols in a row needed to win
        self.map = np.zeros((self.height,self.width),int)   # map is an np array filled with zeros
    def printmap(self):     # function to print the map
        print('   ┃ '+' │ '.join(map(str, list(range(1, self.width+1))))+' │')
        print('━━━╋'+self.width * '━━━╋')
        rownr = 1  # number of current row
        for row in self.map.tolist():    # iterating through rows of map
            print(' '+str(rownr)+' ┃ '+' │ '.join(list(map(str, row)))+' │')  # printing all fields in a row separated by a │
            print('───╋'+len(row) * '───┼')  # printing separator with dynamic length after each row
            rownr += 1  # Number of next row
    def play(self):         # function containing mainloop
        print('Welcome to a fun game of TicTacToe')   # welcome to play my game
        print('To win you have to place',game.inarow,'of your Symbols in a vertical, horizontal or diagonal row.')
        print('Currently',player1.name,'is playing against',player2.name +'.\n')
        self.printmap()     # print first map
        while count(self.map, 0) > 0:   # the game runs until all fields are filed
            if count(self.map, 0) % 2:  # player1 plays when number of free fields is even
                player1.place()         # letting player1 place his symbol
                player1.checkforwin()   # checking if player1 has won
                self.printmap()         # print the map
            else:                       # same for player2, he plays when number of free fields is uneven
                player2.place()         # letting player2 place his symbol
                player2.checkforwin()   # checkin if player2 has won
                self.printmap()         # print the the map

# setup
player1 = player(name='Alice', symbol=1)    # object player one
player2 = player(name='Bob', symbol=2)      # object player two
game = game(width=5, height=5, inarow=3)    # game instance
game.play()     # start the game