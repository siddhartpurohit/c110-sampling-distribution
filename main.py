import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

fig = ff.create_distplot( [data] , ["temp"] , show_hist = False)
#fig.show() 

population_mean = statistics.mean(data)
print("\nMean of population : ", population_mean)
std_deviation = statistics.stdev(data)
print(f"Standard deviation of population : {std_deviation} " )

# data_set = []
# for i in range(0,100):
#     ri = random.randint(0,len(data))
#     value = data[ri]
#     data_set.append(value)
# mean = statistics.mean(data_set)
# std = statistics.stdev(data_set)
# print("mean of sample data",mean)
# print("standard deviation of sample data",std)

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        ri = random.randint(0,len(data)-1)
        value = data[ri]
        data_set.append(value)
    mean = statistics.mean(data_set)
    std = statistics.stdev(data_set)

    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([mean_list],["Temperature"],show_hist = False)
    fig.show()

def setup():
    mlist = []
    for i in range(0,1000):
        setofmeans = random_set_of_mean(100)
        mlist.append(setofmeans)
    mean = statistics.mean(mlist)
    std = statistics.stdev(mlist)
    print("mean of sample data",mean)
    print("standard deviation of sample data",std)
    show_fig(mlist)

setup()

#mean of the population = mean of the sample data


#SD of the sampling mean =  SD of Population / sqrt (number of data in each sample)
# SD of the sampling mean = 5.69 / sqrt(100)
# SD of the sampling mean = 5.69 /10 
# SD of the sampling mean = 0.569