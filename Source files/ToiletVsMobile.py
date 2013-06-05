'''from pylab import *
from matplotlib import font_manager as fm
from matplotlib.transforms import Affine2D
from matplotlib.patches import Circle, Wedge, Polygon
import numpy as np

ax = axes([0.1, 0.1, 0.6, 0.6])
labels = 'people with cell phones', 'people without cell phones'
fracs = [85,15]

explode=(0, 0.1)
patches, texts, autotexts = ax.pie(fracs, labels=labels, explode = explode,         
                             autopct='%1.1f%%', shadow =True)
proptease = fm.FontProperties()
proptease.set_size('xx-small')
setp(autotexts, fontproperties=proptease)
setp(texts, fontproperties=proptease)
rcParams['legend.fontsize'] = 7.0
savefig("pie1")
show()

'''




#naya

from pylab import *
from matplotlib import font_manager as fm
from matplotlib.transforms import Affine2D
from matplotlib.patches import Circle, Wedge, Polygon
import matplotlib.pyplot as plt
import numpy as np

# make a square figure and axes
#figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("source : forbes.com")
labels = 'people with cell phones', 'people without cell phones'
fracs = [85,15]

explode=(0, 0.1)
patches, texts, autotexts = ax.pie(fracs, labels=labels, explode = explode,         
                             autopct='%1.1f%%', shadow =True)
proptease = fm.FontProperties()
proptease.set_size('xx-small')
setp(autotexts, fontproperties=proptease)
setp(texts, fontproperties=proptease)
rcParams['legend.fontsize'] = 7.0
savefig("pie1")



# The slices will be ordered and plotted counter-clockwise.
fig = plt.figure()
ax = fig.add_subplot(111)

labels = 'people with toilets access', 'people without toilet access'
fracs = [65,35]

explode=(0, 0.09)
patches, texts, autotexts = ax.pie(fracs, labels=labels, explode = explode,         
                             autopct='%1.1f%%', shadow =True)
proptease = fm.FontProperties()
proptease.set_size('xx-small')
setp(autotexts, fontproperties=proptease)
setp(texts, fontproperties=proptease)
rcParams['legend.fontsize'] = 7.0
savefig("pie1")



show()

