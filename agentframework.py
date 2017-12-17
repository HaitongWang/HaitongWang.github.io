# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:14:32 2017

@author: ml16h2w
"""
import random


class Agent:
        
    def __init__(self,x,y,environment,store):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)   
        self.environment = environment
        self.store = 0
 
    def move (self):
        if random.random() < 0.5:
            self.x = (int(self.x) + 1) % 100
        else:
            self.x = (int(self.x) - 1) % 100

        if random.random() < 0.5:
            self.y = (int(self.y) + 1) % 100
        else:
            self.y = (int(self.y) + 1) % 100 
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        

def distance_between(agent0:Agent, agent1:Agent): 
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5        