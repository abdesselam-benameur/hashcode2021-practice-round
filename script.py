#%%
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np
#%%
Z = [[1,2], [5,6]] # np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

#%%
fig, ax = plt.subplots()
ax.pcolormesh(Z)
#%%

# import matplotlib.pyplot as plt 
  
# # x axis values 
# x = [1,2,3] 
# # corresponding y axis values 
# y = [2,4,1] 
  
# # plotting the points  
# plt.plot(x, y) 
  
# # naming the x axis 
# plt.xlabel('x - axis') 
# # naming the y axis 
# plt.ylabel('y - axis') 
  
# # giving a title to my graph 
# plt.title('My first graph!') 
  
# # function to show the plot 
# plt.show() 


# import datetime 
# alphabets = [str(x)for x in range(10000000)] 
# a = datetime.datetime.now() # store initial time 
# for item in alphabets: 
#     len(item) 
# b = datetime.datetime.now() # store final time 
# print((b-a).total_seconds()) # results 
# a = datetime.datetime.now() 
# fn = len                    # function stored locally 
# for item in alphabets: 
#     fn(item) 
# b = datetime.datetime.now() 
# print((b-a).total_seconds())


# import datetime

# alphabets = [str(x) for x in range(10000000)]
# a = datetime.datetime.now()  # store initial time
# for item in alphabets:
#     len(item)
# b = datetime.datetime.now()  # store final time
# print((b - a).total_seconds())  # results
# a = datetime.datetime.now()
# fn = len  # function stored locally
# for item in alphabets:
#     fn(item)
# b = datetime.datetime.now()
# print((b - a).total_seconds())

# import datetime
# import itertools

# a = datetime.datetime.now()  # store initial time
# combinations1 = [(x,y) for x in range(100000) for y in range(100000)]
# b = datetime.datetime.now()  # store final time
# print((b - a).total_seconds())  # results

# combinations1  = []
# a = datetime.datetime.now()
# combinations1  = []
# for x in range(100000):
#     for y in range(100000):
#         combinations1.append((x,y))
# b = datetime.datetime.now()
# print((b - a).total_seconds())

# combinations1  = []
# a = datetime.datetime.now()
# combinations1 = itertools.combinations(range(100000), 2)
# b = datetime.datetime.now()
# print((b - a).total_seconds())