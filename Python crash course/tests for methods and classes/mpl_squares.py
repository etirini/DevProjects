import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
input_values = [1,2,3,4,5]
plt.style.use('ggplot')

fig, ax  = plt.subplots()
ax.plot(input_values, squares)
ax.set_title('square numbers')
ax.set_xlabel('value')
ax.set_ylabel('Square of value')

""" 
ax.tick_params(axis='both', labelsize=14)
"""

plt.show()


