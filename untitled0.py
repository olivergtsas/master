import random
import matplotlib.pyplot as plt
import math

# Parameters
list_size = 4  # Adjust this value as needed
min_value = 1   # Minimum value for the integers
max_value = 100 # Maximum value for the integers
num_simulations = 10000000  # Number of simulations

# Simulate and collect data
last_elements = []
for _ in range(num_simulations):
    random_list = random.sample(range(min_value, max_value + 1), list_size)
    random_list.sort()
    last_elements.append(random_list[-1])

# Plotting the histogram
hist_values, bin_edges, _ = plt.hist(last_elements, bins=range(min_value, max_value + 2), density=True, edgecolor='black')

# Calculate probability function
x_values = range(min_value, max_value + 1)
prob_function = [(math.comb(x-1, list_size - 1) / math.comb(max_value, list_size)) for x in x_values]

# Plotting the probability function
plt.plot(x_values, prob_function, color='red', label='Probability Function')

# Setting labels and title
plt.xlabel('Last Element')
plt.ylabel('Probability')
plt.title('Empirical Probability Distribution of Last Element with Probability Function')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()




