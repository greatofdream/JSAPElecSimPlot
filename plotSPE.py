from scipy.io import loadmat
import argparse
import matplotlib.pyplot as plt

psr = argparse.ArgumentParser()
psr.add_argument('-i', dest="input", help="input  file")
psr.add_argument('-o', dest="output", help="output png file ")
args = psr.parse_args()
spe = loadmat(args.input)['SPE']
print(spe.shape)
spe = spe.reshape((-1,))
fig, ax = plt.subplots()
ax.plot(spe)
ax.set_title('spe', size="xx-large", weight="bold")
ax.set_xlim((0,100))
ax.set_xlabel('t/ns', size="xx-large", weight="bold")
ax.set_ylabel('adc', size="xx-large", weight="bold")
plt.savefig(args.output)
plt.close()