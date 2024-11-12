import matplotlib.pyplot as plt
from random import choice
%matplotlib inline
plt.rc('figure', figsize=(12, 6))

def rand_walk(steps):
    walk = []  # Start from the origin and include it in the walk
    step_1 = choice([-1, 1])
    walk.append(step_1)
    for i in range(1, steps):
        step = choice([-1, 1])  # Choose either -1 or 1 randomly
        position = walk[i-1] + step
        walk.append(position)
    
    return walk

def plot_walks(num, walk_steps):
    lab_list = list(range(1, num + 1))
    for i in range(num): 
        x = list(range(1, walk_steps + 1))
        plt.plot(x, rand_walk(walk_steps), label ='Plot Number ' + str(lab_list[i]))
        
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.title('Our Random Walk')
    plt.legend(loc='lower left')
    plt.show()

# Example usage
plot_walks(3, 1000)
