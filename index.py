import pandas as pd
import matplotlib.pyplot as plt
import sys

#load data
general = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/all%20billing%20data.csv')
general['Cost'] = round(general['Cost'], 2)
genpct = general.copy()

#data manipulation
totalspending = genpct['Cost'].sum()

for i in genpct.index:
    genpct.loc[i, 'Cost'] /= totalspending

genpct['Cost'] = round(genpct['Cost'], 4)*100

#report headers
genheader = ('CTA Utility Spending Since 2024')
pctheader = ('Utility Spending Percentages Since 2024')

def drawline(str):
    var = len(str)
    for i in range(0, var):
        sys.stdout.write('-')
    print('\n')


#general spending report
print(genheader)
drawline(genheader)
print(general)
drawline(genheader)

#percent-based spending report
print(pctheader)
drawline(pctheader)
print(genpct)
drawline(pctheader)

#pie chart creation
labels = general['Category']
numbers = general['Cost']
colors = ['yellow', 'red', 'gray', 'mediumpurple', 'deepskyblue']
explode = (0.2, 0, 0, 0, 0)

plt.title(genheader)
plt.pie(numbers, labels=labels, colors=colors, explode=explode)
plt.legend()
plt.show()