import pygame
import time
import random
# initialize pygame
pygame.init()

#Screen size
width = 600
height = 400
screen = pygame.display.set_model((width,height))
pygame.display.set_caption("Snake Game")

#colors
white = (255,255,255)
black