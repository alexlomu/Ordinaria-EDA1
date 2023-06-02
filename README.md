# Ordinaria-EDA1
El link de este repositorio es: [Github](https://github.com/alexlomu/Ordinaria-EDA1)
https://github.com/alexlomu/Ordinaria-EDA1.
En este repositorio se responden diversas preguntas, la mayoría relacionadas con la Programación Orientada a Objetos y otras con Datasets.
## Ejercicio de POO
El código propuesto para resolver las diversas tareas en este ejercicio es el siguiente:
```
import re
from datetime import datetime

def es_correo_valido(correo): #Creamos una función que nos sirve para determinar si un email es válido o no
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None



class UserAccount():
    def __init__(self,alias,email,tweets,followers,timeline,):
        if str(alias): #Comprobamos si el alias es una string
            self.alias = alias
        if es_correo_valido(email) == True: #Comprobamos si el correo es válido
            self.email = email
        if tweets == list: #Los tweets serán una lista donde cada elemento será un tweet
            self.tweets = tweets
        if followers == list: #Los followers serán una lista donde cada elemento es uno de los seguidores
            self.followers = followers
        if timeline == list: #El timeline será una lista donde cada elemento será un tweet que alguien habrá publicado con el momento de publicación
            self.timeline = timeline
        self.tweets = []
        self.followers = []
        self.timeline = []

user1 = UserAccount("pepe","pepe@gmail.com", [], [], [])         #Creamos dos users 
user2 = UserAccount("llucia","llucia@gmail.com", [], [], [])

def follow1(user1): #Recibe un objeto
    user1.followers.append(user2.alias) #Añadimos el alias del user2 a la lista de followers de user1
def follow2(user2): #Recibe un objeto
    user2.followers.append(user1.alias) #Añadimos el alias del user1 a la lista de followers de user2
def tweet_user1(tweet1): #Recibe una string
    user1.tweets.append(tweet1) #Añadimos el tweet a la lista de tweets de user1
    if user2.alias in user1.followers: #Si user2 sigue a user1 el tweet se añadirá al timeline junto con la fecha de publicación
        user2.timeline.append(str(datetime.now()) + "   " + str(tweet1))
def tweet_user2(tweet1): #Recibe una string
    user2.tweets.append(tweet1) #Añadimos el tweet a la lista de tweets de user1
    if user1.alias in user2.followers: #Si user2 sigue a user1 el tweet se añadirá al timeline junto con la fecha de publicación
        user1.timeline.append(str(datetime.now()) + "   " + str(tweet1))


follow1(user1)
follow2(user2)

print("Los seguidores de {} son {}".format(user1.alias, user1.followers))
print("Los seguidores de {} son {}".format(user2.alias, user2.followers))

tweet_user1("Este es un tweet de prueba de user1")
print(user1.tweets)
print(user2.timeline)

tweet_user2("Este es un tweet de prueba de user2")
print(user2.tweets)
print(user1.timeline)

class Tweet:
    def __init__(self, sender, message, time):
        self.sender = sender
        entrada = input("¿Quién va a escribir el mensaje, user1 o user2?") #Preguntamos quién va a escribir el mensaje para luego asociarlo al sender
        if entrada == "user1":
            self.sender = user1.alias
        elif entrada == "user2":
            self.sender = user2.alias
        message = input("Introduzca el mensaje que quiere publicar o enviar.") #Hacemos que escriba el mensaje
        if len(message) > 140: # Comprobamos que el mensaje es inferior a 140 carácteres
            print("El texto es demasiado largo")
        else:
            self.message = message
        self.time = time
        self.time = datetime.now() #Guardamos el momento del mensaje

        def __str__ (self):
            return 'Retweet(' + self.sender +  self.messsage + self.time + ')'

    class Retweet():
        def __init__(self, sender, retwetter, message, init_time, retw_time):
            self.sender = sender
            self.retwetter = retwetter
            entrada = input("¿Quién va a escribir el mensaje, user1 o user2?") #Preguntamos quién va a escribir el mensaje para luego asociarlo al sender
            if entrada == "user1":
                self.sender = user1.alias
                self.retwetter = user2.alias
            elif entrada == "user2":
                self.sender = user2.alias
                self.retwetter = user1.alias
            if len(message) > 140: # Comprobamos que el mensaje es inferior a 140 carácteres
                print("El texto es demasiado largo")
            else:
                self.message = message
            self.init_time = init_time #Creamos una variable para guardar la fecha del tweet inicial
            self.retw_time = retw_time #Y otra para la fecha del retweet
            
        def __str__ (self):
            return 'Retweet(' + self.sender +  self.retwetter + self.message + self.init_time + self.retw_time + ')'

        def retw_user1(self): #Creamos una función que modificará los perfiles de los users en función de si user1 hace retweet
            user1.tweets.append(self.message) #Añadimos el tweet a la lista de tweets de user1
            if user2.alias in user1.followers: #Si user2 sigue a user1 el tweet se añadirá al timeline junto con la fecha de publicación del tweet original más la fecha del retweet
                user2.timeline.append(self.init_time + self.message + self.retw_time)
        def retw_user2(self): #Creamos una función que modificará los perfiles de los users en función de si user2 hace retweet
            user2.tweets.append(self.message) #Añadimos el tweet a la lista de tweets de user1
            if user1.alias in user2.followers: #Si user1 sigue a use21 el tweet se añadirá al timeline junto con la fecha de publicación del tweet original más la fecha del retweet
                user1.timeline.append(self.init_time + self.message + self.retw_time)
    class DirectMessage():
        def __init__(self, sender, receiver, message, time):
            self.sender = sender
            self.receiver = receiver
            entrada = input("¿Quién va a escribir el mensaje, user1 o user2?") #Preguntamos quién va a escribir el mensaje para luego asociarlo al sender
            if entrada == "user1":
                self.sender = user1.alias
                self.receiver = user2.alias
            elif entrada == "user2":
                self.sender = user2.alias
                self.receiver = user1.alias
            if len(message) > 140: # Comprobamos que el mensaje es inferior a 140 carácteres
                print("El texto es demasiado largo")
            else:
                self.message = message
            self.time = time
            self.time = datetime.now()  

        def __str__ (self):
            return 'Retweet(' + self.sender +  self.receiver + self.message + self.time + ')'

```

El output obtenido es el siguiente:

```
Los seguidores de pepe son ['llucia']
Los seguidores de llucia son ['pepe']
['Este es un tweet de prueba de user1']
['2023-06-02 11:57:36.420340   Este es un tweet de prueba de user1']
['Este es un tweet de prueba de user2']
['2023-06-02 11:57:36.420340   Este es un tweet de prueba de user2']
```

Además del código también tenemos que responder las siguientes preguntas:
### •¿Deberá modificar los atributos timeline y tweets de la clase UserAccount (definida en el ejercicio 1) para que contenga elementos de la clase hija Retweet? Justifique su razonamiento y, si cree que hay que modificarlos, explique también cómo lo haría.
Sí, porque estamos tratando de usar variables definidas en una clase hija dentro de una clase padre de esta. Para que esto funcionase tendriamos que definir previamente los elementos de Retweet que quisiesemos utilizar.
 
### • ¿Deberá modificar el método def tweet(Tweet tweet1) de la clase UserAccount (definida en el ejercicio 1) para que pueda enviar también objetos de tipo Retweet? Justifique su razonamiento y, si cree que hay que modificarlo, explique también cómo lo haría.
No, porque al ser Retweet una clase hija de Tweet puede usar los métodos definidos anteriormente sin problema.

## Ejercicio de Dataset

El código propuesto es el siguiente:

```
import matplotlib as plt
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
sentiment_counts = train['sentiment'].value_counts()
fig = go.Figure(data=[go.Pie(labels=sentiment_counts.index, values=sentiment_counts.values)])
fig.update_layout(title='Distribución de Sentimientos en el Conjunto Train')
fig.show()

# Gráfico de embudo
fig = px.funnel(sentiment_counts, title='Gráfico de Embudo de Sentimientos en el Conjunto Train')
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

```

Las gráficas obtenidas son las siguientes:
![image](https://github.com/alexlomu/Ordinaria-EDA1/assets/91721507/82c695d0-85fb-4262-8b23-53303717e028)


![image](https://github.com/alexlomu/Ordinaria-EDA1/assets/91721507/60d48911-9069-4d2c-9ec8-c931fb335987)


![image](https://github.com/alexlomu/Ordinaria-EDA1/assets/91721507/218bbd8c-b7bb-4373-bd2d-cfeb34237432)


![image](https://github.com/alexlomu/Ordinaria-EDA1/assets/91721507/4f6c2939-7a56-4d96-ac94-7eac1c1c8e8d)


