#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import * #We imported a standard GUI, called tkinter, which allows the user access to many widgets and other tools.  
from time import * # We imported time, which allows the game to have delays for a certain amount of time 
import threading # We imported the threading module, which gives the user classes and functions for working with threads.  Threads allow functions to run at the same time
import random #This module generates random numbers, which is useful for making a game which requires many different numbers each time the user plays

whacks = 0 #This variable is used to track how many times the player hits a fruit, essentially counting the player’s score
hole = 0 #This represents the current hole being targeted by a player (becomes targeted when a fruit pops up in the tiles)

emojis = ["🍎","🍐","🍊","🍌","🥭","🍍","🥝"] #This list provides a set of different fruits which eventually pop up randomly during the game
random_emoji = random.choice(emojis) #This line uses the “random.choice()” to choose one fruit from the list and display it on the screen for a player to hit tap

    
screen = Tk() #Tk() creates the main program window and is assigned a variable called screen
screen.config(bg="sienna2", width=500, height=520) #This is used to set the background of the screen and make it the colour sienna.  On top of that, it is also setting the size of the game to be 500 pixels wide and 520 pixels high
screen.resizable(0, 0) #This prevents the user from dragging the edges to make the screen bigger or smaller
screen.attributes('-topmost', True) #This ensures that the screen for the video game is in front of all other windows on the user’s computer
tip = Label(bg='yellow', fg='black', text="Play with mouse for best experience") #Assigns a name, ‘tip’, to a label.  This label has a background (bg) which is yellow and the foreground (fg) is black.  In this case, the foreground is text which tells the user to the play the crush the fruit game with their computer mouse
tip.place(x=0, y=497) #This places the tip label at (0,497), which is in the bottom left corner
lab = Label(text="CRUSH THE FRUIT!", font=("Algerian", 26), bg='spring green', fg='black') #Assigns the name ‘lab’ to a label.  This label has text for the title of the game, with a font of Algerian at size 30.  The background behind this text is spring green, and the title is in black
lab.place(x=110, y=0)  # This places the lab label at (110,0), which is at the top middle part of the page, making it our title.
scorelabel = Label(text=whacks, width=7, font=('Bahnschrift', 30), bg='purple',fg='yellow') #Assigns a name ‘scorelabel’ to a label.  The part of the code which states ‘text=whacks’ means that the text in the label will be the amount of times the player crushes the fruit.  This label can be a maximum of 7 characters, with a font called Bahnschrift at a size of 30.  The background of this label is purple, with the foreground (the text) being yellow
scorelabel.place(x=170, y=52) #This places the score label at the coordinates (170, 52), which is under the title of the game
remark = Label(text="", width=17, bg='spring green', fg='black', font="Centaur 20") # Assigns a label called remark which has a possible width of 17 characters.  The background of the remark label is spring green, with the text in the foreground being black.  There is no initial text for the remark label
remark.place(x=130, y=107) #This piece of code is placed at the coordinates (130, 107), which is right under the scoreboard.  




def onwhack(): #E.C: A function is defined, and is called ‘onwhack’
    global hole, whacks #E.C: States that this is a global hole which is defined outside the function
    if hole == 1: #E.C: This if statement states that if the hole is equal to one, then it will perform a series of functions which are established below
        hole1.config(state='disabled', text='') #if the hole is one, then its state is disabled and the appearance of the button changes.  A text icon also appears.  
    elif hole == 2: #E.C: However, if the hole is two…
        hole2.config(state='disabled', text='') #Then its state is disabled and the appearance of the button changes.  A text icon also appears.  
    elif hole == 3: #However, if the hole is three…
        hole3.config(state='disabled', text='') # Then its state is disabled and the appearance of the button changes.  A text icon also appears.
    elif hole == 4: #However, if the hole is four…
        hole4.config(state='disabled', text='') #Then its state is disabled and the appearance of the button changes.  A text icon also appears.
    elif hole == 5: #However, if the hole is five…
        hole5.config(state='disabled', text='') #Then its state is disabled and the appearance of the button changes.  A text icon also appears.
    elif hole == 6: #However, if the hole is six…
        hole6.config(state='disabled', text='') #Then its state is disabled and the appearance of the button changes.  A text icon also appears.
    elif hole == 7: #However, if the hole is seven…
        hole7.config(state='disabled', text='') #Then its state is disabled and the appearance of the button changes.  A text icon also appears.
    elif hole == 8: #However, if the hole is eight…
        hole8.config(state='disabled', text='') #Then its state is disabled and the appearance of the button changes.  A text icon also appears.
    elif hole == 9: #However, if the hole is nine…
        hole9.config(state='disabled', text='') #Then its state is disabled and the appearance of the button changes.  A text icon also appears.
    global whacks #This statement essentially says that ‘whacks’ is considered a global variable
    whacks += 1 #If the fruit is crushed, this line allows the score to increase by increments of one every time
    scorelabel.config(text="* " + str(whacks) + " *") #This part of the code converts the number of whacks to a string which is displayed on the scoreboard.  It is surrounded by asterisks in the form of a string, which will also show up on the scoreboard.  


