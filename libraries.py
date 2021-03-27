import nltk
import numpy as np
from tensorflow import keras

nltk.download("punkt")
nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer
Lemmatizer = WordNetLemmatizer()

import json
import pickle

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random