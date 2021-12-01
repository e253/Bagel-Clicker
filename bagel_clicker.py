### TODO ####
# 1. Have the bagel spin so that it counts as being animated in grading




import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

# Kitchen Background
background = gamebox.from_image(400, 300, "kitchen-background.png")
background.size = [800, 600]
# Bagel
bagel_sheet = gamebox.load_sprite_sheet("bagel_sheet.png", 4, 4)
bagel_ind = 0
bagel = gamebox.from_image(400, 300, bagel_sheet[bagel_ind])
bagel.size = [20, 15]
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
    bagel.speedx = random.randrange(-20, 20, 5)
    bagel.speedy = random.randrange(-20, 20, 5)

def reset_timer():
    global time
    time = 200

def game_over_function():
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
    global mouse_on
    global bagel_score
    global start
    global game_over
    global time
    global Level
    global have_to_make
    global bagel_ind

    #Start screen
    if not start:
        camera.clear('black')
        camera.draw(gamebox.from_text(400, 100, "Bagel Clicker", 72, "blue"))
        camera.draw(gamebox.from_text(400, 150, "Made by: Ethan Steere (xaq5rz) and Emilie Neulen (ean4tp)", 30, "blue"))
        camera.draw(gamebox.from_text(400, 300, "Instructions:", 40, "red"))
        camera.draw(gamebox.from_text(400, 350, "Bodo's needs help finishing all their catering orders!", 20, "red"))
        camera.draw(gamebox.from_text(400, 400, "Click on the moving bagel to make a bagel, and make as many as needed before the time runs out.", 20, "red"))
        camera.draw(gamebox.from_text(400, 500, "Press Space to start", 50, "blue"))
        camera.display()
        if pygame.K_SPACE in keys:
            start = True

    # User interaction
    if start:
        if not game_over:
            if not camera.mouseclick:
                mouse_on = False
                bagel.size = [20, 15]
            if (bagel.x - 20, bagel.y - 15) < (camera.mousex, camera.mousey) < (
                bagel.x + 20, bagel.y + 15) and camera.mouseclick and not mouse_on:
                bagel_score += 1
                bagel.size = [40, 30]
                mouse_on = True

    # Resets Speeds every 2 seconds
            if ticks % 60:
                average_speed = two_total / 60
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
            camera.draw(background)
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
