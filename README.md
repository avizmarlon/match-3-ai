# match-3-ai
Designed to make the best possible move in a match-3 game. Specifically for the mini-game in Dragon City: Fruit Puzzle Island.

Ok... I've learned my lesson while coding this "little" project.

No - the AI doesn't work; at least not in an efficient way, and here's why:

# The code got too messy
I shouldn't have put everything into one big file. I should've created multiple files, each for a specific and well-defined purpose.

Also, some functions are way too big, some of them go way over 2 screens (over 100 lines) and that just makes the code over-complicated and messy. I should've created multiple functions to hande every little part of the big problem (like breaking down a big problem into small, more manageable problems), instead of creating one function to cover multiple parts of the big problem. This added way more complexity to the code than it should have.

As a human, there is a limit to things we can pay attention to, and more than 10 functions - some with hundreds of lines of code - into one big file with almost 2000 lines of code, is overkill for our little peanut brain.

I remember I had to go through each function multiple times to know what was happening when the code was executed. This is a signal that the code is messy, confusing and over-complicated.

I spent 8 days (full-time) writing this and in the end, the goal wasn't reached - to create an AI to solve match-3 - but, I learned some really valuable lessons that will make my code more readable and organized, and I can't stress enough how important this is; I mean, had the code been organized and structured like I said I should've done before, I'd probably have made this AI work.

# Giving up on this AI?

Nope. I will study more and will come up with something better.
