  #Import the Pygame Zero Library
import pgzrun
from random import random

TITLE = "Good shot"

WDITH = 500
HEIGHT = 500

message = ""

alien = Actor('Alien.png')
def draw():
  # screen is another built-in object
    screen.clear()
    screen.fill(color = (128, 0, 0))
  # place_alien()
    alien.draw()
    screen.draw.text(message, center = (400, 10), fontsize = 30)    

def place_alien():
   alien.x = randint(50, WIDTH-50)
   alien.y = randint(50, WIDTH-50)

def on_mouse_down(pos):
   global message
   if alien.dollidepoint(pos):
      message = "Good shot"
      place_alien()
   else:
      message = "You missed"   
    
place_alien()
pgzrun.go()
   

