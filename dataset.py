import matplotlib.pyplot as plt
import pandas as pd 
from plotly import graph_objs as go 
import plotly.express as px 
import plotly.figure_factory as ff 
from collections import Counter
from PIL import Image 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk 
from nltk.corpus import stopwords
from tqdm import tqdm 
import os 
import nltk 
import scipy
import random 
from spacy.util import compounding 
from spacy.util import minibatch
import warnings 
warnings.filterwarnings("ignore")
import os 
for dirname, _, filenames in os.walk('/kaggle/input'): 
    for filename in filenames: print(os.path.join(dirname, filename))



train = pd.read_csv('csv/train.csv') 
test = pd.read_csv('csv/test.csv') 
ss = pd.read_csv('csv/sample_submission.csv')

train.dropna(inplace = True) #Eliminamos los valores nulos del csv train

def jaccard(str1, str2):
    a = set(str1.lower().split())
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

# Distribución de tweets en el conjunto Train
sentiment_counts_train = train['sentiment'].value_counts()
fig = go.Figure(data=[go.Pie(labels=sentiment_counts_train.index, values=sentiment_counts_train.values)])
fig.update_layout(title='Distribución de Sentimientos en el Conjunto Train')
fig.show()

# Gráfico de embudo
fig = px.funnel(sentiment_counts_train, title='Gráfico de Embudo de Sentimientos en el Conjunto Train')
fig.show()

# Características útiles para generar
train['num_words_text'] = train['text'].apply(lambda x: len(str(x).split()))
train['num_words_selected_text'] = train['selected_text'].apply(lambda x: len(str(x).split()))
train['jaccard_score'] = train.apply(lambda row: jaccard(row['text'], row['selected_text']), axis=1)

# Análisis de curtosis
positive_tweets = train[train['sentiment'] == 'positive']['jaccard_score']
negative_tweets = train[train['sentiment'] == 'negative']['jaccard_score']
neutral_tweets = train[train['sentiment'] == 'neutral']['jaccard_score']

fig, ax = plt.subplots(3, 1, figsize=(10, 12))
ax[0].hist(positive_tweets, bins=30, alpha=0.5, color='green')
ax[0].set_title('Distribución de Jaccard Score para Tweets Positivos')
ax[1].hist(negative_tweets, bins=30, alpha=0.5, color='red')
ax[1].set_title('Distribución de Jaccard Score para Tweets Negativos')
ax[2].hist(neutral_tweets, bins=30, alpha=0.5, color='blue')
ax[2].set_title('Distribución de Jaccard Score para Tweets Neutrales')

plt.tight_layout()
plt.show()

#Ahora voy a hacer una gráfica sobre la longitud de los textos seleccionados en el dataset Train
# Obtener las longitudes de los textos seleccionados en el conjunto Train
train['selected_text_length'] = train['selected_text'].apply(lambda x: len(str(x)))

# Gráfica de las longitudes de los textos seleccionados en el conjunto Train
plt.figure(figsize=(10, 6))
plt.hist(train['selected_text_length'], bins=30, color='purple')
plt.title('Distribución de Longitudes de los Textos Seleccionados (Train)')
plt.xlabel('Longitud')
plt.ylabel('Frecuencia')
plt.show()


