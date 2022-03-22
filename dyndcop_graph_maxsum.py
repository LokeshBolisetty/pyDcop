import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('metrics_smallDensity.csv', delimiter=',', 
                     names=['t', 'cycle', 'cost', 'violation' , 
                            'msg_count', 'msg_size', 'status'])

fig, ax = plt.subplots()
ax.plot(data['t'], data['cost'], label='cost MaxSum')

ax.set(xlabel='time', ylabel='cost', title='Solution cost')
ax.grid()
plt.title("Maxsum cost")

fig.savefig("maxsum_smallDensity.png", bbox_inches='tight')
plt.legend()
plt.show()
