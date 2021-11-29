import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)

# Bagel
bagel = gamebox.from_image(400, 300, "bagel.png")
bagel.size = [20,15]
# Borders
bottom = gamebox.from_color(400, 601, "white", 800, 1)
top = gamebox.from_color(400, -1, "white", 800, 1)
left = gamebox.from_color(-1, 300, "white", 1, 600)
right = gamebox.from_color(801, 300, 'white', 1, 600)


bagel.speedx = random.randrange(-10, 10)
bagel.speedy = random.randrange(-10, 10)
    


ticks = 0
bagel_score = 0

def tick(keys):
    global bagel_score
    # User interaction
    if (bagel.x - 20, bagel.y - 15) < (camera.mousex, camera.mousey) < (bagel.x + 20, bagel.y + 15) and camera.mouseclick:
        bagel_score += 1

    # Side Interactions
    if bagel.touches(bottom) or bagel.touches(top):
        bagel.speedy *= -1
    if bagel.touches(left) or bagel.touches(right):
        bagel.speedx *= -1
    

    # Move Bagel Around
    bagel.x += bagel.speedx
    bagel.y += bagel.speedy

    camera.clear('black')
    camera.draw(bagel)
    camera.display()



ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
