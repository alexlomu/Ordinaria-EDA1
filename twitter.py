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
