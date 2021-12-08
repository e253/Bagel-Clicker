# Names: Emilie Neulen, Ethan Steere
# Computing IDs: ean4tp, xaq5rz
# Overall Description
'''
https://github.com/e253/Bagel-Clicker-Game/blob/master/bagel_clicker.py
Bodo’s bagel unofficially sponsered game.
Object of the game is to click on an bagel that moves .
"Orders" come in for each level for a certain amount of bagels. The player must click on the moving bagel to make a bagel.
This becomes increasingly more difficult as the level number gets higher as there are more bagels that need to be made.
'''
#####################
# Required Features #
#####################

# 1: User Input
"""
There is user input for the main action from the mouse. The mouse must try to click on the bagel.
"""

# 2: Start Screen
"""
There will be a start screen where the player can opt to start the game.
"""

# 3: Game Over
"""
The condition for ending the game will be the failing to complete an order in the allotted time. The bagel will stop moving and there will be a "GAME OVER" message.
"""

# 4: Small Enough Window
"""
The window size will be 800 by 600, the maximum allowed size. 
"""

# 5: Graphics and Images
"""
There will be a bagel graphic as well as a background of an industrial restaurant kitchen where our player is theoretically working.
"""



######################
# 4 Optional Featues #
######################

# 1: Timer
"""
There will be a timer to make the required amount of bagels to fufill the order.
"""

# 2: Multiple Levels
"""
As the player compeletes each order they go up a level. With each new level the game gets more difficult and the setting changes.
"""

# 3: Restart from Game Over
"""
When the player inevitably loses, they can restart by hitting the Space key when prompted.
"""

# 4: Sprite Animation
"""
When you click on the bagel it will deform outward slightly to let you know you successfully pressed it. The animation will make it seem as if you really squish the bagel.
"""

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

# Kitchen Backgrounds
background1 = gamebox.from_image(400, 300, "kitchen-background-1.png")
background1.size = [800, 600]

background2 = gamebox.from_image(400, 300, "kitchen-background-2.png")
background2.size = [800, 600]

background3 = gamebox.from_image(400, 300, "kitchen-background-3.png")
background3.size = [800, 600]

background4 = gamebox.from_image(400, 300, "kitchen-background-4.png")
background4.size = [800, 600]

background5 = gamebox.from_image(400, 300, "kitchen-background-5.png")
background5.size = [800, 600]

background6 = gamebox.from_image(400, 300, "kitchen-background-6.png")
background6.size = [800, 600]

background7 = gamebox.from_image(400, 300, "kitchen-background-7.png")
background7.size = [800, 600]

background = {"b1":background1, "b2":background2, "b3":background3, "b4":background4, "b5":background5, "b6":background6, "b7":background7}
# Bagel
bagel_sheet = gamebox.load_sprite_sheet("bagel_sheet.png", 4, 4)
bagel_ind = 0
bagel = gamebox.from_image(400, 300, bagel_sheet[bagel_ind])
bagel.size = [21, 16]
# Score
score = gamebox.from_text(45, 15, 'Score: 0', 25, 'red', bold=True)
# Borders
bottom = gamebox.from_color(400, 601, "white", 800, 1)
top = gamebox.from_color(400, -1, "white", 800, 1)
left = gamebox.from_color(-1, 300, "white", 1, 600)
right = gamebox.from_color(801, 300, 'white', 1, 600)
# Game Over
over = gamebox.from_text(400, 300, "GAME OVER", 100, "red")
over_instructions = gamebox.from_text(400, 500, "Press Space to restart", 50, "red")
# Level finished
level_complete = gamebox.from_text(400, 200, "Level Complete!", 72, "red")
level_complete_instructions = gamebox.from_text(400, 400, "Press Space to continue", 50, "red")


# Helpers
def reset_speeds():
    """
    This function resets the speed of the bagel
    """
    bagel.speedx = random.randrange(-20, 20, 5)
    bagel.speedy = random.randrange(-20, 20, 5)

def reset_timer():
    """
    This function resets the amount of time on the timer to the original amount
    """
    global time
    time = 200

def game_over_function():
    """
    This function sets up the game over message and also resets all the variables to their values from the beginning of the game
    """
    global Level
    global game_over
    global have_to_make
    game_over = True
    camera.draw(over)
    camera.draw(over_instructions)
    Level = 1
    have_to_make = 5



