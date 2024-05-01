## SDSS Computing Studies Python Assignment


Objectives:
* Make a function call to execute a function
* Create your own function

Programs can get very long and complicated.  Often, we try to break a program into smaller tasks.  In fact, we can often think of having a program within a program.  These may have their own variables, and have limited data that they receive or send to other parts of the main program.

Today, we will explore how a function is defined and how we execute or "call" the function.

Look at example 1 to see how a function is defined:
Note the indenting. 
Note the inclusion of the round brackets in the function defintion.
Note that defining the function does not actually execute the function.

We have looked at quite a lot of commands and structures this year.  In addition to all of the math and logical operators as well as the code structures that control program flow, we have also looked at commands that do a specific task.

Consider the following:

pow(x,y) : which finds out the exponent of x to the power of y
math.floor(x) : which takes the float value of x and rounds it down to an int
int(x) : which takes a float value of x and converts it to an integer

These are examples of functions.  They are mini programs that can be created to do a specific tasks.  Defining function has a number of things in common:

* the keyword **def** is used to indicate that a function is being defined.
* There is a function name, that is used when you want to execute or "call" the function.
* Parameters are the things that are located inside the brackets.   These are important inputs that are needed to run the function or mini program.  The parameters are variables that can be used within the function

In example 2, we actually make use of the function by doing a function call in the main part of our program.

In example 3 we start to refine our program structure by defining a main of code.
While not strictly necessary for our purposes, now is a good time to start getting  into the habit.

Task 1:
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.

Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game
