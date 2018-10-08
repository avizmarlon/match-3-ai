## DO NOT ATTEMPT TO DECIDE THE BEST MOVE BASED ON FUTURE POSSIBLE BOARD POSITIONS
## THE FRUITS THAT APPEAR ARE RANDOM AND THUS UNPREDICTABLE.
## THE BEST MOVE IS THE ONE YOU ARE 100% SURE.



# reference:
# https://forums.socialpointgames.com/topic/9770/the-fruit-puzzle-island-event-sep-27th-oct-8th

#Horizontal booster: Match 4 fruit in a line with a horizontal swap to create it. When used in a match it will clear an entire row!
#Vertical booster: Match 4 fruit in a line with a vertical swap to create it. When used in a match it will clear an entire column!
#Area booster: match 5 or 6 fruit in a T-shape or an L-shape to create it. When used in a match it will collect all the fruit around it!
#Star booster: match 5 fruit in a line to create it. You can swap it with any color to collect all the fruit with that color!

#You can also combine 2 boosters that are next to each other for even more powerful effects:

#Combining 2 area boosters will clear an ever bigger area
#Combining 2 star boosters will clear the entire board!
#Any other combination will clear 3 rows or 3 columns

## when a match is made, all fruits (including new ones) will fall first before
## the game check for other cascated matches and so on

## If I have a possible solution and I can verify it as correct 
## quickly, can I also find that same solution quickly?
## In other words, P=NP?

## ToDo
## After the IA is capable of calculating exacly what happens with each move
## (missing being able to calculate what happens when a match makes a booster
## explode), it should simulate the board after the match was made and see if
## other matches will happen in a chain. If so, update the board again and run
## another simulation to check for more chain matches; repeat until there are
## no matches left. In order to do that we will get the final board_state after
## the state has been calculated and run it through traverse() with a few
## different rules.

## Meanwhile, while the matches are being made, a value should be calculated
## with each match to determine the value of a move and compare to other moves
## to be able to decide what is the best move.

## 1. How to calculate the outcome of a match when the match makes a
## booster explode?

## Idea (Theory): when checking for which [row][col] are cleared by the match, make
## each of these positions represent an empty property (like replacing the
## fruit letter for a '/' or '1') and before making the fruit above go down
## compute the positions that are cleared by the booster that exploded.
## Replace all fruit letters that disappear with the match (including
## the ones cleared by the booster that exploded when the match was made) with
## a character to represent empty and after that, compute the fruits above
## going rows down.
##
## Note: The central fruit (if it creates a booster) that triggered the match
## does NOT disappear when the match is made, even if a booster nearby explodes.
## It simply goes rows down.
##
## Idea (Practical): after replacing all fruit letter that disappeared in a match with a
## character that represents empty ('/' for example), create a function
## that will search for all '/' characters and replace them by the fruits above
## check vertical by vertical (column by column) and the fruits above the '/'s
## will go rows down equal to the amount of '/'s in that column. Similar to
## rows_to_move.

fruit_letters = {'R': 'Red', 'Y': 'Yellow', 'B': 'Blue', 'G': 'Green', 'P': 'Purple',
				 'O': 'Orange'}
fruit_initials = ['R', 'Y', 'B', 'G', 'P', 'O']

#       col1 col2 col3 col4 col5 col6 col7 col8 col9
row1 = ['X', 'Y', 'B', 'B', 'X', 'Y', 'G', 'B', 'X']
row2 = ['B', 'Y', 'R', 'G', 'B', 'G', 'Y', 'Y', 'R']
row3 = ['B', 'R', 'R', 'O', 'Y', 'G', 'P', 'Y', 'Y']
row4 = ['G', 'Y', 'Y', 'O', 'O', 'B', 'Y', 'B', 'Y']
row5 = ['G', 'O', 'Y', 'R', 'B', 'G', 'O', 'O', 'B']
row6 = ['X', 'Y', 'O', 'G', 'G', 'R', 'B', 'O', 'X']
row7 = ['X', 'X', 'R', 'R', 'Y', 'G', 'O', 'X', 'X']
row8 = ['X', 'X', 'X', 'O', 'G', 'B', 'X', 'X', 'X']
row9 = ['X', 'X', 'X', 'X', 'G', 'X', 'X', 'X', 'X']

rows_properties = {
		'row1': {'col1': {'hasModifier': False, 'modifier': None}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': 'row-1'}, 
				'col9': {'hasModifier': False, 'modifier': None},
		},

		'row2': {'col1': {'hasModifier': False, 'modifier': None}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': 'row-2'}, 
				'col9': {'hasModifier': False, 'modifier': None},
		}, 

		'row3': {'col1': {'hasModifier': False, 'modifier': None}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': 'row-3'}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': None}, 
				'col9': {'hasModifier': False, 'modifier': None},
		}, 

		'row4': {'col1': {'hasModifier': False, 'modifier': None}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': 'row-4'}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': True, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': None}, 
				'col9': {'hasModifier': False, 'modifier': None},
		}, 

		'row5': {'col1': {'hasModifier': False, 'modifier': None}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': 'row-5'}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': None}, 
				'col9': {'hasModifier': False, 'modifier': None},
		}, 

		'row6': {'col1': {'hasModifier': False, 'modifier': 'row-6'}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': None}, 
				'col9': {'hasModifier': False, 'modifier': None},
		}, 

		'row7': {'col1': {'hasModifier': False, 'modifier': None}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': None}, 
				'col9': {'hasModifier': False, 'modifier': 'row-7'},
		}, 

		'row8': {'col1': {'hasModifier': False, 'modifier': None}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': None}, 
				'col9': {'hasModifier': False, 'modifier': 'row-8'},
		}, 

		'row9': {'col1': {'hasModifier': False, 'modifier': 'row-9'}, 
				'col2': {'hasModifier': False, 'modifier': None}, 
				'col3': {'hasModifier': False, 'modifier': None}, 
				'col4': {'hasModifier': False, 'modifier': None}, 
				'col5': {'hasModifier': False, 'modifier': None}, 
				'col6': {'hasModifier': False, 'modifier': None}, 
				'col7': {'hasModifier': False, 'modifier': None}, 
				'col8': {'hasModifier': False, 'modifier': None}, 
				'col9': {'hasModifier': False, 'modifier': None},
		}
}

## While running simulations, rows_properties should be reset after each
## move evaluation.
def reset_rows_properties():
	for n in range(9):
		for p in range(9):
			rows_properties[index_to_row[n]][index_to_col[p]]['hasModifier'] = False
			rows_properties[index_to_row[n]][index_to_col[p]]['modifier'] = None

## Columns are automatically enumerated by the list indexes;
## Column 1 contains the elements of the index 0 of all rows;
## Column 2 contains the elements of the index 1 of all rows;
## Column 3 contains the elements of the index 2 of all rows
## and so on.

