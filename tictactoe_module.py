class outcomes:

    # checks if there is a win loss or draw
    def checker(self, side: str) -> bool:

        # dict of all options that results in a win 
        self.dict_board = {'across top':[self.test_board[0],self.test_board[1],self.test_board[2]],
                  'acroos mid':[self.test_board[3],self.test_board[4],self.test_board[5]],
                  'across bot':[self.test_board[6],self.test_board[7],self.test_board[8]],
                  'down left':[self.test_board[0],self.test_board[3],self.test_board[6]],
                  'down mid':[self.test_board[1],self.test_board[4],self.test_board[7]],
                  'down right':[self.test_board[2],self.test_board[5],self.test_board[8]],
                  'dia topleft':[self.test_board[0],self.test_board[4],self.test_board[8]],
                  'diag topright':[self.test_board[2],self.test_board[4],self.test_board[6]]}

        # iterates through dict checking for three in a row
        for i in self.dict_board:
            if self.dict_board[i].count(side) == 3:
                return True


    # creating changes for X and O to be different
    # creates a decision tree for every possible outcome
    def paths(self, board: list, spot: int, switcher: int = 0):

        #
        for j in [i for i in board if type(i) == int]:
            self.test_board = board[:]
            if switcher % 2 == 0:
                side = 'O'
                self.test_board[j-1]= 'O'
            else:
                side = 'X'
                self.test_board[j-1]= 'X'
            if  self.checker('X'):
                self.outc_dict[spot][0] += 1
                continue
            elif self.checker('O'):
                self.outc_dict[spot][1] += 1
                continue
            elif self.test_board.count('X') == 5:
                self.outc_dict[spot][2] += 1
            else:
                self.paths(self.test_board, spot, switcher + 1)
                
    
    # creates a seperate loop for first moves to organize into outc_dict
    def firstMove(self, board: list):

        #
        self.outc_dict = {}
        for j in [i for i in board if type(i) == int]:
            self.outc_dict[j] = [0,0,0]
            self.test_board = board[:]
            self.spot = j
            self.test_board[j-1]= 'X'
            if  self.checker('X'):
                self.outc_dict[j][0] += 1
            elif self.test_board.count('X') == 5:
                self.outc_dict[j][2] += 1
            else:
                self.paths(self.test_board, self.spot)
        return self.outc_dict






