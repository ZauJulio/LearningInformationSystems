import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from read import (
    sourcesGen01,
    sourcesGen02)


def plottable_3d_info(df: pd.DataFrame):
    """
    Transform Pandas data into a format that's compatible with
    Matplotlib's surface and wireframe plotting.
    """
    index = df.index
    columns = df.columns

    x, y = np.meshgrid(np.arange(len(columns)), np.arange(len(index)))
    z = np.array([[df[c][i] for c in columns] for i in index])
    
    xticks = dict(ticks=np.arange(len(columns)), labels=columns)
    yticks = dict(ticks=np.arange(len(index)), labels=index)
    
    return x, y, z, xticks, yticks




gen01KeyAC = list(sourcesGen01["AC_POWER"].keys())[2]

x, y, z, xticks, yticks = plottable_3d_info(sourcesGen01["AC_POWER"][gen01KeyAC])

axes = plt.figure().gca(projection='3d')
axes.plot_surface(x, y, z, antialiased=True)
plt.show()




gen02KeyAC = list(sourcesGen02["AC_POWER"].keys())[2]
x, y, z, xticks, yticks = plottable_3d_info(sourcesGen02["AC_POWER"][gen02KeyAC])

axes = plt.figure().gca(projection='3d')
axes.plot_surface(x, y, z, antialiased=True)
plt.show()