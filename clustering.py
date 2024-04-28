from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

import matplotlib.pyplot as plt

def display_cluster_graph(X, clusters):
    plt.scatter(X['Intell Ag Attention Span'], X['Chem Attention Span'], c=clusters)
    plt.title('Cluster Graph')
    plt.show()