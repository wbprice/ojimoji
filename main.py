#!/usr/bin/env python

# Adapted from @tanurai's "Be Still, My Beating Heart"
# https://learn.pimoroni.com/tutorial/tanya/be-still-my-beating-heart

from unicorn_hat_sim import unicornhathd as unicorn

import time, colorsys

from emoji import list

unicorn.brightness(1)
unicorn.rotation(270)

for emoji in list:
  for y in range(16):
    for x in range(16):
      h = emoji.h
      s = emoji.s
      v = emoji.bitmap[x,y]
      rgb = colorsys.hsv_to_rgb(h, s, v) 
      r = int(rgb[0]*255.0) 
      g = int(rgb[1]*255.0)
      b = int(rgb[2]*255.0)
      unicorn.set_pixel(x, y, r, g, b) 
    unicorn.show() 
    time.sleep(0.005)
  time.sleep(10)

