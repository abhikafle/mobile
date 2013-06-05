#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 10
emailMeans = (719, 817, 1018, 1093, 1319, 1574, 1802, 1971, 2267, 2497)
emailStd =   (0, 0, 0, 0, 0, 0, 0, 0, 1, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, emailMeans, width, color='r', yerr=emailStd)

smsMeans = (1415, 1761, 2205, 2744, 3367, 4029, 4640, 5317, 5957, 6835)
smsStd =   (0, 0, 1, 1, 2, 2, 2, 3, 3, 4)
rects2 = ax.bar(ind+width, smsMeans, width, color='b', yerr=smsStd)

# add some
ax.set_ylabel('Subscriber (in millions)')
ax.set_title('Comparison of Internet and Cell phones subscriber worldwide')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012') )

ax.legend( (rects1[0], rects2[0]), ('Internet', 'Cell Phones'))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()