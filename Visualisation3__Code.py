import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df =pd.read_csv('file_clean.csv',index_col=0)
res_count=df.groupby(['Results']).size().reset_index(name='count')
print(res_count)
nparray_count=res_count['count'].values
list_count=np.array(nparray_count).tolist()
nparray_res=res_count['Results'].values
list_res=np.array(nparray_res).tolist()
plt.pie(list_count,labels=list_res,autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Pie chart showing Results summary from year 2010 - 2017')
plt.show()
