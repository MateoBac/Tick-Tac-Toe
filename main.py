class game:
    def __init__(self):
        #settings
        self.external1 = False
        self.external2 = False #These are yoused to use some other code to make player inputs like machine learning
        self.endless = True # if true a new game starts imidiandly after a game ends

        #def
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.player = 2
        self.winner = 0
        self.places = 0
        self.end = True
        self.error = False
        self.error2 = False
        #start
        self.gameloop()
    def gameloop(self):
        while self.end:
            self.swich_players()
            self.play()
        if self.endless:
            self.__init__()
            return
    def print_board(self):
        for i in range(0,20):
            print('')
        if self.error:
            print('This is not a number please try again')
            self.error = False
        if self.error2:
            print('That spot is already Taken please chose a different one')
            self.error2 = False
        print(f"its player {self.player} turn")
        print(f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}')
        print("-----")
        print(f'{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}')
        print("-----")
        print(f'{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}')
        return
    def swich_players(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1
        else:
            self.player = 1
            print('Error invalid nuber found: The New player ist nuber 1')
        if self.player == 1:
            self.symbole = 'O'
        elif self.player == 2:
            self.symbole = 'X'
        self.places += 1
        return
    def play(self):
        if self.external1 and self.player == 1:
            self.extertal1()
            self.check_win()
            return
        elif self.external2 and self.player == 2:
            self.external2()
            self.check_win()
            return
        self.print_board()
        column = input('in which column you wanna place? 0/1/2\n')
        row = input('in which row you wanna place? 0/1/2\n')
        try:
            row = int(row)
            column = int(column)
            if self.board[row][column] == ' ':
                self.board[row][column] = self.symbole
            else:
                self.error2 = True
                self.play()
                return
            self.check_win()
            return
        except:
            self.error = True

            self.play()
            return
    def win(self):
        self.winner = self.player
        self.end = False
        print(f"Player {self.winner} won the game in {self.places} placements")
    def draw(self):
        self.end = False
        print('Game ended bc. of no more space')
    def check_win(self):
        board = self.board
        if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != ' ':
            self.win()
        elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != ' ':
            self.win()
        elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != ' ':
            self.win()
        elif board[0][0] == board[1][1] and board[0][0] == board[2][2]and board[0][0] != ' ':
            self.win()
        elif board[0][2] == board[1][1] and board[0][2] == board[2][0]and board[1][1] != ' ':
            self.win()
        if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != ' ':
            self.win()
        if board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != ' ':
            self.win()
        if board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != ' ':
            self.win()
        if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
            self.draw()
        return
    def extertal1(self):
        pass
        """
        Here you are abel to put you own code to play as a Player the code to place a think: 
        self.board[row][column] = self.symbole
        WARNING: your submisson is in now way checked if it is a valid move it if it isn't The Program might crash or you could override a previous move
        Valid Moves:
        row = 0-2
        column = 0-2
           0 1 2
         0 # # #
         1 # # #
         2 # # #
        """
    def external2(self ):
        pass
        #read here:
        self.extertal1()

if __name__ =='__main__':
    game = game()
