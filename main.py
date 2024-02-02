import numpy as np
import matplotlib.pyplot as plt

N = 1000 #Number of time slices for testing the distribution.
tests = 500 #Number of times we run each distribution
dt = 0.1

class Poisson:
    def __init__(self, name, nu):
        self.name = name
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

    def try_N_times(self, num):
        """How many steps are taken over the time period"""
        steps = 0
        for i in range (num):
            steps += self.calculate_step()
        return steps #Number of steps taken in N time slices
    
    def visualise_distribution(self, tests):
        """Runs each distribution a TESTS number of times, over N time steps, then plots variable k (number of successes) vs frequency of k"""
        final_steps = [] #Matrix for holding how many steps taken

        for i in range(tests): 
            #EACH TIME, TAKE N STEPS, BUT SIMULATE THIS OVER A CERTAIN NUMBER OF TESTS
            x = self.try_N_times(N)#TAKE N time slices and see how many steps are taken each time
            final_steps.append(x)

        #print(final_steps)

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


def test_distributions(k_values, tests, distributions):
    """Test multiple Poisson distributions and plot the frequency of no. of successes
    #Axes is a linear space describing the range of k values we investigate
    #Tests is the number of times we run each distribution
    #Distributions is an array of however many Poisson distributions we want to run
    """

    distribution_steps = {} #Dictionary holding the name of each distribution and the final step number of each test for each distribution.
    #Eg:
    """
    distribution_steps = {
        'lamba=0.1': [56, 23, 33,...]
        'lambda=0.3': [60, 102, 110]
        ...
    }
    
    """

    for poisson in distributions:
        final_steps = [] #Each time we run the distribution, and we run it a TESTS number of times
        freq = np.zeros_like(k_values)

        for i in range(tests): 
            #EACH TIME, TAKE N STEPS, BUT SIMULATE THIS OVER A CERTAIN NUMBER OF TESTS
            x = poisson.try_N_times(N)#TAKE N STEPS EACH TIME
            final_steps.append(x)
        
        distribution_steps[f'{poisson.name}'] = final_steps

        for step in final_steps:
            if step in k_values:
                freq[step] += 1
        
        #Plot a graph for each distribution, frequency(k) vs k along x-axis
        plt.scatter(k_values, freq, label = f'{poisson.name}', s=2)
        plt.plot(k_values, freq)

    #Overall graph
    plt.xlabel('k')
    plt.ylabel('frequency')
    plt.title(f'Successes against success number, k, for different poisson distributions over {N} time steps')
    plt.legend()
    plt.show()
    
    #return distribution_steps


x = np.arange(int(1.5*N*dt)) #The extremal number of successes in N*dt time is equal to N*dt (i.e. a Poisson process with lambda = 1) 
#so let this define the far edge of our axis


#Initialise three distributions (or more!)
myPoisson = Poisson('lambda = 0.5', 0.5)
myPoisson2 = Poisson('lamba = 0.1', 0.1)
myPoisson3 = Poisson('lamda = 0.9', 0.9)


#Let's try and see what a single distribution looks like.
myPoisson.visualise_distribution(tests)
#myPoisson2.visualise_distribution(tests)

print(test_distributions(x, tests, [myPoisson, myPoisson2, myPoisson3]))
