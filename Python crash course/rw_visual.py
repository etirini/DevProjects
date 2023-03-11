import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(15,9))
    
    point_numbers = range(rw.num_points)
    
    ax.plot(rw.x_values, rw.y_values)

    #abajo el ej. original con Scatter. Arriba el ej. modificado con plot
    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    #ax.scatter(0,0, c='purple', edgecolors='none', s=15)
    #ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=15)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()

    keep_running = input('Run another plot? ')
    if keep_running == 'n':
        break
    