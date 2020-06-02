from flask import Flask
from flask import request
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import pickle

tf.config.set_visible_devices([], 'GPU')

model = keras.models.load_model('model.h5')

with open('corpus.pickle', 'rb') as corpus:
    word_index, index_word = pickle.load(corpus)

url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"
embed = hub.load(url)

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods = ['GET'])
def predict():
    text = request.args.get('text')

    embedding = embed([text])
    
    pred = model.predict(embedding)
    
    idx = np.argmax(pred)
    
    return index_word[idx]
    