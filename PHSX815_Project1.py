#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:35:42 2021

@author: vishakha
"""
import numpy as np
import math

# For plotting
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('notebook')

# Importing pandas
import pandas as pd
from scipy.stats.distributions import chi2
# Begin by flipping coins

flip_1 = np.random.rand()
flip_2 = np.random.rand()
flip_3 = np.random.rand()
print('The resultant probabilities are %s, %s and %s' %(flip_1, flip_2, flip_3))

print('The results of the flips are:')
flips = [flip_1, flip_2, flip_3]
for flip in flips:
    if flip < 0.5:
        print("Heads")
    else: 
        print("Tails")
        
        
        
# Test if our coin flipping algorithm is fair.
n_flips = 1000
p = 0.5  # Our expected probability of a heads.

# Flip the coin n_flips times.
flips = np.random.rand(n_flips)

# Compute the number of heads.
heads_or_tails = flips < p  # Will result in a True (1.0) if heads.
n_heads = np.sum(heads_or_tails)  # Gives the total number of heads.

# Compute the probability of a heads in our simulation.
p_sim = n_heads / n_flips
print('Predicted probability = %s. Simulated probability = %s.' %(p, p_sim))

# Define our step probability and number of steps.

# Hypothesis 1:

step_prob = 0.5  # Can step left or right equally.
n_steps = 100 # Essentially number of steps.

    
# Set up a vector to store our positions.

position = np.zeros(n_steps)

# Loop through each time step.
for i in range(1, n_steps):
    # Flip a coin.
    flip = np.random.rand()
    
    # Figure out which way we should step.
    if flip < step_prob:
        step = -1 # To the 'left'.
    else:
        step = 1# to the 'right'.
        
    # Update our position based on where we were in the last time point. 
    position[i] = position[i-1] + step
    
#print(position[i])

# Number of steps taken to the left in our first hypothesis
nl=int((n_steps-position[i])/2)
print("The number of steps taken to the left is %s.Therefore, the number of steps taken to the right is %s." %(nl, (n_steps-nl)))
# Make a vector of time points.
steps = np.arange(0, n_steps, 1)  # Arange from 0 to n_steps taking intervals of 1.
 
d={'#steps':np.array(steps), '#position':np.array(position)}
df=pd.DataFrame(d)
df.to_csv(r'/home/vishakha/Documents/python/random_walk.csv', index = False)

# Likelihood for binomial distribution

P=(((math.factorial(n_steps))*((step_prob)**(n_steps-nl))*((1-step_prob)**(nl)))/((math.factorial(nl))*(math.factorial(n_steps-nl))))
#P=np.log(((math.factorial(n_steps))*((step_prob)**(100-nl))*((1-step_prob)**(nl)))/(((math.factorial(nl)))*(math.factorial(100-nl))))
print("The likelihood for our hyposthesis is %s" %(P))
#print(steps)
#print(position)
# Plot it!
plt.plot(steps, position)
plt.xlabel('Number of steps')
plt.ylabel('Position')
plt.show()



# Make a vector of time points.



# Perform the random walk multiple times. 
n_simulations = 1000

# Make a new position vector. This will include all simulations.
position = np.zeros((n_simulations, n_steps))


# Redefine our step probabilities just to be clear. 
step_prob = 0.5


# Loop through each simulation.
for i in range(n_simulations):
    # Loop through each step. 

    for j in range(1, n_steps):
        # Flip a coin.
        flip = np.random.rand()
        
        # Figure out how to step.
        if flip < step_prob:
            step = -1
        else:
            step = 1
            
        # Update our position.
        position[i, j] = position[i, j-1] + step
    
        
# Plot all of the trajectories together.
for i in range(n_simulations):
    # Remembering that `position` is just a two-dimensional matrix that is 
    # n_simulations by n_steps, we can get each step for a given simulation 
    # by indexing as position[i, :].
    plt.plot(steps, position[i, :], linewidth=1, alpha=1) 
    
# Add axis labels.
plt.xlabel('Number of steps')
plt.ylabel('Position')
plt.show()


# Compute the mean position at each step. 
mean_position = np.zeros(n_steps)
for i in range(n_steps):
    mean_position[i] = np.mean(position[:, i])

# Plot all of the simulations.
for i in range(n_simulations):
    plt.plot(steps, position[i, :], linewidth=1, alpha=1)
    
# Plot the mean as a thick red line. 
plt.plot(steps, mean_position, 'b-')

# Add the labels.
plt.xlabel('Number of steps')
plt.ylabel('Position')
plt.show()
