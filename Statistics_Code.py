import pandas as pd
df =pd.read_csv('file_clean.csv',index_col=0)


def maxrisk(l):
    #count = 0
    d = dict()
    for data in l:
        if data not in d:
            d[data] = 1
        else:
            d[data] = d[data] + 1
    print(d)
	
    lst = list(d.keys())
    print(lst)
    lst.sort()
    for key in lst:
        print(key, d[key]) 
    return maxrisk
num1 = maxrisk(df['Risk'])
#print('Total Summary of risk',num1 )

mean_risk = df['Risk'].mean()
print(mean_risk)

print(df['Risk'].describe())

