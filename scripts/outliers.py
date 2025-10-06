import sys
import pandas as pd
import matplotlib.pyplot as plt

#load actual data
electric = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Electric%20billing%20data.csv')
water = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Water%20billing%20data.csv')
natural_gas = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Natural%20Gas%20billing%20data.csv')

#load fake data
chosen_data = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/blank.csv')
report_header = 'Choose a report'

def drawline(str):
    var = len(str)
    for i in range(0, var):
        sys.stdout.write('-')
    print('\n')
  
#show options
print('Select which data you would like to see:')
def showoptions():
    print('Press (1) for electric billing data')
    print('Press (2) for water billing data')
    print('Press (3) for natural gas billing data')

showoptions()
user_option = input('Select: ')

#select data
while True:
    if user_option == '1':
        chosen_data = electric
        report_header = "Electric billing data since January 2022"
        break
    elif user_option == '2':
        chosen_data = water
        report_header = "Water billing data since January 2023"
        break
    elif user_option == '3':
        chosen_data = natural_gas
        report_header = "Natural Gas billing data since January 2022"
        break
    else:
        showoptions()
        user_option = input('Please choose a valid option:')
        
#describe function to see what we have to work with
print(report_header)
drawline(report_header)
print(chosen_data.describe())

#box and whisker plot
#chosen_data.plot(kind='box', xlabel='Year', ylabel='Amount Spent (millions)')
plt.title(report_header)
plt.xlabel('Year')
plt.ylabel('Amount Spent')
chosen_data.boxplot()
plt.show()
