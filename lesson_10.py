#1
import pandas as pd
import numpy as np
list_data = ['apple', 'banana', 'cherry']
np_array = np.array(list_data)
dict_data = {'fruit': list_data}
series_from_list = pd.Series(list_data)
dataframe_from_lists = pd.DataFrame([list_data])
series_from_np = pd.Series(np_array)
dataframe_from_np = pd.DataFrame(np_array.reshape(-1, len(np_array)))
series_from_dict = pd.Series(dict_data)
dataframe_from_dict = pd.DataFrame.from_dict(dict_data, orient='index').T
print(f'Series from list:\n{series_from_list}')
print(f'DataFrame from lists:\n{dataframe_from_lists}')
print(f'Series from NumPy array:\n{series_from_np}')
print(f'DataFrame from NumPy array:\n{dataframe_from_np}')
print(f'Series from dictionary:\n{series_from_dict}')
print(f'DataFrame from dictionary:\n{dataframe_from_dict}')

#2
import pandas as pd
series1 = pd.Series(['apple', 'banana', 'cherry'])
series2 = pd.Series(['banana', 'orange', 'grape'])
df = pd.DataFrame({
    'col1': ['apple', 'banana', 'cherry', 'pear'],
    'col2': ['banana', 'orange', 'grape', 'pear']
})
non_intersecting_elements_series = series1.symmetric_difference(series2)
non_intersecting_elements_columns = (
    set(df['col1']).symmetric_difference(set(df['col2']))
)
print("Непересекающиеся элементы в Series:")
print(non_intersecting_elements_series)
print("\nНепересекающиеся элементы в столбцах DataFrame:")
print(non_intersecting_elements_columns)

#3
import pandas as pd
import matplotlib.pyplot as plt
series = pd.Series(['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'apple'])
df = pd.DataFrame({
    'fruits': ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'apple'],
    'colors': ['red', 'yellow', 'green', 'blue', 'purple', 'black', 'white']
})
frequencies_series = series.value_counts()
frequencies_df_fruits = df['fruits'].value_counts()
frequencies_df_colors = df['colors'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(frequencies_series.index, frequencies_series.values)
plt.title('Frequency of Fruits in Series')
plt.xlabel('Fruits')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(8, 6))
plt.bar(frequencies_df_fruits.index, frequencies_df_fruits.values)
plt.title('Frequency of Fruits in DataFrame Column')
plt.xlabel('Fruits')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(8, 6))
plt.bar(frequencies_df_colors.index, frequencies_df_colors.values)
plt.title('Frequency of Colors in DataFrame Column')
plt.xlabel('Colors')
plt.ylabel('Frequency')
plt.show()

#4
import pandas as pd
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
df2 = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12]
})
vertical_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
horizontal_merge = pd.merge(df1, df2, left_index=True, right_index=True)
print("Вертикальное объединение:")
print(vertical_concat)
print("\nГоризонтальное объединение:")
print(horizontal_merge)

#5
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'x': range(1, 21),
    'y1': [i**2 for i in range(1, 21)],
    'y2': [i**3 for i in range(1, 21)]
})
fig, ax = plt.subplots()
ax.plot('x', 'y1', data=df, marker='o', label='y1')
ax.plot('x', 'y2', data=df, marker='^', label='y2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.grid(True)
plt.show()