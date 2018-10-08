# match-3-ai
Designed to make the best possible move in a match-3 game. Specifically for the mini-game in Dragon City: Fruit Puzzle Island.

# Well...
Ok, I've learned my lesson while coding this "little" project.

No - the AI doesn't work; at least not in an efficient way, and here's why:

# The code got too messy
I shouldn't have put everything into one big file. I should've created multiple files, each for a specific and well-defined purpose.

Also, some functions are way too big, some of them go way over 2 screens (over 100 lines) and that just makes the code over-complicated and messy. I should've created multiple functions to hande every little part of the big problem (like breaking down a big problem into small, more manageable problems), instead of creating one function to cover multiple parts of the big problem. This added way more complexity to the code than it should have.

As a human, there is a limit to things we can pay attention to, and more than 10 functions - some with hundreds of lines of code - into one big file with almost 2000 lines of code, is overkill for our little peanut brain.

I remember I had to go through each function multiple times to know what was happening when the code was executed. This is a signal that the code is messy, confusing and over-complicated.

There was also a "deadline". The AI was specifically made for a mini-game of match-3 in Dragon City, and the mini-game would disappear after 1 week +/-, so I had this period of time to come up with an AI. This time pressure was actually really good as it made code like a maniac and motivated me to challenge my discipline.

I spent 8 days (full-time) writing this and in the end, the goal wasn't reached - to create an AI to solve match-3 - but, I learned some really valuable lessons that will make my code more readable and organized, and I can't stress enough how important this is; I mean, had the code been organized and structured like I said I should've done before, I'd probably have made this AI work.

# Planning

I also learned something about planning. This project was kinda big compared to the others I made recently, so I couldn't just open the text editor and code; I had to plan how it was gonna work and what module I was going to work on at that moment. Something like this takes more than 1 session of coding to finish, so it definetely requires good planning. In other words, I couldn't just sit to code the whole thing, I had to sit and code 1/8 of the project.

I needed to think how the AI was going to accomplish it's goal. I had to break even small problems into even smaller pieces. Moving a piece up is very simple for us humans, but explaining to a machine what that means in a programming language is different. You have to create the board using something similar to chess notation and tell the machine that moving a piece up, literally means taking the value of the row X and column Y and replacing it by the value located at row X - 1 and column Y; and replacing the value at row X - 1, column Y for the value at row X, column Y (they exchange positions with each other).

That is just "moving up". While doing that, it also needs to keep track of the positions that contain modifiers (boosters in-game) and what happens when that booster moves.

In our amazing human brains, it sounds very easy and obvious - a kid can play that game - but when you think how to explain to a machine how the game works, it gets much more complicated, especially if you want that machine to be able to make the best possible move in a non-deterministic type of game.

So, I had to plan what modules I was going to work on and how I was gonna do it. It would be really bad to just dive in without planning, write some terrible piece of code just to realize, later on, that it's bad and have to rewrite it. Planning costs a bit of time, but saves a lot more.

# Giving up on this AI?

Nope. I will study more and will come up with something better.
