# bibliotecas

import re
import praw
import config
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

## Lista de busca no Reddit
topics = ['datascience', 'machinelearning', 'bigdata', 'ChatGPT']

## funcao import

def get_dados():

    # Acessando API
    api_reddit = praw.Reddit(client_id = "9lGHzTAJduXoKoofJ5m8dQ",
                             client_secret = "AhzwNnXbGtXTqjGukv21Vb4Y7nYw3w",
                             passaword = "23050800",
                             user_agent = "Classification-app",
                             username = "lptg23")

    # Contando o número de caracteres - expressões regulares
    char_count = lambda post: len(re.sub('\W|\d', '', post.selftext))
    mask = lambda post: char_count(post) >= 50

    # lista para os resultados
    data = []
    labels = []

    # loop
    for i, assunto in enumerate(topics):
        #extrair os posts
        subreddit_data = api_reddit.subreddit(topics).new(limit = 1000)

        # Filtrar os posts que não sastifazem a condicional - mask
        posts = [post.selftext for post in filter(mask, subreddit_data)]

        # Adiciona posts e labels às listas
        data.extend(posts)
        labels.extend([i] * len(posts))

        print(f"Número de posts do assunto r/{topics}: {len(posts)}",
              f"\nUm dos posts extraidos: {posts[0][600]}...\n",
              "_" * 80 + '\n')

        return data, labels