import pandas as pd
import numpy as np

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])

# print(totals)
row_total_sum = totals.sum(axis=1)
print("City with lowest total precipitation:")
print(row_total_sum.idxmin())

# part B
mean_df = totals.mean()
mean_df1 = counts.mean()
print("Average precipitation in each month:")
print(mean_df/mean_df1)

# part C
row_count_sum = counts.sum(axis=1)
daily_avg_city_precipitation = (row_total_sum / row_count_sum)
print("Average precipitation in each city:")
print(daily_avg_city_precipitation)


