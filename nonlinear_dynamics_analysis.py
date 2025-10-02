import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

w = 12
g = 3

nkd = pd.read_csv("nkd.csv")["a"].to_numpy()
scz = pd.read_csv("scz.csv")["a"].to_numpy()

nkd_embed = nkd[(np.arange(w)*(g+1))+ np.arange(np.max(nkd.shape[0] - (w-1)*(g+1), 0)).reshape(-1,1)]
scz_embed = scz[(np.arange(w)*(g+1))+ np.arange(np.max(scz.shape[0] - (w-1)*(g+1), 0)).reshape(-1,1)]

nkd_pca = PCA(2)
scz_pca = PCA(2)

new_nkd = nkd_pca.fit_transform(nkd_embed)[:1000]
new_scz = scz_pca.fit_transform(scz_embed)[:1000]

print(new_nkd.shape)

nkd_plt = plt.figure()
scz_plt = plt.figure()

nkd_ax = nkd_plt.add_subplot()
scz_ax = scz_plt.add_subplot()

nkd_ax.set_title("Phase Plot of Healthy EEG")
scz_ax.set_title("Phase Plot of Schizophrenic EEG")

nkd_ax.plot(*new_nkd.T)
scz_ax.plot(*new_scz.T)

nkd_plt.savefig("nkd_attractor_plot.png")
scz_plt.savefig("scz_attractor_plot.png")