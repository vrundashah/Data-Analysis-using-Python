import pandas as pd
#import pylab as plt
import matplotlib
import matplotlib.pyplot as plt
df =pd.read_csv('file_clean.csv',index_col=0)
matplotlib.style.use('seaborn-dark-palette') # plot style
df.hist(column='Risk',edgecolor='black', bins = 3) #color and column
plt.xlabel('Risk Value') #xaxis label
plt.ylabel('Total insidents with risk value') #yaxis label
plt.suptitle('Frequency Distribution of Average Risk for Food Inspection from 2010 - 2017', ha='center')
