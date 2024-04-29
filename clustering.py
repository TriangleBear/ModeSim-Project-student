from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.pyplot import subplots_adjust
from matplotlib.cm import ScalarMappable
import numpy as np
from matplotlib.cm import ScalarMappable

def cluster_students(X):
    """
    Cluster the students based on their attention span.

    Parameters:
    X (pandas.DataFrame): The attention span data.

    Returns:
    labels (numpy.ndarray): The cluster labels for each student.
    """
    # Perform clustering using K-means algorithm
    kmeans = KMeans(n_clusters=3, random_state=0)
    labels = kmeans.fit_predict(X)

    return labels

def display_cluster_graph(X, clusters):
    plt.figure()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Combine all attention span data into a single list
    all_attention_span = X[['Intell Ag Attention Span', 'Chem Attention Span', 'Ethics Attention Span', 'Info Assurance Attention Span']].values.flatten()
    plt.subplots_adjust(right=0.8)  

    sm = ScalarMappable(norm=plt.Normalize(min(all_attention_span), max(all_attention_span)))
    sm.set_array([])

    # Plot Chemistry and Ethics as minor subjects
    ax1.scatter(X['Chem Attention Span'], X['Ethics Attention Span'], c=clusters)

    # Plot Intelligence Agency and Information Assurance as major subjects
    ax2.scatter(X['Intell Ag Attention Span'], X['Info Assurance Attention Span'], c=clusters)

    plt.colorbar(sm, label='Attention Span (Combined)', ax=[ax1, ax2])

    ax1.set_title('Cluster Graph (Minor Subjects)')
    ax2.set_title('Cluster Graph (Major Subjects)')

    plt.show()