## The initial board is just a reference for future duplications. Any simulation
## must be run on duplicates of the original board so that it is not affected and
## to be able to reset simulated boards with same variable names in loops and/or
## iterations.

board = [list(row1), list(row2), list(row3), list(row4), list(row5), list(row6),
		 list(row7), list(row8), list(row9)
]

## Conversion table for string and index values.
index_to_row = {
	0: 'row1', 
	1: 'row2', 
	2: 'row3', 
	3: 'row4', 
	4: 'row5', 
	5: 'row6', 
	6: 'row7', 
	7: 'row8', 
	8: 'row9'
}

index_to_col = {
	0: 'col1', 
	1: 'col2', 
	2: 'col3', 
	3: 'col4', 
	4: 'col5', 
	5: 'col6', 
	6: 'col7', 
	7: 'col8', 
	8: 'col9'
}

## If a move can make multiple matches, only one will be made - the one with the highest priority value.
match_priority_values = {'vertical_3_match_1x1': 1,
						 'vertical_3_match_21x': 1,
						 'vertical_3_match_x12': 1,
						 'horizontal_3_match_1x1': 1,
						 'horizontal_3_match_21x': 1,
						 'horizontal_3_match_x12': 1,

						 'l_shape_xleft12xtop12': 2, 
						 'l_shape_xright12xtop12': 2, 
						 'l_shape_xleft12xbottom12': 2, 
						 'l_shape_xright12xbottom12': 2, 

						 'vertical_4_match_21x1': 2, 
						 'vertical_4_match_1x12': 2, 
						 'horizontal_4_match_21x1': 2, 
						 'horizontal_4_match_1x12': 2, 

						 'vertical_5_match_21x12': 3, 
						 'horizontal_5_match_21x12': 3, 

						 't_shape_7_left12xbottom12xright12': 4, 
						 't_shape_7_left12xtop12xbottom12': 4, 
						 't_shape_7_left12xtop12xright12': 4, 
						 't_shape_7_top12xright12xbottom12': 4, 

						 't_shape_6_left12xbottom12xright1': 3, 
						 't_shape_6_left12xtop12xbottom1': 3, 
						 't_shape_6_left1xtop12xright12': 3, 
						 't_shape_6_top1xright12xbottom12': 3, 

						 't_shape_6_left1xbottom12xright12': 3,
						 't_shape_6_left12xtop1xbottom12' : 3,
						 't_shape_6_left12xtop12xright1': 3,
						 't_shape_6_top12xright12xbottom1': 3,

						 't_shape_5_left1xright1xbottom12': 2, 
						 't_shape_5_left12xtop1xbottom1': 2, 
						 't_shape_5_left1xtop12xright1': 2, 
						 't_shape_5_top1xright12xbottom1': 2
}

match_boosters = {'l_shape_xleft12xtop12': 'area_booster', 
				 'l_shape_xright12xtop12': 'area_booster', 
				 'l_shape_xleft12xbottom12': 'area_booster', 
				 'l_shape_xright12xbottom12': 'area_booster', 

				 'vertical_4_match_21x1': 'vertical_booster', 
				 'vertical_4_match_1x12': 'vertical_booster', 
				 'horizontal_4_match_21x1': 'horizontal_booster', 
				 'horizontal_4_match_1x12': 'horizontal_booster', 

				 'vertical_5_match_21x12': 'star_booster', 
				 'horizontal_5_match_21x12': 'star_booster', 

				 't_shape_7_left12xbottom12xright12': 'area_booster', 
				 't_shape_7_left12xtop12xbottom12': 'area_booster', 
				 't_shape_7_left12xtop12xright12': 'area_booster', 
				 't_shape_7_top12xright12xbottom12': 'area_booster', 

				 't_shape_6_left12xbottom12xright1': 'area_booster', 
				 't_shape_6_left12xtop12xbottom1': 'area_booster', 
				 't_shape_6_left1xtop12xright12': 'area_booster', 
				 't_shape_6_top1xright12xbottom12': 'area_booster', 

				 't_shape_6_left1xbottom12xright12': 'area_booster',
				 't_shape_6_left12xtop1xbottom12' : 'area_booster',
				 't_shape_6_left12xtop12xright1': 'area_booster',
				 't_shape_6_top12xright12xbottom1': 'area_booster',

				 't_shape_5_left1xright1xbottom12': 'area_booster', 
				 't_shape_5_left12xtop1xbottom1': 'area_booster', 
				 't_shape_5_left1xtop12xright1': 'area_booster', 
				 't_shape_5_top1xright12xbottom1': 'area_booster'
}

match_clear_directions = {
						'vertical_3_match_1x1': {
												'up': 1,
												'down': 1,
												'left': 0,
												'right': 0
						},
						'vertical_3_match_21x': {
												'up': 2,
												'down': 0,
												'left': 0,
												'right': 0
						},
						'vertical_3_match_x12': {
												'up': 0,
												'down': 2,
												'left': 0,
												'right': 0
						},
						'horizontal_3_match_1x1': {
												'up': 0,
												'down': 0,
												'left': 1,
												'right': 1
						},
						'horizontal_3_match_21x': {
												'up': 0,
												'down': 0,
												'left': 2,
												'right': 0
						},
						'horizontal_3_match_x12': {
												'up': 0,
												'down': 0,
												'left': 0,
												'right': 2
						},

						'l_shape_xleft12xtop12': {
												'up': 2,
												'down': 0,
												'left': 2,
												'right': 0
						},
						'l_shape_xright12xtop12': {
												'up': 2,
												'down': 0,
												'left': 0,
												'right': 2
						}, 
						'l_shape_xleft12xbottom12': {
												'up': 0,
												'down': 2,
												'left': 2,
												'right': 0
						}, 
						'l_shape_xright12xbottom12': {
												'up': 0,
												'down': 2,
												'left': 0,
												'right': 2
						}, 

						'vertical_4_match_21x1': {
												'up': 2,
												'down': 1,
												'left': 0,
												'right': 0
						}, 
						'vertical_4_match_1x12': {
												'up': 1,
												'down': 2,
												'left': 0,
												'right': 0
						},
						'horizontal_4_match_21x1': {
												'up': 0,
												'down': 0,
												'left': 2,
												'right': 1
						}, 
						'horizontal_4_match_1x12': {
												'up': 0,
												'down': 0,
												'left': 1,
												'right': 2
						},

						'vertical_5_match_21x12': {
												'up': 2,
												'down': 2,
												'left': 0,
												'right': 0
						}, 
						'horizontal_5_match_21x12': {
												'up': 0,
												'down': 0,
												'left': 2,
												'right': 2
						}, 

						't_shape_7_left12xbottom12xright12': {
												'up': 0,
												'down': 2,
												'left': 2,
												'right': 2
						}, 
						't_shape_7_left12xtop12xbottom12': {
												'up': 2,
												'down': 2,
												'left': 2,
												'right': 0
						}, 
						't_shape_7_left12xtop12xright12': {
												'up': 2,
												'down': 0,
												'left': 2,
												'right': 2
						}, 
						't_shape_7_top12xright12xbottom12': {
												'up': 2,
												'down': 2,
												'left': 0,
												'right': 2
						},

						't_shape_6_left12xbottom12xright1': {
												'up': 0,
												'down': 2,
												'left': 2,
												'right': 1
						},
						't_shape_6_left12xtop12xbottom1': {
												'up': 2,
												'down': 1,
												'left': 2,
												'right': 0
						}, 
						't_shape_6_left1xtop12xright12': {
												'up': 2,
												'down': 0,
												'left': 1,
												'right': 2
						},
						't_shape_6_top1xright12xbottom12': {
												'up': 1,
												'down': 2,
												'left': 0,
												'right': 2
						}, 

						't_shape_6_left1xbottom12xright12': {
												'up': 0,
												'down': 2,
												'left': 1,
												'right': 2
						},
						't_shape_6_left12xtop1xbottom12' : {
												'up': 1,
												'down': 2,
												'left': 2,
												'right': 0
						},
						't_shape_6_left12xtop12xright1': {
												'up': 2,
												'down': 0,
												'left': 2,
												'right': 1
						},
						't_shape_6_top12xright12xbottom1': {
												'up': 2,
												'down': 1,
												'left': 0,
												'right': 2
						},

						't_shape_5_left1xright1xbottom12': {
												'up': 0,
												'down': 2,
												'left': 1,
												'right': 1
						}, 
						't_shape_5_left12xtop1xbottom1': {
												'up': 1,
												'down': 1,
												'left': 2,
												'right': 0
						}, 
						't_shape_5_left1xtop12xright1': {
												'up': 2,
												'down': 0,
												'left': 1,
												'right': 1
						}, 
						't_shape_5_top1xright12xbottom1': {
												'up': 1,
												'down': 1,
												'left': 0,
												'right': 2
						}
}

