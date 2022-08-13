import numpy as np
import matplotlib.pyplot as plt

def plot_matplotlib_figure_1(param):
    fig = plt.figure(figsize=(3, 1))
    x = np.arange(0,4*np.pi,0.1)   # startstop,step
    y = np.sin(param*x)
    plt.plot(x,y)
    #plt.savefig('/Users/larstornberg/Documents/dashboard_template/dashboard/assets/figure.png')
    return fig

def plot_matplotlib_figure_2(param):
    fig = plt.figure(figsize=(6, 3))
    x = np.arange(0,4*np.pi,0.1)   # start,stop,step
    y = np.sin(param*x)
    plt.plot(x,y)
    #plt.savefig('/Users/larstornberg/Documents/dashboard_template/dashboard/assets/figure.png')
    return fig