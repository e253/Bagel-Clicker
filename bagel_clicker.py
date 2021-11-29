import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)

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
    keys.clear()
    camera.draw(gamebox.from_text(45, 15 , 'Score: {}'.format(bagel_score), 25, 'red', bold=True))
    camera.draw(bagel)
    camera.display()



ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
