import matplotlib.pyplot as plt 

x_values = range(1, 100)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=50)

ax.set_title('El plot de tu vieja')
ax.set_xlabel('numero')
ax.set_ylabel('raiz cuadrada')
ax.axis([0, 100, 0, 10000])
plt.show()
#plt.savefig('tuplot.png', bbox_inches='tight')
