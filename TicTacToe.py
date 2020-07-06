import numpy as np

# usefull function
def count(array,variable):  # counts occurrence of variable in array
    number = 0
    for row in range(array.shape[0]): # iterating trough rows
        for column in range(array.shape[1]): # iterating thou column in this row
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
        for positionheight in range(game.height):   # iterate thou column
            for positionwidth in range(game.width): # iterate thou rows
                # check horizontally
                horizontallist = [] # list used to check the map
                try:
                    for step in range(game.inarow): # stepping inarow times to the right
                        horizontallist.append(game.map[positionheight,positionwidth+step])  # appending steps to list
                except IndexError:  # clear list if index goes out of map because it cant be a win
                    horizontallist = []
                if horizontallist.count(self.symbol) == len(horizontallist) and len(horizontallist) == game.inarow:
                    won = True  # game is won when exacly inarow times the players symbol is found in a row
                # check vertical
                verticallist = [] # list used to check the map
                try:
                    for step in range(game.inarow): # stepping inarow times down
                        verticallist.append(game.map[positionheight+step,positionwidth])  # appending steps to list
                except IndexError:  # clear list if index goes out of map because it cant be a win
                    verticallist = []
                if verticallist.count(self.symbol) == len(verticallist) and len(verticallist) == game.inarow:
                    won = True  # game is won when exacly inarow times the players symbol is found in a row
                # check diagonal right
                diagonalrightlist = []  # list used to check the map
                try:
                    for step in range(game.inarow):  # stepping inarow times diagonaly right
                        diagonalrightlist.append(game.map[positionheight + step, positionwidth+step])  # appending steps to list
                except IndexError:  # clear list if index goes out of map because it cant be a win
                    diagonalrightlist = []
                print(diagonalrightlist)
                if diagonalrightlist.count(self.symbol) == len(diagonalrightlist) and len(diagonalrightlist) == game.inarow:
                    won = True  # game is won when exacly inarow times the players symbol is found in a row
                # check diagonal left
                diagonalleftlist = []  # list used to check the map
                try:
                    for step in range(game.inarow):  # stepping inarow times diagonaly left
                        diagonalleftlist.append(game.map[positionheight + step, positionwidth - step])  # appending steps to list
                except IndexError:  # clear list if index goes out of map because it cant be a win
                    diagonalleftlist = []
                print(diagonalleftlist)
                if diagonalleftlist.count(self.symbol) == len(diagonalleftlist) and len(diagonalleftlist) == game.inarow:
                    won = True  # game is won when exactly inarow times the players symbol is found in a row
        if won:     # routine to start if player has won
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
        lmap = self.map.tolist()    # converting map from array to lists in lists for convenient merging
        for row in lmap:    # iterating thru rows
            print(len(row) * '────' + '─')  # printing separator with dynamic length before each row
            print('│ '+' │ '.join(list(map(str, row)))+' │')  # printing all fields in a row separated by a │
        print(len(row) * '────' + '─')  # print last map
    def play(self):         # function containing mainloop
        print('Welcome to a fun game of TicTacToe')   # welcome to play my game
        print('To win you have to place',game.inarow,'of your Symbols in a diagonal or horizontal row.')
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