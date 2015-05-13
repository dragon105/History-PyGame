import pygame
import helperfunctions

class Enemy:
    location = helperfunctions.PVector(0, 0)
    velocity = helperfunctions.PVector(0, 0)
    health = 100
    image = '' #TODO: put 'enemy' sprite here
