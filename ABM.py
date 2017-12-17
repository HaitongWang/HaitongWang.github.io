# -*- coding: utf-8 -*-
"""
Spyder Editor

by Haitong Wang
"""
import matplotlib.pyplot 
import operator
import random
import agentframework

def distance_between(agent0, agent1): 
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Set up agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Random walk agents.(y0,x0)
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        agents[i].move()

      
print (agents) 



distance = distance_between(agents[0], agents[1])
print(distance)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


a = agentframework.Agent()  
print(a.y, a.x)