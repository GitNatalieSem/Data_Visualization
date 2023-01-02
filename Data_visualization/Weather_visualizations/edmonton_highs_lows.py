import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'gc.ca_data_for_Edmonton_2022.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[9])
            low = int(row[11])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            current_date = datetime.strptime(row[4], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[9])
            highs.append(high)
            low = int(row[11])
            lows.append(low)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.plot(dates, lows, c='blue')
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    print(ax.set)
    ax.set_title('Daily high and low temperatures - Edmonton 2022', fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (C)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# Find column number for each header
   # for index, column_header in enumerate(header_row):
   #     print(index, column_header)