import matplotlib.pyplot as plt
plt.style.use('ggplot')
fig, ax = plt.subplots()

x_values = range(1,100)
y_values = [x**2 for x in x_values]

ax.scatter(x_values, y_values)

plt.show()