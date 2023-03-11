from dice import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

dice_1 = Dice()
dice_2 = Dice(10)

results = []
for roll_num in range(1_000_000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

#print(results)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of result'}
my_layout = Layout(title='Results of rolling a d6 and a d10 one million times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d10.html')