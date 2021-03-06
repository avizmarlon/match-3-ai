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