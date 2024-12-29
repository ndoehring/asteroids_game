import pygame
import random
from circleshape import *
from constants import *
from player import *

class Asteroid(CircleShape):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        neg_random_angle = -1 * random_angle
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity_1 = 1.2 * (self.velocity.rotate(random_angle))
        velocity_2 = 1.2 * (self.velocity.rotate(neg_random_angle))
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = velocity_1
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = velocity_2



        