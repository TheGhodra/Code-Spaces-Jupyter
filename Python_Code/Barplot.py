from matplotlib import pyplot as plt
import pandas as pd


df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'A',
 'B', 'B', 'B', 'B', 'B',
 'C', 'C', 'C', 'C', 'C'],
 'points': [12, 29, 34, 14, 10, 11, 7,
36,
 34, 22, 41, 40, 45, 36,
38]})

grouped = df.groupby('team')['points'].sum()


grouped.plot.bar()
plt.show()
