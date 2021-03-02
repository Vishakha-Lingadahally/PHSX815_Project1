#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:35:32 2021

@author: vishakha
"""
import numpy as np

# For plotting
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('notebook')

import pandas as pd

flip_1 = np.random.rand()
flip_2 = np.random.rand()
flip_3 = np.random.rand()
print(flip_1, flip_2, flip_3)

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
#print('Predicted p = %s. Simulated p = %s.' %(p, p_sim))

# Define our step probability and number of steps.
step_prob = 0.5  # Can step left or right equally.
n_steps = 1000   # Essentially time.

# Set up a vector to store our positions. 
position = np.zeros(n_steps)  # Full of zeros.

# Loop through each time step.
for i in range(1, n_steps):
    # Flip a coin.
    flip = np.random.rand()
    
    # Figure out which way we should step.
    if flip < step_prob:
        step = -1  # To the 'left'.
    else:
        step = 1  # to the 'right'.
        
    # Update our position based on where we were in the last time point. 
    position[i] = position[i-1] + step

# Make a vector of time points.
steps = np.arange(0, n_steps, 1)  # Arange from 0 to n_steps taking intervals of 1.
 
d={'steps':np.array(steps), 'position':np.array(position)}
df=pd.DataFrame(d)
print(df)

#print(steps)
#print(position)
# Plot it!
plt.plot(steps, position)
plt.xlabel('Number of steps')
plt.ylabel('Position')
plt.show()

