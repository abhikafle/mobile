import numpy as np
import matplotlib.pyplot as plt

def plot2():
    
    x1 = range(8,15,1)
    y1 = [99.4,98.72,95.9,91.96,87.7,75,50]
    
    x2 = range(8,15,1)
    y2 = [0.6,1.28,4.1,8.04,12.3,28,50]

    #z1= range(8,13,1)
    #z2 = [1,2,3,4,5,6,7,18,19,21,22,25,28]
    
    plt.plot(x1,y1,"bo-",x2,y2,"rs-")
    plt.title('Comparison of Desktop web and Mobile web market share')
    plt.xlabel('Year 2000+ ')
    plt.ylabel('Market share in percents ')
    plt.axis([7,18,0,100])
    '''labels = [ k for k in range(3,18 ) ]
    plt.plot(labels)'''
    #t = np.arange(, 5., )
    #plt.plot(  -3*t + 100, 'bs')
    
    plt.plot(20,30,label='Mobile web', color='red')
    plt.plot(10,20,label='Desktop web', color='blue')
    plt.legend(loc='upper right')
    plt.show()
    millions(1)

plot2()
