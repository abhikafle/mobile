#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

N = 4
emailMeans = (90, 22, 34, 20)
emailStd =   (2, 3, 4, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, emailMeans, width, color='r', yerr=emailStd)

smsMeans = (1, 98, 72, 95)
smsStd =   (0, 5, 2, 3)
rects2 = ax.bar(ind+width, smsMeans, width, color='y', yerr=smsStd)

# add some
ax.set_ylabel('Percentage')
ax.set_title('Comparison of email and sms marketing')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Spam receive', 'Open rate(Average)', 'Use of email/sms in mobile', 'Open rate within 15min') )

ax.legend( (rects1[0], rects2[0]), ('Email', 'SMS') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()