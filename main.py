import copy


class Computer:
    def __init__(self):
        pass
    def checkwin(self,board):
        zeros = 0
        win = 0
        for i in board:
            if i[0] == i[1] and i[0] == i[2] and i[0] != 0:
                win = i[0]
            for a in i:
                if a == 0:
                    zeros += 1

        if win == 0:
            for i in range(0, 3):
                if board[0][i] == board[1][i] and board[0][i] == \
                        board[2][i] and board[0][i] != 0:
                    win = board[0][i]
        if win == 0:
            if ((board[0][0] == board[1][1] and board[0][0] == board[2][
                2])
                or (board[0][2] == board[1][1] and board[0][2] == board[2][0])) \
                    and board[1][1] != 0:
                win = board[1][1]
        if win == 0 and zeros == 0:
            win = -1

        return win

    def copy(self,list):
        return copy.deepcopy(list)

    def get_best_move(self,board,play:int=2,deep:int=-1):
        board = self.copy(board)
        zeros = 0
        for i in board:
            for a in i:
                if a == 0:
                    zeros += 1
        if deep == -1:
            self.deep = zeros
        elif deep > zeros:
            self.deep = zeros
        else:
            self.deep = deep

        self.startboard = self.copy(board)
        self.play = play
        move = self.minmax(board)
        bestmove = max(move,key=move.get)
        move = bestmove.replace("[","").replace("]","").split(",")
        return (3*int(move[0]))+int(move[1])+1

    def minmax(self,board):
        board = self.copy(board)
        player = self.play

        scores = {}
        possibel_moves = self.getpossibelmoves(board)
        for move in possibel_moves:
            scores[str(move)] = self.evaluate_move(self.simulatemove(board, move, player), player,0)
        print(scores)
        return scores


    def evaluate_move(self,board,player,deep):
        if deep >= self.deep:
            return 0
        else:
            deep+=1
            board = self.copy(board)
            win = self.checkwin(board)
            if player == 1:
                player = 2
            else:
                player = 1
            if win == 0:
                score = 0
                possibel_moves = self.getpossibelmoves(board)
                for move in possibel_moves:
                    score += self.evaluate_move(self.simulatemove(board, move, player), player,deep)
                return score
            else:
                if win == self.play:
                    if deep == 1:
                        return 300000
                    else:
                        return 1*(1/(deep*deep))
                elif win == -1:
                    return 0
                else:
                    return -1*(1/(deep*deep))

    def getpossibelmoves(self,board):
        moves = []
        for pos1 in range(3):
            for pos2 in range(3):
                if board[pos1][pos2] == 0:
                    moves.append([pos1,pos2])
        return moves

    def simulatemove(self,board,move,player):
        board = self.copy(board)
        board[move[0]][move[1]] = player
        return board






class Game:
    def __init__(self, player: int):
        if player > 2:
            player = 2
        elif player < 1:
            player = 1
        self.numplayers = player
        self.board = [["1", "2", "3"],
                      ["4", "5", "6"],
                      ["7", "8", "9"]]
        self.comreadboard = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]
        self.player = "X"
        self.comreadplayer = 1
        self.win = 0
        self.computer = Computer()
        self.startgame()

    def convertpos(self,pos):
        if pos < 1 or pos > 9:
            return False,False
        if pos >= 4 and pos <= 6:
            pos2 = pos-4
            pos1 = 1

        elif pos <= 3:
            pos2 = pos-1
            pos1 = 0
        else:
            pos2 = pos-7
            pos1 = 2
        return pos1 ,pos2

    def checkmove(self, move):
        pos1,pos2 = self.convertpos(move)
        try:
            if self.comreadboard[pos1][pos2] == 0:
                return True
            else:
                return False
        except:
            return False

    def place(self,pos):
        if pos >= 4 and pos <= 6:
            pos -= 4
            self.board[1][pos] = self.player
            self.comreadboard[1][pos] = self.comreadplayer

        elif pos <= 3:
            pos -=1
            self.board[0][pos] = self.player
            self.comreadboard[0][pos] = self.comreadplayer
        else:
            pos -= 7
            self.board[2][pos] = self.player
            self.comreadboard[2][pos] = self.comreadplayer


    def nextturn(self):
        if self.comreadplayer == 1:
            self.comreadplayer = 2
            self.player = "$"
        else:
            self.comreadplayer = 1
            self.player = "X"

    def checkwin(self):
        zeros = 0
        for i in self.comreadboard:
            for a in i:
                if a == 0:
                    zeros += 1
            if i[0] == i[1] and i[0] == i[2] and i[0] != 0:
                self.win = i[0]
        if self.win == 0:
            for i in range(0, 3):
                if self.comreadboard[0][i] == self.comreadboard[1][i] and self.comreadboard[0][i] == self.comreadboard[2][i] and self.comreadboard[0][i] != 0:
                    self.win = self.comreadboard[0][i]
        if self.win == 0:
            if ((self.comreadboard[0][0] == self.comreadboard[1][1] and self.comreadboard[0][0] == self.comreadboard[2][2])
            or (self.comreadboard[0][2] == self.comreadboard[1][1] and self.comreadboard[0][2] == self.comreadboard[2][0])) \
            and self.comreadboard[1][1] != 0:
                self.win = self.comreadboard[1][1]
        if zeros == 0 and self.win == 0:
            self.win = -1
        return self.win
    def printboard(self,emty = True):
        if emty:
            for i in range(20):
                print()
        else:
            print()
            print()
        for i in self.board:
            print(f"{i[0]} {i[1]} {i[2]}")
            print()

    def playcomputer(self):
        move = self.computer.get_best_move(self.comreadboard,self.comreadplayer)
        return move

    def startgame(self):

        if self.numplayers == 1:
            self.singelplayer()
        else:
            self.multiplayer()

    def singelplayer(self):
        while self.win == 0:
            if self.comreadplayer == 2:
                self.printboard()
                check = False
                while check == False:
                    move = input(f"Player {self.player} where do you want to place: ")
                    try:
                        move = int(move)
                        check = self.checkmove(move)
                    except:
                        print("Error")
                self.place(move)
            else:
                self.place(self.playcomputer())
            self.checkwin()
            print(self.comreadboard)
            self.nextturn()
        self.won()

    def multiplayer(self):
        while self.win == 0:
            self.printboard()
            check = False
            while check== False:
                move = input(f"Player {self.player} where do you want to place: ")
                try:
                    move = int(move)
                    check = self.checkmove(move)
                except:
                    print("Error")
            self.place(move)
            self.checkwin()
            self.nextturn()
        self.won()



    def won(self):
        if self.win > 0:
            self.printboard()
            print(f"Player {self.win} Has won!")
        else:
            self.printboard()
            print("Draw!")


if __name__ == "__main__":
    player = None
    print("""
1 Player: you play against a minmax algorithm
WARNING Singleplayer Can run very slow on older computers
2 Players: you against an other human on the same machine(Online Not Coming Soon) """)
    while player == None:
        try:

            player = int(input("how manny players?(1/2):"))
        except:
            pass
    game = Game(player)
