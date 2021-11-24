import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
df = pd.read_csv("newdata.csv")
data = df["average"].tolist()


data_set = []
for i in range(0,100):
    ri = random.randint(0,len(data))
    value = data[ri]
    data_set.append(value)
mean = statistics.mean(data_set)
std = statistics.stdev(data_set)
print("mean of sample data",mean)
print("standard deviation of sample data",std)

fig = ff.create_distplot([data_set],["average"],show_hist = False)
fig.show()
