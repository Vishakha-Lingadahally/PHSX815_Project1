# PHSX815_Project1: How to run the code
On the command line, enter "python3.8 PHSX815_Project1.py" to run the simulations. Important: In the 87th line of the code, please change the path of the file where you want the data to be saved (of 1 isolated run), in the form of a .csv file. Make the same changes to line 89, in order for the code to read data from the saved file. Lines 85 to 93 save the data of a single random walk in the desired path and read the data from there to plot the track. Of course, the code also plots the track without saving it too. Therefore, one sees two plots of the tracks as output.

Here's how to interpret the outputs (details of which are elaborated in the project report):
1. The numbers: The numbers generated are the probabilities of obtaining heads when a coin is tossed thrice. It also gives an output of 'Heads' or 'Tails' after tossing the coin. We can also see the simulated and expected probabilities of obtaining 'Heads' during a coin-toss.
2. Plots: The first plot is that of a single run of the random walk. The second one is that of multiple runs plotted together (the number of times can be altered by altering the parameter n_simulations in line 84 of the code). The third one is just the second plot with the mean computed at each point.


