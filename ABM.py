# -*- coding: utf-8 -*-
"""
Spyder Editor

by Haitong Wang
"""
import matplotlib.pyplot 
import operator
import random
import agentframework
import csv

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []  #Lines here happen before any data is processed
for row in reader:
    rowlist = []  #Lines here happen before each row is processed
    for values in row:
        rowlist.append(values)  #do something with values
    environment.append(rowlist)  #Lines here happen after row is processed
f.close()      

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


for agent0 in agents:
     for agent1 in agents:
         distance = distance_between(agent0, agent1)
distance = distance_between(agents[0], agents[1])
print(distance)



matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


a = agentframework.Agent()  
print(a.y, a.x)