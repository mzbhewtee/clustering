from flask import Flask
from flask import render_template
from cluster_algorithm import cluster_articles, cluster_product_images

app = Flask(__name__)

news_articles = [
    "Research Team Identifies New Species of Orchid in the Amazon Rainforest",
    "Government Proposes Comprehensive Plan to Combat Air Pollution",
    "Tech Stocks Surge to All-Time Highs Amid Economic Rebound",
    "COVID-19 Vaccination Efforts Expand to Cover Children Ages 5 to 11",
    "Global Conference Addresses Growing Threats in Cybersecurity",
    "New Study Links Social Media Use to Increased Anxiety in Teens",
    "Massive Wildfire Engulfs Parts of Australia, Forcing Evacuations",
    "Report Warns of Drastic Decline in Global Honeybee Populations",
    "Space Exploration Mission Uncovers Potential Traces of Water on Mars",
    "Health Authorities Declare Victory Over Measles Outbreak in Asia"
]
images = [
    '/static/images/c1.jpg',
    '/static/images/c2.avif',
    '/static/images/c3.webp',
    '/static/images/f1.jpg',
    '/static/images/f2.avif',
    '/static/images/f3.jpg',
    '/static/images/s1.jpg',
    '/static/images/s2.jpg',
    '/static/images/s3.avif',
]
text_descriptions = [
    'crowd of people at a concert',
    'crowd of people at a concert',
    'crowd of people at a concert',
    'fashion',
    'fashion',
    'fashion',
    'sports',
    'sports',
    'sports',
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster/articles')
def cluster():
    # Perform clustering on the list of news articles
    clustered_data = cluster_articles(news_articles)

    # Pass clustered data to the template
    return render_template('article.html', clusters=clustered_data)

@app.route('/cluster/images')
def cluster_images():
    # Perform clustering on the list of news articles
    clustered_images = cluster_product_images(images, text_descriptions)

    # Pass clustered data to the template
    return render_template('images.html', clustered_images=clustered_images)
if __name__ == '__main__':
  app.run()