# Overall Description
'''
https://github.com/e253/Bagel-Clicker-Game/blob/master/bagel_clicker.py

Bodo’s bagel unofficially sponsered game.
Object of the game is to click on an bagel that moves more erraticly with each level.
"Orders" come in for each level for a certain amount of bagels. The player must click on the moving bagel to make a bagel.
This becomes increaseingly more difficult as the level number gets higher. There are more bagels to be made in less time. The bagel will move more quickly.
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
There will be a start screen where the player can opt to start the game and also change difficulty.
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
As the player compeletes each order they go up a level. With each new level the game gets more difficult....
"""

# 3: Restart from Game Over
"""
When the player inevitably loses, they can restart by hitting the R key when prompted. Or, they can return to the home screen.
"""

# 4: Sprite Animation
"""
When you click on the bagel it will deform outward slightly to let you know you successfully pressed it. The animation will make it seem as if you really squish the bagel.
"""



import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)


# Kitchen Background
background = gamebox.from_image(400, 300, "kitchen-background.png")
background.size = [800, 600]
# Bagel
bagel = gamebox.from_image(400, 300, "bagel.png")
bagel.size = [20,15]
# Score
score = gamebox.from_text(45, 15 , 'Score: 0', 25, 'red', bold=True)
# Borders
bottom = gamebox.from_color(400, 601, "white", 800, 1)
top = gamebox.from_color(400, -1, "white", 800, 1)
left = gamebox.from_color(-1, 300, "white", 1, 600)
right = gamebox.from_color(801, 300, 'white', 1, 600)


# Helpers
def reset_speeds():
    bagel.speedx = random.randrange(-20, 20, 5)
    bagel.speedy = random.randrange(-20, 20, 5)
    

# Startup
reset_speeds()
ticks = 0
bagel_score = 0
mouse_on = False


def tick(keys):
    global mouse_on
    global bagel_score

    # User interaction
    if not camera.mouseclick:
        mouse_on = False
        bagel.size = [20,15]
    if (bagel.x - 20, bagel.y - 15) < (camera.mousex, camera.mousey) < (bagel.x + 20, bagel.y + 15) and camera.mouseclick and not mouse_on:
        bagel_score += 1
        bagel.size = [40, 30]
        mouse_on = True

    # Resets Speeds every 2 seconds
    if ticks % 60:
        average_speed = two_total/60
        reset_speeds()

    # Side Interactions
    if bagel.touches(bottom) or bagel.touches(top):
        bagel.speedy *= -1
        bagel.speedx  = random.randrange(-20, 20, 5)
    if bagel.touches(left) or bagel.touches(right):
        bagel.speedx *= -1
        bagel.speedx  = random.randrange(-20, 20, 5)
    
    # If it glitches out of the window
    if bagel.x < -2 or bagel.x > 802:
        bagel.x = 400
    if bagel.y < -2 or bagel.y > 602:
        bagel.x = 300

    # Move Bagel Around
    bagel.x += bagel.speedx
    bagel.y += bagel.speedy

    camera.clear('black')
    camera.draw(background)
    keys.clear()
    camera.draw(gamebox.from_text(45, 15 , 'Score: {}'.format(bagel_score), 25, 'red', bold=True))
    camera.draw(bagel)
    camera.display()



ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)


