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


# Pattern for a baseline puzzle grid, which we will use later when we create
# our valid solution. Using our base and side variables, our pattern function 
# will format our list of lists.
   
def pattern(r,c):
	return (base*(r%base)+r//base+c)%side

# We define a shuffle function using the sample method from random.
# The sample() method returns a list of unique elements chosen
# randomly from the list provided without repetition. The randomly 
# selected list consists of the length of items we provide to the 
# shuffle function.

def shuffle(s):
	return sample(s,len(s))

# In our nums variable, we provide our shuffle function the range of
# numbers 1 through one more than our side variable, which we will then
# shuffle. By definition of our shuffle function the length will be 9 in
# this case. 

nums  = shuffle(range(1, side + 1))

# We define a grid layout function that we use in conjuction with our 
# pattern function. We use the empy list axis in order to access the numbers
# we will then use as inputs for our pattern function. Because we are 
# shuffling our rBase, the numbers that are returned in axis will be random calculations
# of 0, 1, or 2 times base. 


def grid_layout(rBase):
	axis = []
	for g in shuffle(rBase):
		for r in shuffle(rBase):
			axis.append(g*base + r)
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

	nums2   = [ [""]+[symbol[n] for n in row] for row in b]
	print(line0)
	for r in range(1,side+1):
		print( "".join(n+s for n,s in zip(nums2[r-1],line1.split("."))) )
		print([line2,line3,line4][(r%side==0)+(r%base==0)])

def puzzle():
	
	# produce board using randomized baseline pattern function and shuffling function.
	# pattern function is used as an indices assigner to select the placement of the 
	# numbers chosen by nums.

	board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

	# This varialbe copies the original filled in board into board0
	board0 = deepcopy(board)

	# This part of the puzzle() function is randomly removing numbers from our original board. 
	
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
