import matplotlib.pyplot as plt
import numpy as np

def make_pie(sizes, text,colors,labels, radius=1):
    col = [[i/255 for i in c] for c in colors]
    plt.axis('equal')
    width = 0.35
    kwargs = dict(colors=col, startangle=180)
    outside, _ = plt.pie(sizes, radius=radius, pctdistance=1-width/2,labels=labels,**kwargs)
    plt.setp( outside, width=width, edgecolor='white')

    kwargs = dict(size=20, fontweight='bold', va='center')
    plt.text(0, 0, text, ha='center', **kwargs)

# Group colors
c1 = (226, 33, 7)
c2 = (60, 121, 189)

# Subgroup colors
d1 = (226, 33, 7)
d2 = (60, 121, 189)
d3 = (25, 25, 25)

make_pie([100, 80, 90], "", [d1, d3, d2], ['M', 'N', 'F'], radius=1.2)
make_pie([180, 90], "", [c1, c2], ['M', 'F'], radius=1)
plt.show()