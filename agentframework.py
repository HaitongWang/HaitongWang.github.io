# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:14:32 2017

@author: ml16h2w
"""
import random

agents = []
agents.append([random.randint(0,99),random.randint(0,99)])

class Agent:
    def __init__ (self,x,y):
            self.x = random.randint(0,99)
            self.y = random.randint(0,99)
    def move (self,x,y):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y + 1) % 100 
        

def distance_between(agent0:Agent, agent1:Agent): 
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5        