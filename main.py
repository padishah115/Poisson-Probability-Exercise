import numpy as np
import matplotlib.pyplot as plt

N = 1000 #Number of time steps for testing the distribution. NOT THE NUMBER OF TRIALS
trials = 100
dt = 0.1

class Poisson:
    def __init__(self, nu):
        self.lmda = nu
        self.p_plus = nu*dt
        self.p_0 = 1 - nu*dt
        self.expectation = N*(nu*dt)
    
    def calculate_step(self):
        """Calculate whether a step is taken or not"""
        step = 0
        chance = np.random.random()
        if chance <= self.p_plus:
            step = 1

        return step

    def get_N_steps(self, num):
        """How many steps are taken over the time period"""
        steps = 0
        for i in range (num):
            steps += self.calculate_step()
        return steps
    
    def test_distribution(self, trials):
        final_steps = [] #Matrix for holding how many steps taken

        for i in range(trials): 
            #EACH TIME, TAKE N STEPS, BUT SIMULATE THIS OVER A CERTAIN NUMBER OF TRIALS
            x = self.get_N_steps(N)#TAKE N STEPS EACH TIME
            final_steps.append(x)

        print(final_steps)

        step_no = []
        freq = []

        for a in final_steps:
            counted_num = []
            if a not in counted_num:
                step_no.append(a)
                freq.append(final_steps.count(a))
                counted_num.append(a)
        
        mean = np.mean(step_no)

        plt.bar(step_no, freq)
        plt.title(f'Expectation value: {self.expectation:.2f}. Observed mean: {mean}')
        plt.show()



myPoisson = Poisson(0.5)
myPoisson2 = Poisson(0.1)
myPoisson.test_distribution(trials)
myPoisson2.test_distribution(trials)

