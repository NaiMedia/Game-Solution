# Sudoku Generator
# Our Sudoku board is generated as a nested list (i.e a list of
# 9 lists with 9 numbers within each list.) Our generator creates
# a 9 X 9 matrix consisting of nine 3 X 3 smaller matrices.     
from random import sample
from copy import deepcopy


base  = 3
side  = base*base
rBase = range(base)
symbol = " 123456789"


# Pattern for a baseline valid solution. Our pattern will assign
# the index of each inner and outer list 3 X 3 at a time from left
# to right.  

def pattern(r,c):
	return (base*(r%base)+r//base+c)%side

# We define a shuffle function using the sample mathod from random
# The sample() methon that returns a list of unique elements chosen
# randomly from the list provided. The randomly selected list consists
# of a specified number of items provided.

def shuffle(s):
	return sample(s,len(s))

# In this case we enter the range of 1 through 9 for our 9 X 9 sudoku

nums  = shuffle(range(1,base*base+1))

# We define a grid layout function that we use in conjuction with our 
# pattern function to create each inner list within our main
# outer list as well as outer list. We do this by shuffling the numbers
# 0, 1, 2 multipying them by our base (in this case 3) then adding another
# random number from 0,1,or 2. This will be used in conjuction with the 
# pattern function. 

def grid_layout(rBase):
	axis = []
	for g in shuffle(rBase):
		for r in shuffle(rBase):
			axis.append(g*base +r)
	return axis

rows = grid_layout(rBase)
cols = grid_layout(rBase)

# next two functions are used to draws the grid lines around our board

def expandLine(line):
    return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]


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
	
	# produce board using randomized baseline pattern
	board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

	# copy the filled in board into board0
	board0 = deepcopy(board)

	# getting numbers out of our grid. 
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
