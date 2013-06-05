import numpy as np
import matplotlib.pyplot as plt

def plot2():
    
    x1 = range(2,12,1)
    y1 = [0,0,1,4,12,15,19,31,44,65]
    x2 = range(2,12,1)
    y2 = [0.4,0.4,0.8,1.1,1.4,1.7,2.0,7.9,9.0,19]
    
    plt.plot(x1,y1,"bs--",x2,y2, "rs-")
    plt.title('Internet users vs. mobile users in nepal')
    plt.xlabel('Year 2000+ ')
    plt.ylabel('Users per 100 ')
    plt.axis([0,15,0,70])
    '''labels = [ k for k in range(3,18 ) ]
    plt.plot(labels)'''
    plt.plot(20,30,label='internet', color='red')
    plt.plot(10,20,label='mobile', color='blue')
    plt.legend(loc='upper right')
    plt.show()
    

plot2()
