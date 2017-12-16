# -*- coding: utf-8 -*-
"""
Spyder Editor

by Haitong Wang
"""
import matplotlib.pyplot 
import operator
import random

num_of_agents = 10
num_of_iterations = 100
agents = []

# Set up first pair of variables.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Random walk one step.(y0,x0)

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

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

matplotlib.pyplot.show()