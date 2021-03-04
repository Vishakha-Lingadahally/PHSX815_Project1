# PHSX815_Project1: How to run the code
On the command line, enter "python 'path/Random_walk.py'" to run the simulations.
Here's how to interpret the outputs:
1. The numbers: The numbers generated are the probabilities of obtaining heads when a coin is tossed thrice. It also gives an output of 'Heads' or 'Tails' after tossing the coin. We can also see the simulated and expected probabilities of obtaining 'Heads' during a coin-toss.
2. Plots: The first plot is that of a single run of the random walk. The second one is that of multiple runs plotted together (the number of times can be altered by altering the parameter n_simulations in line 84 of the code). The third one is just the second plot with the mean computed at each point.
On the command line, enter "python 'path/Random_walk.py'" output > random_walk.txt. This will save the output of the sample (single trial) in a text file.
I'm still working on the part of the code that can analyse data from a text file. I will update the code as soon as I figure it out.
