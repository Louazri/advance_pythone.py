import matplotlib.pyplot as plt
from random import choice
%matplotlib inline
plt.rc('figure', figsize=(16, 16))

def trans_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1,y1

def trans_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x+ 0.5
    y1 = 0.5 * y + 0.5
    return x1,y1

def trans_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y 
    return x1,y1

# List of transformation functions
transformation = [trans_1, trans_2, trans_3]

# Initialize lists to store the points
a1 = [0]
b1 = [0]
a, b = 0, 0  # Starting point

# Generate points using the transformations
for i in range(5000000):  # Increased the number of iterations
    trans = choice(transformation)
    a, b = trans((a, b))
    a1.append(a)
    b1.append(b)

# Plot the generated points
plt.plot(a1, b1, 'o', markersize=0.5)  # Smaller markers for clearer pattern
plt.title("Sierpiński Triangle (Generated with Transformations)")
plt.show()