# Startup
reset_speeds()
ticks = 0
bagel_score = 0
mouse_on = False
start = False
game_over = False
time = 200
Level = 1
have_to_make = 5

def tick(keys):
    """
    This is the function that describes all the mechanics of the game
    :param keys: keys that can be pressed 
    """
    global mouse_on
    global bagel_score
    global start
    global game_over
    global time
    global Level
    global have_to_make
    global bagel_ind
    global background

    #Start screen
    if not start:
        camera.clear('black')
        camera.draw(gamebox.from_text(400, 100, "Bagel Clicker", 72, "blue"))
        camera.draw(gamebox.from_text(400, 150, "Made by: Ethan Steere (xaq5rz) and Emilie Neulen (ean4tp)", 30, "blue"))
        camera.draw(gamebox.from_text(400, 300, "Instructions:", 40, "red"))
        camera.draw(gamebox.from_text(400, 350, "Bodo's needs help finishing all their catering orders!", 20, "red"))
        camera.draw(gamebox.from_text(400, 400, "Click on the moving bagel to make a bagel, and make as many as needed before the time runs out.", 20, "red"))
        camera.draw(gamebox.from_text(400, 450, "With each passing level the place of business will change and the task will be slightly more difficult. Good Luck!", 20, "red"))
        camera.draw(gamebox.from_text(400, 500, "Press Space to start", 50, "blue"))
        camera.display()
        if pygame.K_SPACE in keys:
            start = True

    # User interaction
    if start:
        if not game_over:
            if not camera.mouseclick:
                mouse_on = False
                bagel.size = [21-Level, 16-Level]
            if (bagel.x - 20, bagel.y - 15) < (camera.mousex, camera.mousey) < (
                bagel.x + 20, bagel.y + 15) and camera.mouseclick and not mouse_on:
                bagel_score += 1
                bagel.size = [40, 30]
                mouse_on = True

    # Resets Speeds every 2 seconds
            if ticks % 60:
                reset_speeds()

    # Decreasing time
            time -= 1
            timer = gamebox.from_text(750, 15, "Time: {}".format(time), 25, "red", bold=True)

    # Side Interactions
            if bagel.touches(bottom) or bagel.touches(top):
                bagel.speedy *= -1
                bagel.speedx = random.randrange(-20, 20, 5)
            if bagel.touches(left) or bagel.touches(right):
                bagel.speedx *= -1
                bagel.speedx = random.randrange(-20, 20, 5)

    # If it glitches out of the window
            if bagel.x < -2 or bagel.x > 802:
                bagel.x = 400
            if bagel.y < -2 or bagel.y > 602:
                bagel.x = 300



    # Move Bagel Around
            bagel.x += bagel.speedx
            bagel.y += bagel.speedy

    # Refresh Stuff
            camera.clear('black')
            camera.draw(background['b{}'.format(Level)])
            keys.clear()
            camera.draw(gamebox.from_text(45, 15, 'Score: {}'.format(bagel_score), 25, 'red', bold=True))
            camera.draw(gamebox.from_text(750, 35, "Level: {}".format(Level), 25, "red"))
            camera.draw(gamebox.from_text(78, 35, "Bagels needed: {}".format(have_to_make), 25, "red"))

            # Chanage bagel from sheet
            if ticks % 3 == 0:
                if bagel_ind == len(bagel_sheet) -1:
                    bagel_ind = 0
                else:
                    bagel_ind += 1
                bagel.image = bagel_sheet[bagel_ind]

            camera.draw(bagel)
            camera.draw(timer)

    # Game Over or Level Complete
            if Level < 7:
                if time == 0 and bagel_score < have_to_make:
                    game_over_function()
                elif bagel_score >= have_to_make and time >= 0:
                    game_over = True
                    camera.draw(level_complete)
                    camera.draw(level_complete_instructions)
                    Level += 1
                    have_to_make += 5
            elif Level == 7:
                if time == 0 and bagel_score < have_to_make:
                    game_over_function()
                elif bagel_score >= have_to_make and time >= 0:
                    game_over = True
                    camera.draw(level_complete)
                    camera.draw(gamebox.from_text(400, 300, "You finished all the orders!", 72, "red"))
                    camera.draw(gamebox.from_text(400, 500, "Press Space to play again", 72, "red"))
                    Level = 1
                    have_to_make = 5

        else:
            if pygame.K_SPACE in keys:
                game_over = False
                reset_speeds()
                reset_timer()
                bagel_score = 0


        camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
