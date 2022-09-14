import numpy as np

# part 1
data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']

sum_across_rows = np.sum(totals, axis=1)

lowest_precipitation = np.argmin(sum_across_rows, axis=None, out=None)
print("Row with lowest total precipitation:")
print(lowest_precipitation)

# part 2
total_columns_sum = np.sum(totals, axis=0)  # total precipitation for each month(axis 0)
counts_columns_sum = np.sum(counts, axis=0)  # total observation for the month

avg_precipitation = total_columns_sum / counts_columns_sum
print("Average precipitation in each month:")
print(avg_precipitation)

# part 3
totals_rows_sum = np.sum(totals, axis=1)
counts_rows_sum = np.sum(counts, axis=1)

daily_Avg_city_precipitation = totals_rows_sum / counts_rows_sum
print("Average precipitation in each city:")
print(daily_Avg_city_precipitation)

# Part 4
# numpy.reshape(array, newshape, order='C')
reshaped_quarterly = totals.reshape((4 * (totals.shape[0]), 3))
quarter_sum = np.sum(reshaped_quarterly, axis=1)
quarter_sum = quarter_sum.reshape(((totals.shape[0]), 4))
print("Quarterly precipitation totals:")
print(quarter_sum)
