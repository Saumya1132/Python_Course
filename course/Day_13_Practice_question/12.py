# read csv file and which uses seaborn to create a swarm plot for data visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_csv_and_plot(file_path):
    df = pd.read_csv(file_path)
    
    sns.swarmplot(x='Category', y='Value', data=df)
    
    plt.title('Swarm Plot of Category vs. Value')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.savefig('swarm_plot.png', format='png')
    plt.show()

file_path = 'D:\course\Day_13_Practice_question\data4.csv'
read_csv_and_plot(file_path)