def doesMatchCreatesBooster(match):
	if match not in match_boosters:
		return False
	else:
		return match_boosters[match]

def adjacentFruits(row, col, test_board):
	leftFruits = []
	rightFruits = []
	topFruits = []
	bottomFruits = []

	## The conditionals checks for edges and extremities of the board
	## in which you can't get fruits to the left/right/top/bottom (depending
	## on what edge or extremity you are).
	## If the col number is 0, then it's impossible to even get the first fruit to the
	## the left, so it breaks, no point in even trying to get the 2nd or 
	## 3rd fruit to the left. If the col is 2 (> 1), then it means there are 2 fruits to
	## the left that we can get, and so on to the right fruit, top fruit and 
	## bottom fruit verifications.

	## left fruits
	if col > 0:
		leftFruit3 = test_board[row][col - 1]
		leftFruits.append(leftFruit3)

	if col > 1:
		leftFruit2 = test_board[row][col - 2]
		leftFruits.append(leftFruit2)

	if col > 2:
		leftFruit1 = test_board[row][col - 3]
		leftFruits.append(leftFruit1)

	## right fruits
	if col < 8:
		rightFruit1 = test_board[row][col + 1]
		rightFruits.append(rightFruit1)

	if col < 7:
		rightFruit2 = test_board[row][col + 2]
		rightFruits.append(rightFruit2)

	if col < 6:
		rightFruit3 = test_board[row][col + 3]
		rightFruits.append(rightFruit3)

	## top fruits
	if row > 0:
		topFruit3 = test_board[row - 1][col]
		topFruits.append(topFruit3)

	if row > 1:
		topFruit2 = test_board[row - 2][col]
		topFruits.append(topFruit2)

	if row > 2:
		topFruit1 = test_board[row - 3][col]
		topFruits.append(topFruit1)

	## bottom fruits
	if row < 8:
		bottomFruit1 = test_board[row + 1][col]
		bottomFruits.append(bottomFruit1)

	if row < 7:
		bottomFruit2 = test_board[row + 2][col]
		bottomFruits.append(bottomFruit2)

	if row < 6:
		bottomFruit3 = test_board[row + 3][col]
		bottomFruits.append(bottomFruit3)

	adjacentFruits = {'leftFruits': leftFruits,
					  'rightFruits': rightFruits,
					  'topFruits': topFruits,
					  'bottomFruits': bottomFruits
	}
	return adjacentFruits

## The following functions simply replace the fruit above (row -1) or fruit to the left
## (col - 1) and vice-versa in the simulated board.
def moveUp(row, col):
	simulated_board = [list(row1), list(row2), list(row3), list(row4), list(row5), 
					   list(row6), list(row7), list(row8), list(row9)
	]
	if row > 0:
		current_fruit = simulated_board[row][col]
		fruit_above = simulated_board[row - 1][col]
		simulated_board[row - 1][col] = current_fruit
		simulated_board[row][col] = fruit_above
		return {'canMove': True, 'output_board': simulated_board}
	else:
		# no fruit above the first row
		return {'canMove': False}

def moveDown(row, col):
	simulated_board = [list(row1), list(row2), list(row3), list(row4), list(row5), 
					   list(row6), list(row7), list(row8), list(row9)
	]
	if row < 8:
		current_fruit = simulated_board[row][col]
		fruit_below = simulated_board[row + 1][col]
		simulated_board[row + 1][col] = current_fruit
		simulated_board[row][col] = fruit_below
		return {'canMove': True, 'output_board': simulated_board}
	else:
		# no fruit below the last row
		return {'canMove': False}

def moveLeft(row, col):
	simulated_board = [list(row1), list(row2), list(row3), list(row4), list(row5), 
					   list(row6), list(row7), list(row8), list(row9)
	]
	if col > 0:
		current_fruit = simulated_board[row][col]
		fruit_to_the_left = simulated_board[row][col - 1]
		simulated_board[row][col - 1] = current_fruit
		simulated_board[row][col] = fruit_to_the_left
		return {'canMove': True, 'output_board': simulated_board}
	else:
		# no fruit to the left in the first column
		return {'canMove': False}

def moveRight(row, col):
	simulated_board = [list(row1), list(row2), list(row3), list(row4), list(row5), 
					   list(row6), list(row7), list(row8), list(row9)
	]
	if col < 8:
		current_fruit = simulated_board[row][col]
		fruit_to_the_right = simulated_board[row][col + 1]
		simulated_board[row][col + 1] = current_fruit
		simulated_board[row][col] = fruit_to_the_right
		return {'canMove': True, 'output_board': simulated_board}
	else:
		# no fruit to the right in the last column
		return {'canMove': False}

