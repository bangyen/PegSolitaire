def main():
	

	# handle the game

	
	print("""
	
	WELCOME TO CS300 PEG SOLITAIRE!
	===============================
	
	Board Style Menu
	
	1) Cross
	2) Circle
	3) Triangle
	4) simple T 
	
	""")
	
	boardvalue = readValidBoardValue()
	print(f'choose a board stype : {boardvalue}')
	
	Board = makeBoard(boardvalue)
	print(' \n' + printBoard(Board))
	
	while not gamewon(Board) or noMovesleft(Board):
		
		col,row = getColRow()
		print(' \n' + f'choose a column : {col}')
		print(' \n' + f'choose a row : {row}')
		
		moves,locations = checkNeighbours(row - 1, col - 1, Board)
		print(' \n' + 'chose from the moves :' + ' '.join(moves))
		
		Board = UpadteBoard(row - 1, col - 1, Board, getMove(moves), locations)
		print(' \n' + printBoard(Board))
	
	if gamewon():
		print('you won the game')
	elif noMovesleft(Board) and not gamewon(Board):
		print('you lost the game')
		
		
		
def UpdateBoard(row,col,Board,moveToTake,locations):
# 	the func will take the move choosen by user on the board and update it
	
# 	@param Board: the board on which move has to be taken
# 	@param move: the direction in which peg would move
	
	newBoard = Board
	
	dict = {
		'up' = 0,
		'down' = 1,
		'left' = 2,
		'right' = 3
	}
	
	locToMove = locations[dict[moveToTake]]['tomove']
	locRemove = locations[dict[moveToTake]]['remove']
	
	newBoard[locToMove[0]][locToMove[1]] = 1
	newBoard[locRemove[0]][locRemove[1]] = 0
	newBoard[row][col] = 0 
	
	return newBoard
	
	
def gamewon(Board):
# 	func would tell if we won the the game by using the criteria that 
# 	only one peg is left on the board 
	
# 	@param Board: the board on which we are checking the pegs
# 	@return bollean: true or false depending on game won or not
	
	count = 0
	
	for row in Board:
		count += row.count(1)
	
	return count == 1
	


def noMovesleft(Board):
	
# 	func tells if there is any move left
	