hole1 = Button( #Assigns a label to the ‘Button(‘ which is called hole1.  
    width=6, #Hole1 has a width of 6 units
    height=3, #Hole1 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole1.place(x=20, y=160) #Hole1 is placed at the coordinates (20,160).
hole2 = Button( #Assigns a label to the ‘Button(‘ which is called hole2.
    width=6, #Hole2 has a width of 6 units
    height=3, #Hole2 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole2.place(x=20, y=290) #Hole2 is placed at the coordinates (20,290).
hole3 = Button( #Assigns a label to the ‘Button(‘ which is called hole3.
    width=6, #Hole3 has a width of 6 units
    height=3, #Hole3 has a height of 3 units
    bg='black',  #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole3.place(x=20, y=420) #Hole3 is placed at the coordinates (20,420).
hole4 = Button( #Assigns a label to the ‘Button(‘ which is called hole4.
    width=6, #Hole4 has a width of 6 units
    height=3, #Hole4 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is calle
hole4.place(x=200, y=160) #Hole4 is placed at the coordinates (220,160).
hole5 = Button( #Assigns a label to the ‘Button(‘ which is called hole5.
    width=6, #Hole5 has a width of 6 units
    height=3,  #Hole5 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole5.place(x=200, y=290) #Hole5 is placed at the coordinates (220,290).
hole6 = Button( #Assigns a label to the ‘Button(‘ which is called hole6.
    width=6, #Hole6 has a width of 6 units
    height=3, #Hole6 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole6.place(x=200, y=420) #Hole6 is placed at the coordinates (220,420).
hole7 = Button( #Assigns a label to the ‘Button(‘ which is called hole7.
    width=6, #Hole7 has a width of 6 units
    height=3, #Hole7 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole7.place(x=390, y=160) #Hole7 is placed at the coordinates (420,160).
hole8 = Button( #Assigns a label to the ‘Button(‘ which is called hole8.
    width=6, #Hole8 has a width of 6 units
    height=3, #Hole8 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the user
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole8.place(x=390, y=290) #Hole8 is placed at the coordinates (420,290).
hole9 = Button( #Assigns a label to the ‘Button(‘ which is called hole9.
    width=6, #Hole9 has a width of 6 units
    height=3, #Hole9 has a height of 3 units
    bg='black', #The background colour of the hole is black
    state='disabled', #The button is initially at a disabled state, which means it cannot be clicked on by the use
    command=onwhack) #This part of the code states that when the button is clicked on, a function called ‘onwhack’ is called
hole9.place(x=390, y=420) #Hole9 is placed at the coordinates (420,420).


def start(): #The function ‘start()’ is defined
    global whacks #This states that ‘global whacks’ is a global variable, meaning that it is declared outside any function
    whacks = 0 #This resets the players score to zero at the start of a new game
    remark.config(text="") #Clears anything in the ‘remark’ label
    replaybtn.config(state='disabled') #This causes the replay button to be disabled when a new game is in progress.  Specifically, the ‘replay.btn’ button prevents the player from clicking ‘replay’ while a game has begun
    t = threading.Thread(target=whac_a_mole) #This sets up a thread that can run the ‘crush the fruit’ function
    t.start() #Starts the new thread and allows the game to run on its own while another program continues

try:
    with open("highscore.txt","r") as file: #Opens a high score file in read-only mode 
        high_score = int(file.read()) # reads the content and converts to an integer, then assigns it to variable high_score
        
except FileNotFoundError: # in a case which there is no highscore saved, file will not be found
    high_score = 0 # if file is not found, highscore will equal 0
    
high_score_label = Label(text = f"High Score: {high_score}", width= 10, font=('Bahnschrift',20),bg = 'purple',fg ='yellow') # designs the label for the high score, as purple background and yellow writing
high_score_label.place(x = 350, y = 2) # determines the placement of the high score label


def whac_a_mole(): #Defines a function called ‘whac_a_mole()’
    ready_set_whack() #The function ‘ready_set_whack()’ is called, which allows the player to get ready for the game ahead
    global hole, whacks, high_score #This states that ‘global hole’ is a global variable, meaning that it is declared outside any function

    for i in range(0, 10): #A ‘for’ loop is called, which runs the loop 60 times, making the game 60 seconds
        remark.config(text="LEVEL 1") #Is a label widget in the GUI, which when executed the text displayed in the ‘scorelabel’ widget is changed to "WHACK!!"
        sleep(1)
        hole = random.randint(1, 9) #This function selects a random hole for a fruit to pop out of (between hole 1 to 9)
        random_emoji = random.choice(emojis)
        if hole == 1: #if the hole selected is the first one…
            hole1.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole1.config(state='disabled', text='', bg='black') #After the one second delay, hole1 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 2: #if the hole selected is the second one…
            hole2.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole2.config(state='disabled', text='', bg='black')  #After the one second delay, hole2 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 3: #if the hole selected is the third one…
            hole3.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole3.config(state='disabled', text='', bg='black') #After the one second delay, hole3 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 4: #if the hole selected is the fourth one…
            hole4.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole4.config(state='disabled', text='', bg='black') #After the one second delay, hole4 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 5: #if the hole selected is the fifth one…
            hole5.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole5.config(state='disabled', text='', bg='black') #After the one second delay, hole5 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 6: #if the hole selected is the sixth one…
            hole6.config(  #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole6.config(state='disabled', text='', bg='black')  #After the one second delay, hole6 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 7: #if the hole selected is the seventh one…
            hole7.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole7.config(state='disabled', text='', bg='black')  #After the one second delay, hole7 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 8:  #if the hole selected is the eighth one…
            hole8.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole8.config(state='disabled', text='', bg='black') #After the one second delay, hole8 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 9: #if the hole selected is the ninth one…
            hole9.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1.3) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole9.config(state='disabled', text='', bg='black') #After the one second delay, hole9 changes back to a disabled state, the text disappears, and the background is black.



    for i in range(10, 20): #A ‘for’ loop is called, which runs the loop 60 times, making the game 60 seconds
        remark.config(text="LEVEL 2") #Is a label widget in the GUI, which when executed the text displayed in the ‘scorelabel’ widget is changed to "WHACK!!"
        sleep(1)
        hole = random.randint(1, 9) #This function selects a random hole for a fruit to pop out of (between hole 1 to 9)
        random_emoji = random.choice(emojis)
        if hole == 1: #if the hole selected is the first one…
            hole1.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole1.config(state='disabled', text='', bg='black') #After the one second delay, hole1 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 2: #if the hole selected is the second one…
            hole2.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole2.config(state='disabled', text='', bg='black')  #After the one second delay, hole2 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 3: #if the hole selected is the third one…
            hole3.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole3.config(state='disabled', text='', bg='black') #After the one second delay, hole3 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 4: #if the hole selected is the fourth one…
            hole4.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole4.config(state='disabled', text='', bg='black') #After the one second delay, hole4 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 5: #if the hole selected is the fifth one…
            hole5.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole5.config(state='disabled', text='', bg='black') #After the one second delay, hole5 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 6: #if the hole selected is the sixth one…
            hole6.config(  #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole6.config(state='disabled', text='', bg='black')  #After the one second delay, hole6 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 7: #if the hole selected is the seventh one…
            hole7.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole7.config(state='disabled', text='', bg='black')  #After the one second delay, hole7 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 8:  #if the hole selected is the eighth one…
            hole8.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole8.config(state='disabled', text='', bg='black') #After the one second delay, hole8 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 9: #if the hole selected is the ninth one…
            hole9.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(1) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole9.config(state='disabled', text='', bg='black') #After the one second delay, hole9 changes back to a disabled state, the text disappears, and the background is black


    for i in range(20, 30): #A ‘for’ loop is called, which runs the loop 30 times
        remark.config(text="LEVEL 3") #Is a label widget in the GUI, which when executed the text displayed in the ‘scorelabel’ widget is changed to "WHACK!!"
        sleep(1)
        hole = random.randint(1, 9) #This function selects a random hole for a fruit to pop out of (between hole 1 to 9)
        random_emoji = random.choice(emojis)
        if hole == 1: #if the hole selected is the first one…
            hole1.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole1.config(state='disabled', text='', bg='black') #After the one second delay, hole1 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 2: #if the hole selected is the second one…
            hole2.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole2.config(state='disabled', text='', bg='black')  #After the one second delay, hole2 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 3: #if the hole selected is the third one…
            hole3.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole3.config(state='disabled', text='', bg='black') #After the one second delay, hole3 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 4: #if the hole selected is the fourth one…
            hole4.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole4.config(state='disabled', text='', bg='black') #After the one second delay, hole4 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 5: #if the hole selected is the fifth one…
            hole5.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole5.config(state='disabled', text='', bg='black') #After the one second delay, hole5 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 6: #if the hole selected is the sixth one…
            hole6.config(  #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole6.config(state='disabled', text='', bg='black')  #After the one second delay, hole6 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 7: #if the hole selected is the seventh one…
            hole7.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole7.config(state='disabled', text='', bg='black')  #After the one second delay, hole7 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 8:  #if the hole selected is the eighth one…
            hole8.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole8.config(state='disabled', text='', bg='black') #After the one second delay, hole8 changes back to a disabled state, the text disappears, and the background is black.
        elif hole == 9: #if the hole selected is the ninth one…
            hole9.config( #The block of code is executed
                state='normal', #Changes the state of the hole from ‘disabled’ to ‘normal’, meaning the player can click it
                text=random_emoji, #The text is changed to display the fruit
                bg='pink', #The background of the button changes pink
                fg='black') #The colour of the fruit icon is black
            sleep(0.8) #The ‘sleep’ function pauses the program execution for 1 second, allowing the player to click the fruit
            hole9.config(state='disabled', text='', bg='black') #After the one second delay, hole9 changes back to a disabled state, the text disappears, and the background is black

            
            
    replaybtn.config(state='normal') #After the game is finished, a replay button is enabled which prompts the player to start a new game
    global whacks #This states that ‘global whacks’ is a global variable, meaning that it is declared outside any function
    if whacks < 5: #This checks if the number of ‘whacks’ the player achieved is less than 10
        remark.config(text="POOR") #If the number is less than 10, a remark is displayed which states “POOR”
    elif whacks >= 5 and whacks < 10: #This checks if the number of ‘whacks’ the player achieved is greater than 10 but less than 20
        remark.config(text="BAD") #If the number is between 10 and 20, a remark is displayed which states “BAD”
    elif whacks >= 10 and whacks < 15: #This checks if the number of ‘whacks’ the player achieved is greater than 20 but less than 30
        remark.config(text="DO BETTER!") #If the number is between 20 and 30, a remark is displayed which states “DO BETTER”
    elif whacks >= 15 and whacks < 20: #This checks if the number of ‘whacks’ the player achieved is greater than 30 but less than 40
        remark.config(text="GOOD") #If the number is between 30 and 40, a remark is displayed which states “GOOD”
    elif whacks >= 20 and whacks < 25: #This checks if the number of ‘whacks’ the player achieved is greater than 40 but less than 50
        remark.config(text="GREAT!") #If the number is between 40 and 50, a remark is displayed which states “GREAT”
    elif whacks >= 25 and whacks < 29: #This checks if the number of ‘whacks’ the player achieved is greater than 40 but less than 50
        remark.config(text="AWESOME!") #If the number is between 50 and 60, a remark is displayed which states “AWESOME”
    elif whacks == 30: #If the number of whacks is equal to 60 then…
        remark.config(text="CRUSHED 'em ALL!", font="Centaur 18") #A remark is displayed which states “GOT ‘em ALL!”
    if whacks > high_score: # the current score a.k.a “whacks” is greater than highscore
        high_score = whacks # this updates the current score to high_score 
        high_score_label.config(text = f"High Score: {high_score}") #updates the display with the current high score
    with open("high_score.txt","w") as file: # opens file in write mode and rewrites it, if there's no file it will create one.
        file.write(str(high_score)) # converts the integer to a string before writing it into the file

def ready_set_whack(): #A function that is responsible for displaying a countdown-like sequence 
    sleep(1) #Each step in the sequence is displayed for 1 second
    scorelabel.config(text="Ready") #Is a label widget in the GUI, which when executed the text displayed in the ‘scorelabel’ widget is changed to "Ready."
    sleep(1)
    scorelabel.config(text="Set") #Is a label widget in the GUI, which when executed the text displayed in the ‘scorelabel’ widget is changed to "Set"
    sleep(1)
    scorelabel.config(text="CRUSH!!") #Is a label widget in the GUI, which when executed the text displayed in the ‘scorelabel’ widget is changed to "WHACK!!"
    sleep(1)
    scorelabel.config(text="0") #Sets the score label to zero once, the Ready, Set, WHACK!! Sequence is carried out


replaybtn = Button(text="Play Again", command=start)#creates a button labelled “Play Again” that when clicked the ‘start’ function will be called 
replaybtn.place(x=0, y=2) #The button is placed at coordinates (0,2) within the GUI 

start() #when the “Play Again” button is clicked the ‘start’ function will be executed 


screen.mainloop()#Starts the main event loop. Will continuously listen to user inputs, until the GUI window is closed 


# In[ ]:




