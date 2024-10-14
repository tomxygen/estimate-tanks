# DEFINITIONS

# before performing the experiment, a number of batches is defined, as well as the number of draws for each batch. 
# then, the number or trials is defined. The same number is applied to each batch.

# batches: how many different runs we want to perform.
# draws: how many tanks are drawn for every batch. The higher, the more accurate the predicted value will be .
# trials: how many times the experiment on the same batch is performed by extracting a new batch of random tanks.
#         the more tanks in the batch, the less variability is expected in the predicted value.


import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib
#import pandas as pd


# number of drawn tanks for each batch. Initialize the list
n_of_draws = []


# user input defines the number of tanks for each batch and subsequelty the number of batches. User is asked to add each batch. When is done, type 'stop'
print("Add the number of tanks of each batch. When done, type 'stop' to proceed")
i = 1
while True: 
    temp_input = input(f"Number of tanks of the {i} batch: ")
    if temp_input == 'stop':
        break
    elif temp_input == 'default':
        n_of_draws = [2,5,10,20]
        break
    n_of_draws.append(int(temp_input))
    i+=1
print("\n")


# number of trials (how many times the random tank selection is performed) 
print("Add the number of times each experiment is performed")
print("Default = 100")
temp_input = input("Number of expeirments: ")
if temp_input == '':
    n_of_trials = 100
else:
    n_of_trials = int(temp_input)
print(f"Number of trials: {n_of_trials}")
print("\n")


# total number of tanks
print("Add the total number tanks that needs to be guessed")
print("Default = 200000")
temp_input = input("Number of tanks: ")
if temp_input == '':
    n_of_tanks = 200000
else:
    n_of_tanks = int(temp_input)
print(f"Number of tanks: {n_of_tanks}")
print("\n")


print(f"The experiment is performed on {len(n_of_draws)} batches.")
print(f"Each experiment is performed {n_of_trials} times.")
print(f"On the following batches: {n_of_draws}.\n")






dictResult = {}


# draw the random tanks. The function expects two parameters: 
# tanks -> total number of tanks produced among which the random selected are the ones destroied
# sample -> sample size of each batch, defined in the list n_of_draws
# the function returns a list of #sample integer numbers from 1 to tanks which represents one destroied tank.
def random_tank_generation(tanks, sample):
    random_tanks = np.random.randint(1,tanks,sample)
    return random_tanks

# estimate the number of tanks. The function expects two parameters:
# maximum -> is the highest number of each batch among the n_of_trials drawn
# sample -> sample size of each batch, defined in the list n_of_draws
# the function returns the estimate total number of tanks produced.
def tank_number_estimation(maximum, sample):
    ext_number_of_tanks = maximum + (maximum-sample)/sample
    return ext_number_of_tanks



for draw in n_of_draws: #this loops in the list of batches
    dictResult[f"drawn tanks: {draw}"] = [] #declare the result dictionary
    #now we need to extract 5 random numbers and put them in a list, for 300 times
    for trial in range(n_of_trials):
        generated_random_tanks = random_tank_generation(n_of_tanks, draw)
        max = generated_random_tanks.max()
        dictResult[f"drawn tanks: {draw}"].append(tank_number_estimation(max, draw))

stdList = []

for draw in n_of_draws:
    print(f"Batch {n_of_draws.index(draw)+1} with {draw} drawn tanks:")
    print("->average: ", np.mean(dictResult[f"drawn tanks: {draw}"]))
    print("->standard deviation: ", np.std(dictResult[f"drawn tanks: {draw}"]))
    print("->off by ", abs(np.mean(dictResult[f"drawn tanks: {draw}"])-n_of_tanks), "(",abs(np.mean(dictResult[f"drawn tanks: {draw}"])-n_of_tanks)/n_of_tanks*100,"% )")
    print("\n")
    stdList.append(np.std(dictResult[f"drawn tanks: {draw}"]))


matplotlib.pyplot.axhline(y=n_of_tanks, linewidth=1, color='black')#, ls=':')
sns.set_style('darkgrid')
sns.lineplot(dictResult)
plt.show()

sns.lineplot(stdList)    
plt.show()




    