## Simulates a move in a direction and checks if there are matches.
def ValidMoves(row, col, test_board):
	minimum_match_count = 3
	validMoves = []
	current_fruit = test_board[row][col]

	## These conditionals checks if the fruit can be moved in the specified direction.

	## Move up conditional check.
	move_up_call = moveUp(row, col)
	if move_up_call['canMove'] == True:
		## Star Booster can match any color and will trigger a match whenever it's
		## swapped, independent of the amount or color of adjacent tiles.
		if rows_properties[index_to_row[row]][index_to_col[col]]['modifier'] == 'star_booster':
			validMoves.append('up')

		test_board = move_up_call['output_board']
		up_adjacentFruits = adjacentFruits(row - 1, col, test_board)

		## Verifies the adjacent fruits for matches when moving in a direction.
		if 'up' not in validMoves:

			## The [::-1] reverses the list, so that we can get the adjacent fruits in order
			## just like in the border, col - 1 will be the fruit immediately to the left
			## col - 2 will be to the left of col -1 (using the board positions as reference)
			horizontal_check = list(fruit for fruit in up_adjacentFruits['leftFruits'][::-1]) + \
							   list(current_fruit) + \
							   list(fruit for fruit in up_adjacentFruits['rightFruits'])
			c = 0
			for fruit in horizontal_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('up')
						break
				else:
					c = 0

		## This conditional is in case there are matches in both horizontal and vertical
		## positions. Like the "L-shape" or "T-shape" match, which would add 2 'up's to
		## validMoves, because moving up would make both a vertical and a horizontal match.
		if 'up' not in validMoves:
			vertical_check = list(fruit for fruit in up_adjacentFruits['topFruits'][::-1]) + \
							 list(current_fruit) + \
							 list(fruit for fruit in up_adjacentFruits['bottomFruits'])
			c = 0
			for fruit in vertical_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('up')
						break
				else:
					c = 0

	## Move down conditional check.
	move_down_call = moveDown(row, col)
	if move_down_call['canMove'] == True:

		## Star Booster can match any color and will trigger a match whenever it's
		## swapped, independent of the amount or color of adjacent tiles.
		if rows_properties[index_to_row[row]][index_to_col[col]]['modifier'] == 'star_booster':
			validMoves.append('down')

		test_board = move_down_call['output_board']
		down_adjacentFruits = adjacentFruits(row + 1, col, test_board)

		## Verifies the adjacent fruits for matches when moving in a direction.
		if 'down' not in validMoves:
			horizontal_check = list(fruit for fruit in down_adjacentFruits['leftFruits'][::-1]) + \
							   list(current_fruit) + \
							   list(fruit for fruit in down_adjacentFruits['rightFruits'])
			c = 0
			for fruit in horizontal_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('down')
						break
				else:
					c = 0

		## This conditional is in case there are matches in both horizontal and vertical
		## positions. Like the "L-shape" or "T-shape" match, which would add 2 'up's to
		## validMoves, because moving up would make both a vertical and a horizontal match.
		if 'down' not in validMoves:
			vertical_check = list(fruit for fruit in down_adjacentFruits['topFruits'][::-1]) + \
							 list(current_fruit) + \
							 list(fruit for fruit in down_adjacentFruits['bottomFruits'])
			c = 0
			for fruit in vertical_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('down')
						break
				else:
					c = 0

	## Move left conditional check.
	move_left_call = moveLeft(row, col)
	if move_left_call['canMove'] == True:

		## Star Booster can match any color and will trigger a match whenever it's
		## swapped, independent of the amount or color of adjacent tiles.
		if rows_properties[index_to_row[row]][index_to_col[col]]['modifier'] == 'star_booster':
			validMoves.append('left')

		test_board = move_left_call['output_board']
		left_adjacentFruits = adjacentFruits(row, col - 1, test_board)

		## Verifies the adjacent fruits for matches when moving in a direction.
		if 'left' not in validMoves:
			horizontal_check = list(fruit for fruit in left_adjacentFruits['leftFruits'][::-1]) + \
							   list(current_fruit) + \
							   list(fruit for fruit in left_adjacentFruits['rightFruits'])
			c = 0
			for fruit in horizontal_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('left')
						break
				else:
					c = 0

		## This conditional is in case there are matches in both horizontal and vertical
		## positions. Like the "L-shape" or "T-shape" match, which would add 2 'up's to
		## validMoves, because moving up would make both a vertical and a horizontal match.
		if 'left' not in validMoves:
			vertical_check = list(fruit for fruit in left_adjacentFruits['topFruits'][::-1]) + \
							 list(current_fruit) + \
							 list(fruit for fruit in left_adjacentFruits['bottomFruits'])
			c = 0
			for fruit in vertical_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('left')
						break
				else:
					c = 0

	## Move right conditional check.
	move_right_call = moveRight(row, col)
	if move_right_call['canMove'] == True:

		## Star Booster can match any color and will trigger a match whenever it's
		## swapped, independent of the amount or color of adjacent tiles.
		if rows_properties[index_to_row[row]][index_to_col[col]]['modifier'] == 'star_booster':
			validMoves.append('right')

		test_board = move_right_call['output_board']
		right_adjacentFruits = adjacentFruits(row, col + 1, test_board)

		## Verifies the adjacent fruits for matches when moving in a direction.
		if 'right' not in validMoves:
			horizontal_check = list(fruit for fruit in right_adjacentFruits['leftFruits'][::-1]) + \
							   list(current_fruit) + \
							   list(fruit for fruit in right_adjacentFruits['rightFruits'])
			c = 0
			for fruit in horizontal_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('right')
						break
				else:
					c = 0

		## This conditional is in case there are matches in both horizontal and vertical
		## positions. Like the "L-shape" or "T-shape" match, which would add 2 'up's to
		## validMoves, because moving up would make both a vertical and a horizontal match.
		if 'right' not in validMoves:
			vertical_check = list(fruit for fruit in right_adjacentFruits['topFruits'][::-1]) + \
							 list(current_fruit) + \
							 list(fruit for fruit in right_adjacentFruits['bottomFruits'])
			c = 0
			for fruit in vertical_check:
				if fruit == current_fruit:
					c += 1
					if c >= minimum_match_count:
						validMoves.append('right')
						break
				else:
					c = 0

	if len(validMoves) == 0:
		return {'isValid': False}
	elif len(validMoves) > 0:
		return {'isValid': True, 'validMoves': validMoves}

## Each of the match functions below check the board for a specific match and returns the matches or False in
## case of none found.
## The "1x1", "x11", etc. Means: 1 is the adjacent fruits and x
## is the current fruit and it moved to that tile. This is useful
## to know exactly how the match-3 is made and know exactly what
## columns and rows will be affected by the 3-match.
## 1 means -1 col or -1 row; 2 means -2 col or -2 row.