# 	@param board: the board for which we will check moves
# 	@return bollean: true or false depending on moves are left or not

	movesleft = 0
	for i in range(len(Board)):
		for j in range(len(Board[0]):
			if Board[i][j] == 1:
				moves = checkNeighbours(i,j,Board)[0]
				movesleft+=len(moves)
	return movesleft <= 0
		
			

def checkNeighbours(col,row,Board):
	
# 	check for pegs around the specific peg with given col and row on a board
	
# 	@param col: the column of the peg
# 	@param row: the row of the peg
# 	@param board:the board on which the pegs are
# 	@return list of Neighbours around the specific peg
	
	moves = []
	locations = []
	
	# check up
	uprow = row - 1
	upcol = col
	
	if inbound(uprow,upcol,Board) and inbound(uprow - 1,upcol,Board):
		if Board[uprow][upcol] == 1 and Board[uprow - 1][upcol] == 0:
			moves.append('up')
			locations.append({'moveto' : [uprow-1,upcol], 'remove' : [uprow,upcol]})
		
	
	# check down
	downrow = row + 1
	downcol = col
	
	if inbound(downrow,downcol,Board) and inbound(downrow + 1,dowcol,Board):
		if Board[downrow][downcol] == 1 and Board[downrow + 1][downcol] == 0:
			moves.append('down')
			location.append({'moveto' : [downrow + 1,downcol], 'remove' : [downrow,downcol]})
		          
	
	# check left
	leftcol = col - 1
	leftrow = row
	
	if inbound(leftrow, leftcol, Board) and inbound(leftrow, leftcol - 1, Board):
		if Board[leftrow][leftcol] == 1 and Board[leftrow][leftcol - 1] == 0:
			moves.append('left')
			location.append({'moveto' : [leftrow, leftcol - 1], 'remove' : [leftrow, leftcol]})
		
	
	# check right
	rightcol = col + 1
	rightrow = row
	
	if inbound(rightrow, rightcol, Board) and inbound(rightrow, rightcol + 1, Board):
		if Board[rightrow][rightcol] == 1 and Board[rightrow][rightcol + 1] == 0:
			moves.append('right')
			location.append({'moveto' : [rightrow, rightcol + 1], 'remove' : [rightrow, rightcol]})
	
	
	return moves, locations
	


def getMove(moves, message='pls tell the move you would like to make'):
	
# 	the func will ask the user to input a valid move 
# 	and if not valid will ask again
	
# 	@param moves: is a list of optimal moves
# 	@param message: the string the user will get while entering the input 
# 	@return int or string specific to the move the user chose
	
	value = input(message)
	if value in range(1, len(moves)) or value in moves:
		return value
	return getMove(moves,message = 'invalid input pls try again')
		
	
		
	


def getColRow(Board,message = 'pls tell the column and row in the format "col row"'):
	
# 	the func will ask user to input col and row number but if it is out of bound it will keep on askingfor it
	
# 	@param Board: the 2d array for which we need the col and row number
# 	@param message: string which apears when player fills the input
# 	@return vector of col and row

	col, row = input(message).split(' ')
	if row <= len(Board) and col <= len(board[0]):
		return col, row
	return getColRow(Board, message='the values you filled were out of bound(format: col row)')
		
	

	
	
	
def printBoard(Board):
	
# 	convert 2d board with values ranging from -1 to 1 into symbols (@,_,#) to represent it visually 
	
# 	@param Board: d list of intigers representing a board
# 	@return visualBoard: an array of rows of board represented with @,_,#
	
	rowcount = 0
	visualBoard = []
	
	for row in Board:
		rowcount += 1
	    newRow = ''.join(map(convertValToSym, row).insert(0, rowcount))
		visualBoard.append(newRow)
		
	return visualBoard.insert(0, range(len(Board[0]) + 1))	
	
	

def convertValToSym(val):
	
# 	converts board values into symbols for visual representation
# 	-1 to #, 0 to _ and 1 to @ 
	
# 	@param val is an int ranging from -1 to 1
# 	@return string ranging from #,_,@ 
	
	return ['-', '@', '#'][val] if val in [-1, 0, 1] else None
		


def readValidBoardValue(message = 'pls fill in the board type'):
	
# 	    the func will check if the input by user is valid or not and if not the ask 
# 		them to refill it by running the func again with error message
		
# 		@param messsage: the message shown while taking in the input
# 		@return value: the int or string for specific board type
	
	value = input(message)
	
	if value not in range(1, 5) and value not in ['cross', 'circle', 'triangle', 'simple_T', 'simple T']:
	    return readValidBoardValue(message='the value you filled was out of bound')
	return value
		

def makeBoard(type):
	
# 	@param: takes in a string or int for specific type of board | @return a 2d board (2 dimensional list)
# 	1)cross 2)circle 3)triangle 4)simple_T
# 	 '1' represents a peg 
# 	 '0' represents an empty space
# 	'-1' represents a non play-able space
	
	if type == 1 or type == 'cross:
		return [
			[-1,-1,-1, 1, 1, 1,-1,-1,-1],
			[-1,-1,-1, 1, 1, 1,-1,-1,-1],
			[ 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[ 1, 1, 1, 1, 0, 1, 1, 1, 1],
			[ 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[-1,-1,-1, 1, 1, 1,-1,-1,-1],
			[-1,-1,-1, 1, 1, 1,-1,-1,-1]
		]
	elif type == 2 or type == 'circle':
		return [
			[-1, 0, 1, 1, 0,-1],
			[ 0, 1, 1, 1, 1, 0],
			[ 1, 1, 1, 1, 1, 1],
			[ 1, 1, 1, 1, 1, 1],
			[ 0, 1, 1, 1, 1, 0],
			[-1, 0, 1, 1, 0,-1]
		]
		
	elif type == 3 or type == 'tiangle':
		return [
			[-1,-1,-1, 0, 1, 0,-1,-1,-1],
			[-1,-1, 0, 1, 1, 1, 0,-1,-1],
			[-1, 0, 1, 1, 0, 1, 1, 0,-1],
			[ 0, 1, 1, 1, 1, 1, 1, 1, 0]
		]
		
	elif type == 4 or type in ['simple_T', 'simple T']:
		return [
			[ 0, 0, 0, 0, 0],
			[ 0, 1, 1, 1, 0],
			[ 0, 0, 1, 0, 0],
			[ 0, 0, 1, 0, 0],
			[ 0, 0, 0, 0, 0]
		]
	 	
		
def inbound(row,col,array):
	return row in range(len(array)) and col in range(len(array[0]))
