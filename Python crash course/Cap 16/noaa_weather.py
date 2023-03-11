import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'noaa.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headers = next(reader)
    for index, column_header in enumerate(headers):
        print(index, column_header) 

    lows, highs, dates = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%m/%d/%y")
        try:
            low = int(row[7])
            high = int(row[6])
        except ValueError:
            print(f'Values not found for date {current_date}')
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)
    

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, lows, c='blue')
ax.plot(dates, highs, c='red')
ax.set_title('miami temperature 2022')
ax.set_xlabel('date')
ax.set_ylabel('temperature')
plt.show()