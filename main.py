import pygame as p
import time
import random
import math
import sys

s = p.display.set_mode((600,600))
r = 10
x = random.randint(0,600)
y = random.randint(0,600)
shetchik = 0
b = 0

while True:
p.draw.rect(s,(255,255,255),(0,0,600,600))
p.draw.circle(s,(0,255,0),(x,y), r)
p.display.update()
time.sleep(0.01)
shetchik = shetchik+1

while True:
p.draw.rect(s,(255,255,255),(0,0,600,600))
p.draw.square(s,(0,255,0),(x,y), r)
p.display.update()
time.sleep(0.01)
shetchik = shetchik-shetchik

if shetchik > 150:
p.quit()
sys.exit()

for i in p.event.get():
if i.type == p.MOUSEBUTTONDOWN:

mx, my = i.pos
dist = math.sqrt((x-mx)**2 + (y-my)**2)

if dist<=r:
x = random.randint(0,600)
y = random.randint(0,600)
shetchik=0
b=b+1
print(b)
else:
p.quit()
sys.exit()
