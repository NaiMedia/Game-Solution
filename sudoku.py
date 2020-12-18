from random import sample
from copy import deepcopy


base  = 3
side  = base*base
rBase = range(base)
symbol = " 123456789"
# pattern for a baseline valid solution
def pattern(r,c):
	return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)


def shuffle(s):
	return sample(s,len(s))

nums  = shuffle(range(1,base*base+1))

def grid_layout(rBase):
	axis = []
	for g in shuffle(rBase):
		for r in shuffle(rBase):
			axis.append(g*base +r)
	return axis

rows = grid_layout(rBase)
cols = grid_layout(rBase)

# rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
# cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]



def expandLine(line):
    return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]

#draws the lines around our board
def print_board(b):

	line0  = expandLine("╔═══╤═══╦═══╗")
	line1  = expandLine("║ . │ . ║ . ║")
	line2  = expandLine("╟───┼───╫───╢")
	line3  = expandLine("╠═══╪═══╬═══╣")
	line4  = expandLine("╚═══╧═══╩═══╝")
	nums2   = [ [""]+[symbol[n] for n in row] for row in b ]
	print(line0)
	for r in range(1,side+1):
		print( "".join(n+s for n,s in zip(nums2[r-1],line1.split("."))) )
		print([line2,line3,line4][(r%side==0)+(r%base==0)])

def puzzle():
	# board = []
	# for c in cols:
	# 	for r in rows:
	# 		board.append(nums[pattern(r,c)])
	# print_board(board)


	# produce board using randomized baseline pattern
	board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
	#copy the filled in board into board0
	board0 = deepcopy(board)

	# getting numbers out
	squares = side*side
	empties = squares * 3//4
	for p in sample(range(squares),empties):
		board[p//side][p%side] = 0
	return(board0, board)

	
# b0 had the original filled in board without any blanks. b is the final puzzle
# with some numbers taken out.

(b0, b) = puzzle()
print('===   Puzzle board  ===')
print_board(b)

print('=== Initial filled in board ===')
print_board(b0)	
