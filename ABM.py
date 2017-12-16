# -*- coding: utf-8 -*-
"""
Spyder Editor

by Haitong Wang
"""
import matplotlib.pyplot 
import operator
import random

def distance_between(agent0, agent1): 
    return (((agent0[0] - agent1[0])**2) + ((agent0[1] - agent1[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Set up agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Random walk agents.(y0,x0)
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] + 1) % 100 
        
print (agents) 


print (max(agents, key=operator.itemgetter(1)))

distance = distance_between(agents[0], agents[1])
print(distance)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

matplotlib.pyplot.show()
