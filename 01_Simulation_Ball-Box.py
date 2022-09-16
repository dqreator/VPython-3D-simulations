#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# 
# This script simulates a ball inside of a box changing its velocity,
# and color depending on the wall that collides. 
#
# 2019 David Quezada, Krakow, Poland
# email [dqreator@gmail.com]
# -----------------------------------------------------------

from vpython import *
import random

# Definition of the canvas 
scene = canvas(width=600, height=600)

# Definition of the walls 
wall_left   = box(pos=vec(-3.55, 0, 0), size=vector(0.3, 7, 7), color=color.red)
wall_rigth  = box(pos=vec(3.55, 0, 0), size=vector(0.3, 7, 7), color=color.green)
wall_up     = box(pos=vec(0, 3.55, 0), size=vector(7, 0.3, 7), color=color.blue)
wall_down   = box(pos=vec(0, -3.55, 0), size=vector(7, 0.3, 7), color=color.yellow)
wall_back   = box(pos=vec(0, 0, -3.55), size=vector(7, 7, 0.3), color=color.magenta)

# Definition of the ball 
ball = sphere(pos=vec(0, 0, 0), radius=0.5)

# Definition of a random initial velocity of the ball 
ball_initial_vel = {"x": random.random(), "y": random.random(), "z": random.random()}
ball.vel         = vector(ball_initial_vel["x"], ball_initial_vel["y"], ball_initial_vel["z"])

# Initialize time
t  = 0
# Define time step
dt = 0.005

# Main loop 
while t<500:
    rate(1000)
    # Update the position of the ball 
    ball.pos = ball.pos + ball.vel*dt
    """Identifies if the ball colides with any of the walls,
     takes the color of the wall which collided and
     invert the direction of the velocity."""

    # Check rigth and left
    if abs(ball.pos.x) >= wall_rigth.pos.x-ball.radius:
        # Inverts velocity 
        ball.vel.x = -ball.vel.x
        # Changes color
        if ball.pos.x >0:
            ball.color= wall_rigth.color
        else:
            ball.color = wall_left.color
    # Check up and down 
    if abs(ball.pos.y) >= wall_up.pos.y-ball.radius:
        # Inverts velocity 
        ball.vel.y=-ball.vel.y 
        # Changes color          
        if ball.pos.y >0:
            ball.color= wall_up.color
        else:
            ball.color = wall_down.color 
    # Check back and front 
    if abs(ball.pos.z) >= (-wall_back.pos.z-ball.radius):
        # Inverts velocity
        ball.vel.z = -ball.vel.z
        # Changes color
        if ball.pos.z >0:
            ball.color = color.white
        else:
            ball.color=wall_back.color
    # Increases time by dt
    t=t+dt