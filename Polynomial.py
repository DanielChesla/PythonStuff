#!/usr/bin/env python
# coding: utf-8

# In[13]:


import matplotlib.pyplot as plt

# Define the polynomial function
def polynomial(x):
    return x**3 - 3*x**2 + 2*x + 1

# Generate x values
x_values = [i for i in range(-10, 10)]  # Generating values from -2 to 4 in steps of 0.1

# Compute y values
y_values = [polynomial(x) for x in x_values]

# Plot the polynomial
plt.figure(figsize=(10, 10))
plt.plot(x_values, y_values, label='y = x^3 - 3x^2 + 2x + 1', color='red')
plt.title('Plot of the Polynomial y = x^3 - 3x^2 + 2x + 1')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)
plt.grid(True, which='both', linestyle='--', linewidth=1)
plt.legend()
plt.show()


# In[ ]:




