import numpy as np
import matplotlib.pyplot as plt

#? Online sources:
#? https://www.youtube.com/watch?v=slbZ-SLpIgg
#? https://www.youtube.com/watch?v=7TqhmX92P6U
#?
#? To lookup:
#? https://www.youtube.com/watch?v=wKdmEXCvo9s 
#?

#! First simulate random outcomes between two set ranges
"""#!--- Three steps:
        1) Setup the predictive model
            - identifying the dependant variable to be predicted
            - identifying the independant variables (input risk of predictive variables)
        2) Specify the probability distribution and assign probability weights for each
            - define a range of likely values
                - historical data or
                - subjective values
        3) Run repeated simulations to generate random values of the independant variables
"""

sims = 1000000  # Number of simulations to run

A = np.random.uniform(1, 5, sims)
B = np.random.uniform(2, 6, sims)

duration = A + B
# print(duration)

plt.figure(figsize = (10, 5))
plt.hist(duration, density = True)
plt.axvline(9, color = 'r')
plt.show()
print((duration > 9).sum()/sims)