import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle, Wedge, Polygon


fig, ax = plt.subplots(figsize=[8, 8])
plt.ylim([0, 40])
plt.xlim([0, 40])
patches = []
w1 = Wedge(center=[20, 20], r=10, theta1=30, theta2=150, facecolor='red', edgecolor=None, zorder=1)
w2 = Wedge(center=[20, 20], r=10, theta1=150, theta2=270, facecolor='green', edgecolor=None, zorder=1)
w3 = Wedge(center=[20, 20], r=10, theta1=270, theta2=390, facecolor='yellow', edgecolor=None, zorder=1)
patches.extend([w1, w2, w3])

p1 = Polygon([[20-5*3**0.5, 25], [20-2.5*3**0.5, 17.5], [20, 25]], facecolor='red', edgecolor=None, zorder=2)
p2 = Polygon([[20-2.5*3**0.5, 17.5], [20, 10], [20+2.5*3**0.5, 17.5]], facecolor='green', edgecolor=None, zorder=2)
p3 = Polygon([[20+2.5*3**0.5, 17.5], [20+5*3**0.5, 25], [20, 25]], facecolor='yellow', edgecolor=None, zorder=2)
patches.extend([p1, p2, p3])

c1 = Circle((20, 20), 5, facecolor='white', edgecolor=None, zorder=3)
c2 = Circle((20, 20), 4, facecolor='blue', edgecolor=None, zorder=4)
patches.extend([c1, c2])

p = PatchCollection(patches, match_original=True)
ax.add_collection(p)
plt.show()
