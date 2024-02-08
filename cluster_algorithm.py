from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_articles(news_articles):
    if len(news_articles) < 5:
        raise ValueError("Number of news articles should be at least 5 for clustering.")

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(news_articles)

    num_clusters = min(len(news_articles), 5)  # Adjusted number of clusters
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)
    clusters = kmeans.labels_

    clustered_data = {}
    for cluster_id in range(num_clusters):
        clustered_data[cluster_id] = [news_articles[i] for i, label in enumerate(clusters) if label == cluster_id]

    return clustered_data

def cluster_product_images(image_paths, text_descriptions):
    # Ensure that the number of image paths matches the number of text descriptions
    if len(image_paths) != len(text_descriptions):
        raise ValueError("Number of image paths must match the number of text descriptions.")

    # Preprocess text descriptions
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(text_descriptions)

    # K-means clustering
    num_clusters = 5 
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)

    # Assign each image to its corresponding cluster
    clustered_images = {}
    for i, label in enumerate(kmeans.labels_):
        if label not in clustered_images:
            clustered_images[label] = []
        clustered_images[label].append(image_paths[i])

    return clustered_images
