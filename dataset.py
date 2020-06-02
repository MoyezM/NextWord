import random 
import nltk
import string
from tqdm import tqdm
import re
from tensorflow.keras.preprocessing.text import Tokenizer
import random
import tensorflow_hub as hub


WORD = re.compile(r'\w+')

def regTokenize(text):
    words = WORD.findall(text)
    return words

def load_data(lines, data_path = 'wiki_data.txt'):
    data = []
    i = 0
    with open(data_path) as file:
        for line in tqdm(file):
            sent = line.split('|||')[1][1:-2]
            data.append(' '.join(regTokenize(sent.lower())))
            i += 1
            
            if i == lines:
                break

    return data

def split_data(data, split=0.9):
    size = len(data)
    split_idx = int(size * split)
    train = data[:split_idx]
    test = data[split_idx:]
    
    return (train, test)

def split_words(words, low, high):
    temp = words
    ret = []

    while len(temp) != 0:
        idx = random.randint(low, high)

        if idx > len(temp):
            idx = len(temp)

        sub_seq = temp[:idx]
        ret.append(' '.join(sub_seq))
        temp = temp[idx:]

    return ret

def process_data(data, min_seq_len, max_seq_len):
    split_data = []
    for text in tqdm(data):
        words = regTokenize(text)
        
        split_data += (split_words(words, min_seq_len, max_seq_len))

    return split_data

        
def create_tokenizer(data):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data)
    
    return tokenizer

def shuffle_and_split(data, split=.90):
    random.shuffle(data)
    d = [create_x_y(x) for x in data]
    x = [' '.join(x[0]) for x in d]
    y = [x[1] for x in d]
    
    
    return (x, y)
    
def create_x_y(seq):
    arr = regTokenize(seq)
    x = arr[:len(arr) - 1]
    y = arr[len(arr)-1]
    
    return (x,y)
    

