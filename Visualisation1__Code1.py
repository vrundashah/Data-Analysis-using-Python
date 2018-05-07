import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
df = pd.read_csv('dict1.csv')
top10 = df.sort_values('Total',ascending = 0).head(10)[['Inspect1','Total']]
plt.rcParams['figure.figsize']=(15,10)
matplotlib.style.use('ggplot')
ax=top10.plot.bar(x='Inspect1', y='Total',title='Top 10 Inspections')