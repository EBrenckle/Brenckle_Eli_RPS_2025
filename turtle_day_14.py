# This file was created by: Eli Brenckle

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
have t

'''

# import package
import sys
import random
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

playagain_w, playagain_h = 138, 88

quit_w, quit_h = 136, 84


# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

playagain_image = os.path.join(images_folder, 'playagain.gif')
playagain_instance = turtle.Turtle()
playagain_instance.hideturtle()
screen.addshape(playagain_image)
playagain_instance.shape(playagain_image)
playagain_instance.penup()
playagain_pos_x = 0
playagain_pos_y = 0

quit_image = os.path.join(images_folder, 'quit.gif')    
quit_instance = turtle.Turtle()
quit_instance.hideturtle()
screen.addshape(quit_image)
quit_instance.shape(quit_image)
quit_instance.penup()
quit_pos_x = 0
quit_pos_y = -100

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
screen.addshape(paper_image)
paper_instance.shape(paper_image)
paper_instance.penup()
paper_pos_x = 0
paper_pos_y = 0
paper_instance.setpos(paper_pos_x,paper_pos_y)

rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
screen.addshape(rock_image)
rock_instance.shape(rock_image)
rock_instance.penup()
rock_pos_x = -300
rock_pos_y = 0
rock_instance.setpos(rock_pos_x,rock_pos_y)

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
screen.addshape(scissors_image)
scissors_instance.shape(scissors_image)
scissors_instance.penup()
scissors_pos_x = 300
scissors_pos_y = 0
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

computerChoice = ['rock', 'paper', 'scissors']
index = random.randint(0, len(computerChoice)-1)
aiChoice = computerChoice[index]

def spawnRock(x,y):
    # setup the rock image using the os module as rock_image
    rock_image = os.path.join(images_folder, 'rock.gif')
    # instantiate (create an instance of) the Turtle class for the rock
    rock_instance = turtle.Turtle()
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # assign vars for rock position
    rock_pos_x = x
    rock_pos_y = y
    # set the position of the rock_instance
    rock_instance.setpos(rock_pos_x,rock_pos_y)

def spawnRockAi(x,y):
    # setup the rock image using the os module as rock_image
    rock_image = os.path.join(images_folder, 'rockai.gif')
    # instantiate (create an instance of) the Turtle class for the rock
    rock_instance = turtle.Turtle()
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # assign vars for rock position
    rock_pos_x = x
    rock_pos_y = y
    # set the position of the rock_instance
    rock_instance.setpos(rock_pos_x,rock_pos_y)

def spawnPaper(x,y):
    # setup the paper image using the os module as paper_image
    paper_image = os.path.join(images_folder, 'paper.gif')
    # instantiate (create an instance of) the Turtle class for the paper
    paper_instance = turtle.Turtle()
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # assign vars for paper position
    paper_pos_x = x
    paper_pos_y = y
    # set the position of the paper_instance
    paper_instance.setpos(paper_pos_x,paper_pos_y)

def spawnPaperAi(x,y):
    # setup the paper image using the os module as paper_image
    paper_image = os.path.join(images_folder, 'paperai.gif')
    # instantiate (create an instance of) the Turtle class for the paper
    paper_instance = turtle.Turtle()
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # assign vars for paper position
    paper_pos_x = x
    paper_pos_y = y
    # set the position of the paper_instance
    paper_instance.setpos(paper_pos_x,paper_pos_y)

def spawnScissors(x,y):
    # setup the scissors image using the os module as scissors_image
    scissors_image = os.path.join(images_folder, 'scissors.gif')
    # instantiate (create an instance of) the Turtle class for the scissors
    scissors_instance = turtle.Turtle()
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # assign vars for scissors position
    scissors_pos_x = x
    scissors_pos_y = y
    # set the position of the scissors_instance
    scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

def spawnScissorsAi(x,y):
    # setup the scissors image using the os module as scissors_image
    scissors_image = os.path.join(images_folder, 'scissorsai.gif')
    # instantiate (create an instance of) the Turtle class for the scissors
    scissors_instance = turtle.Turtle()
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # assign vars for scissors position
    scissors_pos_x = x
    scissors_pos_y = y
    # set the position of the scissors_instance
    scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

def playAgain(x,y):
    playagain_image = os.path.join(images_folder, 'playagain.gif')
    playagain_instance = turtle.Turtle()
    screen.addshape(playagain_image)
    playagain_instance.shape(playagain_image)
    playagain_instance.penup()
    playagain_pos_x = x
    playagain_pos_y = y
    playagain_instance.setpos(playagain_pos_x,playagain_pos_y)

def quit(x,y):
    quit_image = os.path.join(images_folder, 'quit.gif')
    quit_instance = turtle.Turtle()
    screen.addshape(quit_image)
    quit_instance.shape(quit_image)
    quit_instance.penup()
    quit_pos_x = x
    quit_pos_y = y
    quit_instance.setpos(quit_pos_x,quit_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
def randomChoice():
    computerChoice = ['rock', 'paper', 'scissors']
    index = random.randint(0, len(computerChoice)-1)
    aiChoice = computerChoice[index]

# function that passes through wn onlick
def mouse_pos(x, y):
    #If player choice is rock
    if collide(x,y,rock_instance,rock_w,rock_h):
        randomChoice()  
        paper_instance.hideturtle()
        scissors_instance.hideturtle()
        scissors_instance.setpos(500,0)
        paper_instance.setpos(-500,0)
        rock_instance.setpos(-250,0)
        text.penup()
        text.goto(-250,170)
        text.write("YOU CHOSE ROCK!", False, "center", ('Ariel', 24, 'normal'))
        if aiChoice == 'rock':
            text.goto(250,170)
            text.write("AI CHOSE ROCK!", False, "center", ('Ariel', 24, 'normal'))
            spawnRockAi(250,0)
            text.goto(0,110)
            text.write("DRAW", False, "center", ('Ariel', 24, 'normal'))
            playAgain(0,0)
            quit(0,-100)
        elif aiChoice == 'paper':
            text.goto(250,170)
            text.write("AI CHOSE PAPER!", False, "center", ('Ariel', 24, 'normal'))
            spawnPaperAi(250,0)
            text.goto(0,110)
            text.write("YOU LOSE", False, "center", ('Ariel', 24, 'normal'))
            playAgain(0,0)
            quit(0,-100)
        elif aiChoice == 'scissors':
            text.goto(250,170)
            text.write("AI CHOSE SCISSORS!", False, "center", ('Ariel', 24, 'normal'))
            spawnScissorsAi(250,0)
            text.goto(0,110)
            text.write("YOU WIN", False, "center", ('Ariel', 24, 'normal'))
            playAgain(0,0)
            quit(0,-100)
    #If player choice is paper
    elif collide(x,y,paper_instance,paper_w,paper_h):       
        randomChoice()  
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        scissors_instance.setpos(500,0)
        rock_instance.setpos(-500,0)
        paper_instance.setpos(-250,0)
        text.penup()
        text.goto(-250,170)
        text.write("YOU CHOSE PAPER!", False, "center", ('Ariel', 24, 'normal'))
        if aiChoice == 'rock':
            text.goto(250,170)
            text.write("AI CHOSE ROCK!", False, "center", ('Ariel', 24, 'normal'))
            spawnRockAi(250,0)
            text.goto(0,110)
            text.write("YOU WIN", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,0)
            text.write("Play Again", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,-50)
            text.write("Quit", False, "center", ('Ariel', 24, 'normal'))
        elif aiChoice == 'paper':
            text.goto(250,170)
            text.write("AI CHOSE PAPER!", False, "center", ('Ariel', 24, 'normal'))
            spawnPaperAi(250,0)
            text.goto(0,110)
            text.write("DRAW!", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,0)
            text.write("Play Again", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,-50)
            text.write("Quit", False, "center", ('Ariel', 24, 'normal'))
        elif aiChoice == 'scissors':
            text.goto(250,170)
            text.write("AI CHOSE SCISSORS!", False, "center", ('Ariel', 24, 'normal'))
            spawnScissorsAi(250,0)
            text.goto(0,110)
            text.write("YOU LOSE!", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,0)
            text.write("Play Again", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,-50)
            text.write("Quit", False, "center", ('Ariel', 24, 'normal'))
        else:   
            return False
    #if player choice is scissors    
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        randomChoice()  
        rock_instance.hideturtle()
        paper_instance.hideturtle()
        paper_instance.setpos(500,0)
        rock_instance.setpos(-500,0)
        scissors_instance.setpos(-250,0)
        text.penup()
        text.goto(-250,170)
        text.write("YOU CHOSE SCISSORS!", False, "center", ('Ariel', 24, 'normal'))
        if aiChoice == 'rock':
            text.goto(250,170)
            text.write("AI CHOSE ROCK!", False, "center", ('Ariel', 24, 'normal'))
            spawnRockAi(250,0)
            text.goto(0,110)
            text.write("YOU LOSE!", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,0)
            text.write("Play Again", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,-50)
            text.write("Quit", False, "center", ('Ariel', 24, 'normal'))
        elif aiChoice == 'paper':
            text.goto(250,170)
            text.write("AI CHOSE PAPER!", False, "center", ('Ariel', 24, 'normal'))
            spawnPaperAi(250,0)
            text.goto(0,110)
            text.write("YOU WIN!", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,0)
            text.write("Play Again", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,-50)
            text.write("Quit", False, "center", ('Ariel', 24, 'normal'))
        elif aiChoice == 'scissors':
            text.goto(250,170)
            text.write("AI CHOSE SCISSORS!", False, "center", ('Ariel', 24, 'normal'))
            spawnScissorsAi(250,0)
            text.goto(0,110)
            text.write("DRAW!", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,0)
            text.write("Play Again", False, "center", ('Ariel', 24, 'normal'))
            text.goto(0,-50)
            text.write("Quit", False, "center", ('Ariel', 24, 'normal'))    
        else:   
            return False
    elif collide(x,y,playagain_instance, playagain_w, playagain_h):
            rpsGame()
    elif collide(x,y,quit_instance, quit_w, quit_h):
            turtle.hideturtle()
    else:
        return False

def rpsGame():
    spawnPaperAi(0,400)
    spawnRockAi(0,400)
    spawnScissorsAi(0,400)
    playAgain(0,400)
    quit(0,400)
    text.hideturtle()
    paper_image = os.path.join(images_folder, 'paper.gif')
    paper_instance = turtle.Turtle()
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_pos_x = 0
    paper_pos_y = 0
    paper_instance.setpos(paper_pos_x,paper_pos_y)

    rock_image = os.path.join(images_folder, 'rock.gif')
    rock_instance = turtle.Turtle()
    screen.addshape(rock_image)
    rock_instance.shape(rock_image)
    rock_instance.penup()
    rock_pos_x = -300
    rock_pos_y = 0
    rock_instance.setpos(rock_pos_x,rock_pos_y)

    scissors_image = os.path.join(images_folder, 'scissors.gif')
    scissors_instance = turtle.Turtle()
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_pos_x = 300
    scissors_pos_y = 0
    scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
    randomChoice()
    screen.onclick(mouse_pos)
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()
