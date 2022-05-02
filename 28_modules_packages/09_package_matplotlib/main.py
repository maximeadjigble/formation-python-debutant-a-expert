# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

plt.plot([5,6,7,8],[1,5,3,4])
plt.plot([4,5,6,7],[10,2,4,5], 'o')
plt.plot([4,5,6,7],[12,6,3,8], '+')

plt.title("Prix de stock")
plt.xlabel("Temps (jours)")
plt.ylabel("Prix ($)")
plt.show()