def match_3(row, col, current_fruit, simul_board, adjacent_fruits):
	match_3_matches = []

	## Vertical

	## len() conditional checks if there are adjacent fruits in the
	## specified direction.
	if len(adjacent_fruits['bottomFruits']) > 0 and len(adjacent_fruits['topFruits']) > 0:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit:
			match_3_matches.append('vertical_3_match_1x1')

	if len(adjacent_fruits['topFruits']) > 1:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit:
			match_3_matches.append('vertical_3_match_21x')

	if len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			match_3_matches.append('vertical_3_match_x12')

	## Horizontal
	if len(adjacent_fruits['leftFruits']) > 0 and len(adjacent_fruits['rightFruits']) > 0:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit:
			match_3_matches.append('horizontal_3_match_1x1')

	if len(adjacent_fruits['leftFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit:
			match_3_matches.append('horizontal_3_match_21x')

	if len(adjacent_fruits['rightFruits']) > 1:
		if adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit:
			match_3_matches.append('horizontal_3_match_x12')

	## I know this is redundant, since the program wouldn't get here if there
	## wasn't a valid move, which has to be a 3-match at minimum, which means
	## match_3_matches will always have a len() > 0, but I wrote this anyway
	## for consistency with the rest of the code (code pattern).
	if len(match_3_matches) > 0:
		return match_3_matches
	else:
		return False

def match_l_shape(row, col, current_fruit, simul_board, adjacent_fruits):
	l_shape_matches = []

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['topFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit:
			l_shape_matches.append('l_shape_xleft12xtop12')

	if len(adjacent_fruits['rightFruits']) > 1 and len(adjacent_fruits['topFruits']) > 1:
		if adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit:
			l_shape_matches.append('l_shape_xright12xtop12')

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			l_shape_matches.append('l_shape_xleft12xbottom12')

	if len(adjacent_fruits['rightFruits']) > 1 and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			l_shape_matches.append('l_shape_xright12xbottom12')

	if len(l_shape_matches) > 0:
		return l_shape_matches
	else:
		return False

def match_4(row, col, current_fruit, simul_board, adjacent_fruits):
	match_4_matches = []

	## Vertical
	if len(adjacent_fruits['topFruits']) > 1 and len(adjacent_fruits['bottomFruits']) > 0:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit:
			match_4_matches.append('vertical_4_match_21x1')

	if len(adjacent_fruits['topFruits']) > 0 and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			match_4_matches.append('vertical_4_match_1x12')

	## Horizontal
	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['rightFruits']) > 0:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit:
			match_4_matches.append('horizontal_4_match_21x1')

	if len(adjacent_fruits['leftFruits']) > 0 and len(adjacent_fruits['rightFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit:
			match_4_matches.append('horizontal_4_match_1x12')

	if len(match_4_matches) > 0:
		return match_4_matches
	else:
		return False

def match_5(row, col, current_fruit, simul_board, adjacent_fruits):
	match_5_matches = []

	## Vertical
	if len(adjacent_fruits['topFruits']) > 1 and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			match_5_matches.append('vertical_5_match_21x12')

	## Horizontal
	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['rightFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit:
			match_5_matches.append('horizontal_5_match_21x12')

	if len(match_5_matches) > 0:
		return match_5_matches
	else:
		return False

def match_t_shape(row, col, current_fruit, simul_board, adjacent_fruits):
	t_shape_matches = []

	## Here the x in for example "xleft12xbottom12xright12", means: relative to x, go
	## left 1 time and then 2 times; relative to x, go bottom 1 time and then
	## 2 times; relative to x, go right 1 time and then 2 times. Same applies for others.

	## "T-shape match with 7 fruits.
	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['bottomFruits']) > 1 \
	and len(adjacent_fruits['rightFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_7_left12xbottom12xright12')

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['topFruits']) > 1 \
	and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_7_left12xtop12xbottom12')

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['topFruits']) > 1 \
	and len(adjacent_fruits['rightFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_7_left12xtop12xright12')

	if len(adjacent_fruits['topFruits']) > 1 and len(adjacent_fruits['rightFruits']) > 1 \
	and	len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_7_top12xright12xbottom12')

	## A 7 fruits t-shape match is worth more than a 6 and 5 fruits t-shape match, so
	## we can end the function here if any 7 fruits t-shape match was found.
	if len(t_shape_matches) > 0:
		return t_shape_matches

	## "T-shape match with 6 fruits.

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['bottomFruits']) > 1 \
	and len(adjacent_fruits['rightFruits']) > 0:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit:
			t_shape_matches.append('t_shape_6_left12xbottom12xright1')

	if len(adjacent_fruits['leftFruits']) > 0 and len(adjacent_fruits['bottomFruits']) > 1 \
	and len(adjacent_fruits['rightFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_6_left1xbottom12xright12')	

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['topFruits']) > 1 \
	and len(adjacent_fruits['bottomFruits']) > 0:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit:
			t_shape_matches.append('t_shape_6_left12xtop12xbottom1')

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['topFruits']) > 0 \
	and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_6_left12xtop1xbottom12')

	if len(adjacent_fruits['leftFruits']) > 0 and len(adjacent_fruits['topFruits']) > 1 \
	and len(adjacent_fruits['rightFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_6_left1xtop12xright12')

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['topFruits']) > 1 \
	and len(adjacent_fruits['rightFruits']) > 0:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit:
			t_shape_matches.append('t_shape_6_left12xtop12xright1')			

	if len(adjacent_fruits['topFruits']) > 0 and len(adjacent_fruits['rightFruits']) > 1 \
	and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_6_top1xright12xbottom12')

	if len(adjacent_fruits['topFruits']) > 1 and len(adjacent_fruits['rightFruits']) > 1 \
	and len(adjacent_fruits['bottomFruits']) > 0:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit:
			t_shape_matches.append('t_shape_6_top12xright12xbottom1')

	## Same logic - a 6 fruits t-shape match is worth more than a 
	## 5 fruits t-shape match, so we can end the function here if 
	## any 6 fruits t-shape match was found.
	if len(t_shape_matches) > 0:
		return t_shape_matches

	## "T-shape match with 5 fruits.

	if len(adjacent_fruits['leftFruits']) > 0 and len(adjacent_fruits['rightFruits']) > 0 \
	and len(adjacent_fruits['bottomFruits']) > 1:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][1] == current_fruit:
			t_shape_matches.append('t_shape_5_left1xright1xbottom12')

	if len(adjacent_fruits['leftFruits']) > 1 and len(adjacent_fruits['topFruits']) > 0 \
	and len(adjacent_fruits['bottomFruits']) > 0:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['leftFruits'][1] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit:
			t_shape_matches.append('t_shape_5_left12xtop1xbottom1')

	if len(adjacent_fruits['leftFruits']) > 0 and len(adjacent_fruits['topFruits']) > 1 \
	and len(adjacent_fruits['rightFruits']) > 0:
		if adjacent_fruits['leftFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['topFruits'][1] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit:
			t_shape_matches.append('t_shape_5_left1xtop12xright1')

	if len(adjacent_fruits['topFruits']) > 0 and len(adjacent_fruits['rightFruits']) > 1 \
	and len(adjacent_fruits['bottomFruits']) > 0:
		if adjacent_fruits['topFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][0] == current_fruit and \
		adjacent_fruits['rightFruits'][1] == current_fruit and \
		adjacent_fruits['bottomFruits'][0] == current_fruit:
			t_shape_matches.append('t_shape_5_top1xright12xbottom1')

	if len(t_shape_matches) > 0:
		return t_shape_matches
	else:
		return False

## Will check all matches that this move makes relative to the fruit that was moved
## and then it will consider the match with the highest priority value and use that
## match to simulate the board after the match was done to make further calculations
## todo: evaluate the value of each match and return the highest value match (same
## priority system used by the game)
## For example, if a match-3 is possible and a match-5 is possible,
## it means there is 5 fruits in a row, and the 5-match will take precedence
## over match-3 and match-4.
## The priority goes like this: match-3 < match-4 < match-5 < l-shape < t-shape.
def matches_check(row, col, input_board):
	matches = []
	simul_board = []
	priority_match = None
	for fruit_row in input_board:
		simul_board.append(list(fruit_row))
	current_fruit = simul_board[row][col]
	adjacent_fruits = adjacentFruits(row, col, simul_board)
	#print(adjacent_fruits)
	## check for 3-match
	match_3_check = match_3(row, col, current_fruit, simul_board, adjacent_fruits)
	if match_3_check != False:
		matches.extend(match_3_check)

	## check for 4-match
	match_4_check = match_4(row, col, current_fruit, simul_board, adjacent_fruits)
	if match_4_check != False:
		matches.extend(match_4_check)

	## check for l-shape match
	match_l_shape_check = match_l_shape(row, col, current_fruit, simul_board, adjacent_fruits)
	if match_l_shape_check != False:
		matches.extend(match_l_shape_check)
		
	## check for 5-match
	match_5_check = match_5(row, col, current_fruit, simul_board, adjacent_fruits)
	if match_5_check != False:
		matches.extend(match_5_check)	

	## check for t-shape match (5, 6 and 7 fruits)
	match_t_shape_check = match_t_shape(row, col, current_fruit, simul_board, adjacent_fruits)
	if match_t_shape_check != False:
		matches.extend(match_t_shape_check)	

	## This will compute the highest priority match using priority points (match_priority_values)
	highest_value = 0
	for match in matches:
		match_value = match_priority_values[match]
		if match_value > highest_value:
			priority_match = match
			highest_value = match_value



	#print('\n')
	#print("Matches:")
	#print(matches)
	#print("Priority Match:")
	#print(priority_match)
	#print('\n')
	return {'priority_match': priority_match, \
			'booster': doesMatchCreatesBooster(priority_match)
	}

## Counts the amount of fruits above a coordinate (row, col).
def fruits_above_count(row, col, board_state):
	fruits_above = 0
	c = 0
	while True:
		c += 1
		if row - c >= 0:
			fruit = board_state[row - c][col:col+1]
			if len(fruit) > 0:
				fruits_above += 1
		else:
			return fruits_above
			break

def vertical_booster_clear(row, col, board_state, empty_character):
	for fruit_row in board_state:
		board_state[fruit_row][col] = empty_character
	return board_state

def horizontal_booster_clear(row, col, board_state):
	for fruit_col in board_state[row]:
		board_state[row][fruit_col] = empty_character
	return board_state

def area_booster_clear(row, col, board_state):
	# left
	board_state[row][col - 1] = empty_character

	# right
	board_state[row][col + 1] = empty_character

	# up
	board_state[row - 1][col] = empty_character

	# down
	board_state[row + 1][col] = empty_character

	# left_up
	board_state[row - 1][col - 1] = empty_character

	# left_down
	board_state[row + 1][col - 1] = empty_character

	# right_up
	board_state[row - 1][col + 1] = empty_character

	# right_down
	board_state[row + 1][col + 1] = empty_character

	return board_state

def star_booster_clear(row, col, board_state):
	fruit_color_letter = board_state[row][col]
	for fruit_row in board_state:
		for fruit_col in board_state:
			fruit_being_analyzed = board_state[fruit_row][fruit_col]
			if fruit_being_analyzed == fruit_color_letter:
				board_state[fruit_row][fruit_col] = empty_character
	return board_stat

## Removes the fruits cleared in the match; pulls down the fruits above and replace the previos position of
## the fruits above with 'X's.
def pull_fruits_above_down(row, col, board_state, fruits_above, total_rows_to_move, match_booster, match_fruits_count):
	
	# If the match creates a booster, it means the central fruit won't disappear - it will turn into
	# a booster, and so the amount of fruits that disappear in the vertical reduces by 1, thus reducing
	# the amount of rows the fruits above will move down.
	#print("current row on pull_fruits_above_down: " + str(row))

	if match_booster != False:
		total_rows_to_move -= 1

		#print('\n')
		#print("Rows Properties (" + index_to_row[row] + ") on pull_fruits_above_down:")
		#print(rows_properties[index_to_row[row]])
		#print('\n')

		# This is so that when the fruits go down, they don't replace the
		# booster fruit that was just created.
		row -= 1

	for fruit_above in range(fruits_above):
		fruit_above += total_rows_to_move
		board_state[row - (fruit_above - total_rows_to_move)][col] = board_state[row - fruit_above][col]

	# Replace the space left by the fruits that moved down by 'X', which means
	# random, unpredictable fruit. Number of 'X' in the specific vertical line = total_rows_to_move
	for num in range(total_rows_to_move):
		board_state[num][col] = 'X'

	return board_state

## This will replace the fruits that disappear with the match by a character
## to represent Empty. For example: '/'.
def execute_match_clear(row, col, board_state, match_booster, match_fruits_count):
	empty_character = '/'

	## If the match does not create a booster, replace the current fruit
	## with an empty character.
	row_property = rows_properties[index_to_row[row]][index_to_col[col]]
	if row_property['hasModifier'] == False:
		board_state[row][col] == empty_character

	up_direction_fruits_count = match_fruits_count['up']
	if up_direction_fruits_count > 0:
		for n in range(up_direction_fruits_count):
			n += 1

			## This is in case the match makes a booster explode.
			row_property = rows_properties[index_to_row[row - n]][index_to_col[col]]
			if row_property['hasModifier'] == True:
				modifier = row_property['modifier']
				if modifier == 'vertical_booster':
					board_state = vertical_booster_clear(row - n, col, board_state, empty_character)
				if modifier == 'horizontal_booster':
					board_state = horizontal_booster_clear(row - n, col, board_state, empty_character)
				if modifier == 'area_booster':
					board_state = area_booster_clear(row - n, col, board_state, empty_character)
				if modifier == 'star_booster':
					board_state = star_booster_clear(row - n, col, board_state, empty_character)

				## Since the booster on this position exploded, we update rows_properties to
				## reflect that.
				rows_properties[index_to_row[row - n]][index_to_col][col]['hasModifier'] = False
				rows_properties[index_to_row[row - n]][index_to_col][col]['modifier'] = None

			print("The row inside execute_match_clear() for 'up' direction is: " + str(row))
			board_state[row - n][col] = empty_character

	down_direction_fruits_count = match_fruits_count['down']
	if down_direction_fruits_count > 0:		
		for n in range(down_direction_fruits_count):
			n += 1

			## This is in case the match makes a booster explode.
			row_property = rows_properties[index_to_row[row + n]][index_to_col[col]]
			if row_property['hasModifier'] == True:
				modifier = row_property['modifier']
				if modifier == 'vertical_booster':
					board_state = vertical_booster_clear(row + n, col, board_state, empty_character)
				if modifier == 'horizontal_booster':
					board_state = horizontal_booster_clear(row + n, col, board_state, empty_character)
				if modifier == 'area_booster':
					board_state = area_booster_clear(row + n, col, board_state, empty_character)
				if modifier == 'star_booster':
					board_state = star_booster_clear(row + n, col, board_state, empty_character)
														
				## Since the booster on this position exploded, we update rows_properties to
				## reflect that.
				rows_properties[index_to_row[row + n]][index_to_col][col]['hasModifier'] = False
				rows_properties[index_to_row[row + n]][index_to_col][col]['modifier'] = None															

			print("The row inside execute_match_clear() for 'down' direction is: " + str(row))
			board_state[row + n][col] = empty_character

	left_direction_fruits_count = match_fruits_count['left']
	if left_direction_fruits_count > 0:
		for n in range(left_direction_fruits_count):
			n += 1

			## This is in case the match makes a booster explode.
			row_property = rows_properties[index_to_row[row]][index_to_col[col - 1]]
			if row_property['hasModifier'] == True:
				modifier = row_property['modifier']
				if modifier == 'vertical_booster':
					board_state = vertical_booster_clear(row, col - 1, board_state, empty_character)
				if modifier == 'horizontal_booster':
					board_state = horizontal_booster_clear(row, col - 1, board_state, empty_character)
				if modifier == 'area_booster':
					board_state = area_booster_clear(row, col - 1, board_state, empty_character)
				if modifier == 'star_booster':
					board_state = star_booster_clear(row, col - 1, board_state, empty_character)																	

				## Since the booster on this position exploded, we update rows_properties to
				## reflect that.
				rows_properties[index_to_row[row]][index_to_col][col - n]['hasModifier'] = False
				rows_properties[index_to_row[row]][index_to_col][col - n]['modifier'] = None
			
			board_state[row][col - n] = empty_character

	right_direction_fruits_count = match_fruits_count['right']
	if right_direction_fruits_count > 0:
		for n in range(right_direction_fruits_count):
			n += 1

			## This is in case the match makes a booster explode.
			row_property = rows_properties[index_to_row[row]][index_to_col[col + 1]]
			if row_property['hasModifier'] == True:
				modifier = row_property['modifier']
				if modifier == 'vertical_booster':
					board_state = vertical_booster_clear(row, col + 1, board_state, empty_character)
				if modifier == 'horizontal_booster':
					board_state = horizontal_booster_clear(row, col + 1, board_state, empty_character)
				if modifier == 'area_booster':
					board_state = area_booster_clear(row, col + 1, board_state, empty_character)
				if modifier == 'star_booster':
					board_state = star_booster_clear(row, col + 1, board_state, empty_character)										

				## Since the booster on this position exploded, we update rows_properties to
				## reflect that.
				rows_properties[index_to_row[row]][index_to_col][col + n]['hasModifier'] = False
				rows_properties[index_to_row[row]][index_to_col][col + n]['modifier'] = None

			board_state[row][col + n] = empty_character

	print('\n')
	print("Board after it was replaced with '/'s.")
	for superl in board_state:
		print(superl)
	print('\n')
	return board_state

# This makes a dictionary (col_fruits) in which the keys are cols and the values are
# also keys (rows) and the values are the fruits located in that position. It's kinda
# like an inversed board. I honestly don't know if this will be used, but my intuition
# says it could be useful when looking for empty characters since we would be traversing
# column by column and not row by row (because new fruits fall in the verticals)
#col_fruits = {}
#for e in range(9):
#	col_fruits[index_to_col[e]] = {}
#	for u in range(9):
#		col_fruits[index_to_col[e]][index_to_row[u]] = board[u][e]

def generate_board_state_after_match(row, col, board_state, match_fruits_count, match_booster):

	# what is the top-most row of the match?
	topmost_row = row - match_fruits_count['up']

	# what is the bottom-bost row of the match?
	bottommost_row = row + match_fruits_count['down']
		
	# how many fruits above the topmost_row?
	fruits_above = fruits_above_count(topmost_row, col, board_state)

	# how many rows the fruits above the topmost_row should go down?
	total_rows_to_move = 1 + match_fruits_count['up'] + match_fruits_count['down']


	# Update the property of a specific coordinate to have a booster
	if match_booster != False:
		print("Match booster updated: ")
		print(match_booster)
		rows_properties[index_to_row[bottommost_row]][index_to_col[col]]['modifier'] = match_booster
		rows_properties[index_to_row[bottommost_row]][index_to_col[col]]['hasModifier'] = True
	
		## This will replace the fruits cleared by the match with a '/' to represent
		## "empty space".
		#board_state = execute_match_clear(row, col, board_state, match_booster, match_fruits_count)

	# if the match creates a booster, the central fruit will become a
	# booster instead of disappearing, and it will move to the bottommost_row
	# of the match.
	# What is the purpose of this shit? The central fruit becomes the fruit which
	# is at the bottommost_row of it's row? WTf? ISn't it supposed to be the other
	# way around? I'm commenting this for now, because after several runs of the
	# program under different circumstances, the result was always the same
	# with or without this piece of code.
	#if match_booster != False:
		#board_state[bottommost_row][col] = board_state[row][col]

	# pull down the fruits above the topmost_row by the amount of rows that are cleared by the match
	board_state = pull_fruits_above_down(bottommost_row, col, board_state, fruits_above, total_rows_to_move, match_booster, match_fruits_count)

	#print('\n')
	#print("board after vertical replacement")
	#print('\n')
	#for roar in board_state:
	#	print(roar)

	# this needs to be set to False after the first pull_fruits_above_down has been executed
	# otherwise the fruits above the left and right side of the match won't go down
	match_booster = False

	# how many fruits above the left fruit at col -1, col -2...?
	left_match_fruits = match_fruits_count['left']
	if left_match_fruits > 0:
		leftCol = int(col)
		for n in range(left_match_fruits):
			n += 1

			## change the col to analyze the fruit to the left and then to left of the previous fruits
			## and so on
			leftCol = leftCol - 1

			## get the amount of fruits above the fruit we are analyzing
			fruits_above = fruits_above_count(row, leftCol, board_state)

			# how many rows the fruits above the fruit we're analyzing should go down?
			total_rows_to_move = 1

			## pull the fruits above 1 row down (in the case of left and right adjacent fruits of
			## the match, the fruits only go down 1 row)
			board_state = pull_fruits_above_down(row, leftCol, board_state, fruits_above, total_rows_to_move, match_booster, match_fruits_count)

			#print('\n')
			#print("[left]board after removal of fruits above col " + str(leftCol))
			#print('\n')
			#for roar in board_state:
			#	print(roar)


	# how many fruits above the right fruit at col + 1, col +2...?
	right_match_fruits = match_fruits_count['right']
	if right_match_fruits > 0:
		rightCol = int(col)
		for n in range(right_match_fruits):
			n += 1

			## change the col to analyze the fruit to the right and then to right of the previous fruits
			## and so on
			rightCol = rightCol + 1

			## get the amount of fruits above the fruit we are analyzing
			fruits_above = fruits_above_count(row, rightCol, board_state)

			# how many rows the fruits above the fruit we're analyzing should go down?
			total_rows_to_move = 1

			## pull the fruits above 1 row down (in the case of left and right adjacent fruits of
			## the match, the fruits only go down 1 row)
			board_state = pull_fruits_above_down(row, rightCol, board_state, fruits_above, total_rows_to_move, match_booster, match_fruits_count)
			#print('\n')
			#print("[right] board after removal of fruits above col " + str(rightCol))
			#print('\n')
			#for roar in board_state:
			#	print(roar)

	return board_state

def simulation(row, col, priority_match, board_state, match_booster):

	#print('\n')
	#print("Board After Move:")
	#for rooow in board_state:
	#	print(rooow)
	#print('\n')

	match_fruits_count = match_clear_directions[priority_match]
	new_board = generate_board_state_after_match(row, \
				col, board_state, match_fruits_count, match_booster)
	return new_board

	#print('\n')
	#print("Board After Simulation:")
	#for rowrowrow in new_board:
	#	print(rowrowrow)
	#print('\n')

def move_outcome(row, col, valid_moves):
	moves_values = {}
	if rows_properties[index_to_row[row]][index_to_col[col]]['modifier'] == 'star_booster':
		pass
	for move_direction in valid_moves['validMoves']:
		if move_direction == 'up':
			print("## UP")
			output_board = moveUp(row, col)['output_board']
			match_check = matches_check(row - 1, col, output_board)
			priority_match = match_check['priority_match']
			match_booster = match_check['booster']
			board_state = simulation(row - 1, col, priority_match, output_board, match_booster)
			simulation_traverse = traverse(board_state, simulation_flag=True)
			if simulation_traverse['hasMatch'] != False:
				print("Cascated match detected.")
				print(simulation_traverse)
				print('\n')
				board_state = simulation_traverse['board_state']
				simulation_traverse = traverse(board_state, simulation_flag=True)
			else:
				pass

			## While running simulations, rows_properties should be reset after each
			## move evaluation.			
			reset_rows_properties()

		if move_direction == 'down':
			print("## DOWN")
			output_board = moveDown(row, col)['output_board']
			match_check = matches_check(row + 1, col, output_board)
			priority_match = match_check['priority_match']
			match_booster = match_check['booster']
			board_state = simulation(row + 1, col, priority_match, output_board, match_booster)
			simulation_traverse = traverse(board_state, simulation_flag=True)
			if simulation_traverse['hasMatch'] != False:
				print("Cascated match detected.")
				print(simulation_traverse)
				print('\n')			
				board_state = simulation_traverse['board_state']
				simulation_traverse = traverse(board_state, simulation_flag=True)
			else:
				pass			

			## While running simulations, rows_properties should be reset after each
			## move evaluation.
			reset_rows_properties()

		if move_direction == 'left':
			print("## LEFT")
			output_board = moveLeft(row, col)['output_board']
			match_check = matches_check(row, col - 1, output_board)
			priority_match = match_check['priority_match']
			match_booster = match_check['booster']
			board_state = simulation(row, col - 1, priority_match, output_board, match_booster)
			simulation_traverse = traverse(board_state, simulation_flag=True)
			print(simulation_traverse)
			if simulation_traverse['hasMatch'] != False:
				print("Cascated match detected.")
				print(simulation_traverse)
				print('\n')				
				board_state = simulation_traverse['board_state']				
				simulation_traverse = traverse(board_state, simulation_flag=True)
			else:
				pass			

			## While running simulations, rows_properties should be reset after each
			## move evaluation.				
			reset_rows_properties()

		if move_direction == 'right':
			print("## RIGHT")
			output_board = moveRight(row, col)['output_board']
			match_check = matches_check(row, col + 1, output_board)
			priority_match = match_check['priority_match']
			match_booster = match_check['booster']
			board_state = simulation(row, col + 1, priority_match, output_board, match_booster)
			simulation_traverse = traverse(board_state, simulation_flag=True)
			if simulation_traverse['hasMatch'] != False:
				print("Cascated match detected.")
				print(simulation_traverse)
				print('\n')				
				board_state = simulation_traverse['board_state']
				simulation_traverse = traverse(board_state, simulation_flag=True)
			else:
				pass			

			## While running simulations, rows_properties should be reset after each
			## move evaluation.			
			reset_rows_properties()

# in progress
def traverse(board_state, simulation_flag=False):
	for i in range(9):
		row = i
		for j in range(9):
			col = j
			current_fruit = board_state[row][col]
			if current_fruit == 'X':
				continue
			if simulation_flag == False:
				valid_moves = ValidMoves(row, col, board_state)
				if valid_moves['isValid'] == True:

					#print("Original Board:")
					#for row_row in board_state:
						#print(row_row)
					print(current_fruit + " at pos " + str(row + 1) + "," + 
					str(col + 1))
					#print("Valid Moves:")
					#print(valid_moves['validMoves'])
					#print('\n')

					move_outcome(row, col, valid_moves)
			has_match = False
			if simulation_flag == True:
				print(current_fruit + " at pos " + str(row + 1) + "," + 
					str(col + 1))
				match_check = matches_check(row, col, board_state)
				priority_match = match_check['priority_match']
				if priority_match == None:
					has_match = False
					continue
				else:
					has_match = True
				match_booster = match_check['booster']
				board_state = simulation(row, col, priority_match, board_state, match_booster)
				return {'hasMatch': has_match, 
						'position': current_fruit + " at pos " + str(row + 1) + "," + \
									str(col + 1),
						'match': priority_match,
						'match_booster': match_booster,
						'board_state': board_state
				}


traverse(board, simulation_flag=False)


#we know what a match does by now
#we know the tiles that are cleared
#and we are even capable of pulling down the fruits above these tiles

#now we just need it to be functional and at least better than a human
#it doesn't need to be the most eficient'

#I want the IA to tell me:
#1. after a match is made, if other matches will happen
#2. if the match explodes a booster (because of its major effects)
#3. what moves (and how valuable they are) there will be after that match is made
#4. if the match creates a booster