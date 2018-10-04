###########################################################################

## original board that I used
## backup just in case I want to use it again to check with
## the board I hand-wrote in my notepad
#row1 = ['R', 'Y', 'B', 'G', 'R', 'P', 'Y', 'R', 'R']
#row2 = ['R', 'O', 'O', 'P', 'R', 'R', 'B', 'B', 'O']
#row3 = ['O', 'G', 'R', 'P', 'G', 'Y', 'R', 'R', 'P']
#row4 = ['O', 'Y', 'P', 'R', 'P', 'P', 'R', 'Y', 'R']
#row5 = ['B', 'G', 'Y', 'P', 'O', 'O', 'Y', 'P', 'Y']
#row6 = ['G', 'Y', 'R', 'O', 'Y', 'Y', 'P', 'G', 'R']
#row7 = ['R', 'O', 'O', 'Y', 'B', 'B', 'G', 'B', 'P']
#row8 = ['O', 'B', 'B', 'P', 'Y', 'Y', 'P', 'R', 'Y']
#row9 = ['Y', 'R', 'B', 'Y', 'P', 'R', 'B', 'B', 'O']


## in-game real board
row1 = ['P', 'Y', 'R', 'Y', 'R', 'B', 'Y', 'P', 'G']
row2 = ['R', 'R', 'G', 'P', 'Y', 'R', 'G', 'O', 'G']
row3 = ['P', 'G', 'Y', 'P', 'B', 'R', 'P', 'O', 'O']
row4 = ['B', 'B', 'O', 'G', 'R', 'B', 'R', 'P', 'G']
row5 = ['R', 'G', 'O', 'G', 'G', 'O', 'Y', 'P', 'R']
row6 = ['O', 'Y', 'B', 'O', 'R', 'R', 'P', 'O', 'G']
row7 = ['G', 'O', 'R', 'R', 'G', 'Y', 'P', 'B', 'O']
row8 = ['O', 'O', 'G', 'Y', 'P', 'Y', 'Y', 'R', 'R']
row9 = ['Y', 'P', 'Y', 'O', 'O', 'P', 'P', 'O', 'G']

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


board = [list(row1), list(row2), list(row3), list(row4), list(row5), list(row6),
		 list(row7), list(row8), list(row9)
]




# what we learned from the video
# you can always swap a booster with another, independent of color, type or if
# it makes a match.
# horizontal/vertical with horizontal/vertical = clear whole row and col relative
# to the fruit that was swapped (eg: you moved a booster down and swapped with another booster
# the reference position will be row + 1 (cause  you moved the booster down))

# horizontal/vertical + area booster clears 3 rows or 3 cols (depends if it's horizontal or
# vertical booster) relative to the position the swapped to

#if after a match, a t-shape happens, the area_booster will appear on the position you
#swapped from (if you swapped from 'row' to 'row + 1', the booster will appear on 'row')

#when a booster is made, it will appear on the position the central fruit was swapped to
#and it will fall to the rows below if the match clears rows below

# area booster will clear all 8 adjacent fruits (all around the booster where it exploded)

# if an area booster explodes another adjacent booster, the adjacent booster will not trigger

# when a horizontal booster is made after another match was made (cascated)
# the booster will appear in the last "col" of the match

# a booster resultant of a cascated match appears in the row/col that was cleared

# a booster destroyed by consequence of another booster effect, will not proc

# a booster that appears as a result of another match, doesn't have a clear
# definition/rule of where the booster will appear, so we can't count on it



# take into consideration:
# boosters should affect the board in a specific way

## IMPORTANT!
# if the match creates a booster, the current_fruit (central one; the one that was moved)
# will not disappear, only the adjacent fruits will. The current_fruit only disappears
# when the match doesn't creaate a booster.


def pull_fruits_above_down(row, col, board_state, fruits_above, total_rows_to_move, match_booster):
	
	# If the match creates a booster, it means the central fruit won't disappear - it will turn into
	# a booster, and so the amount of fruits that disappear in the vertical reduces by 1, thus reducing
	# the amount of rows the fruits above will move down.
	if match_booster != False:
			total_rows_to_move -= 1

	for fruit_above in range(fruits_above):
		fruit_above += total_rows_to_move
		board_state[row - (fruit_above - total_rows_to_move)][col] = board_state[row - fruit_above][col]

	# how do we address the current fruit transforming into a booster?
	# it doesn't disappear like the rest of the fruits of the match
	# it goes down before the other fruits above
	# the amount of rows it goes down = amount of fruits below it

	# Replace the space left by the fruits that moved down by 'X', which means
	# random, unpredictable fruit. Number of 'X' in the specific vertical line = total_rows_to_move
	for num in range(total_rows_to_move):
		board_state[num][col] = 'X'

	return board_state



# need to implement something like this on pull_fruits_above_down()
if match_booster != False:
	total_rows_to_move -= 1
	if match_booster == 'vertical_booster':
		pass
	if match_booster == 'horizontal_booster':
		pass
	if match_booster == 'area_booster':
		pass
	if match_booster == 'star_booster':
		pass


def generate_board_state_after_match(row, col, board_state, match_fruits_count, match_booster):

	# what is the top-most row of the match?
	topmost_row = row - match_fruits_count['up']

	# what is the bottom-bost row of the match?
	bottommost_row = row + match_fruits_count['down']

	# how many fruits above the topmost_row?
	fruits_above = fruits_above_count(topmost_row, col, board_state)

	# how many rows the fruits above the topmost_row should go down?
	total_rows_to_move = 1 + match_fruits_count['up'] + match_fruits_count['down']

	# pull down the fruits above the topmost_row by the amount of rows that are cleared by the match
	board_state = pull_fruits_above_down(bottommost_row, col, board_state, fruits_above, total_rows_to_move, match_booster)

	print('\n')
	print("board after vertical replacement")
	print('\n')
	for roar in board_state:
		print(roar)

	# how many fruits above the left fruit at col -1, col -2...?
	left_match_fruits = match_fruits_count['left']
	print('Amount of fruits to the left:')
	print(list(lol for lol in range(left_match_fruits)))
	if left_match_fruits > 0:
		leftCol = int(col)
		for n in range(left_match_fruits):
			n += 1
			print('n value is: ' + str(n))

			## change the col to analyze the fruit to the left and then to left of the previous fruits
			## and so on
			leftCol = leftCol - 1

			## get the amount of fruits above the fruit we are analyzing
			fruits_above = fruits_above_count(row, leftCol, board_state)

			# how many rows the fruits above the fruit we're analyzing should go down?
			total_rows_to_move = 1

			## pull the fruits above 1 row down (in the case of left and right adjacent fruits of
			## the match, the fruits only go down 1 row)
			board_state = pull_fruits_above_down(row, leftCol, board_state, fruits_above, total_rows_to_move, match_booster)

			print('\n')
			print("[left]board after removal of fruits above col " + str(leftCol))
			print('\n')
			for roar in board_state:
				print(roar)


	# how many fruits above the right fruit at col + 1, col +2...?
	right_match_fruits = match_fruits_count['right']
	print('Amount of fruits to the right:')
	print(list(yeah for yeah in range(right_match_fruits)))
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
			board_state = pull_fruits_above_down(row, rightCol, board_state, fruits_above, total_rows_to_move, match_booster)
			print('\n')
			print("[right] board after removal of fruits above col " + str(rightCol))
			print('\n')
			for roar in board_state:
				print(roar)

	return board_state




###########################################################################