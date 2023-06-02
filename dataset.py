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



train = pd.read_csv('/csv/train.csv') 
test = pd.read_csv('/csv/test.csv') 
ss = pd.read_csv('/csv/sample_submission.csv')

train.dropna() #Eliminamos los valores nulos del csv train