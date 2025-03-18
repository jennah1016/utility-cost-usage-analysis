import pandas as pd
import matplotlib.pyplot as plt
import sys

general = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/all%20billing%20data.csv')
electric = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Electric%20billing%20data.csv')
water = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Water%20billing%20data.csv')
natural_gas = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Natural%20Gas%20billing%20data.csv')

genheader = ('CTA Utility Spending Since 2024')
pctheader = ('Utility Billing Percentages Since 2024')

def drawline(str):
    var = len(str)
    for i in range(0, var):
        sys.stdout.write('-')
    print('\n')

print(genheader)
drawline(genheader)
print(general)

drawline(genheader)

print(pctheader)
drawline(pctheader)
print(general['Category'])




labels = general['Category']
numbers = general['Cost']
colors = ['yellow', 'red', 'gray', 'mediumpurple', 'deepskyblue']
explode = (0.2, 0, 0, 0.2, 0.2)

plt.title(genheader)
plt.pie(numbers, labels=labels, colors=colors, explode=explode)
plt.legend()
plt.show()


