import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_angle = random.uniform(20, 50)
        asteroid_split_speed = 1.2

        splits = 2
        children = []
        for i in range(0,splits):
            children.append(Asteroid(self.position.x, self.position.y, new_radius))
        
        children[0].velocity = self.velocity.rotate(split_angle) * asteroid_split_speed
        children[1].velocity = self.velocity.rotate(-split_angle) * asteroid_split_speed

