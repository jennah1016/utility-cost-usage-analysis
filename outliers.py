import sys
import pandas as pd
import matplotlib.pyplot as plt

general = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/all%20billing%20data.csv')
electric = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Electric%20billing%20data.csv')
water = pd.read_csv('https://raw.githubusercontent.com/jennah1016/name-tbd/refs/heads/main/Water%20billing%20data.csv')

#select data to view
#describe function to see what we have to work with
#histogram
