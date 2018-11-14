import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.metrics import silhouette_score, silhouette_samples,adjusted_rand_score
from sklearn.base import clone

def cluster_stability(data, model, n_iter=10):
    labels, indices = list(), list()
    rng = np.random.RandomState(1)

    for i in range(n_iter):
        # draw bootstrap samples, store indices
        sample_indices = rng.randint(0, data.shape[0], data.shape[0])
        indices.append(sample_indices)
        model = clone(model)
        if hasattr(model, "random_state"):
            # randomize estimator if possible
            model.random_state = rng.randint(1e5)
        try:  # numpy array or list
            data_bootstrap = np.array(data)[sample_indices]
        except TypeError:  # pandas data frame
            data_bootstrap = data.iloc[sample_indices]
        model.fit(data_bootstrap)
        # store clustering outcome using original indices
        relabel = -np.ones(data.shape[0], dtype=np.int)
        relabel[sample_indices] = model.labels_
        labels.append(relabel)

    scores = list()
    for l, i in zip(labels, indices):
        for k, j in zip(labels, indices):
            # we also compute the diagonal which is a bit silly
            in_both = np.intersect1d(i, j)
            scores.append(adjusted_rand_score(l[in_both], k[in_both]))

    return model, np.mean(scores)

def silhouette_plot(train_data, predict_data, n_clusters, score=None):
    fig = plt.figure()
    # fig.set_size_inches(18, 7)
    plt.title(("Silhouette plot w/ n_clusters = %d" % n_clusters),
              fontsize=14, fontweight='bold')

    # The silhouette coefficient can range from -1, 1
    # The (n_clusters+1)*10 is for inserting blank space between silhouette plots of individual clusters
    plt.xlim([-0.2, 1])
    plt.ylim([0, len(train_data) + (n_clusters + 1) * 10])

    # Compute the silhouette scores for each sample
    silhouette_values = silhouette_samples(train_data, predict_data)

    y_lower = 10
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to cluster i, and sort them
        ith_cluster_silhouette_values = sorted(silhouette_values[predict_data == i])

        size_cluster_i = len(ith_cluster_silhouette_values)
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        plt.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster numbers at the middle
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

    # The vertical line for average silhouette score of all the values
    if score is not None:
        plt.axvline(x=score, color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.show()

