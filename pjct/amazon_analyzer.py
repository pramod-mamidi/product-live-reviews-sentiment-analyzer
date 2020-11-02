import pandas as pd
import numpy as np
from tensorflow.python.keras import models, layers, optimizers
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer, text_to_word_sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
import bz2
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
import re
mod=tensorflow.keras.models.load_model('pjct/model_save')
def predict_sent(x):
    import re
    NON_ALPHANUM = re.compile(r'[\W]')
    NON_ASCII = re.compile(r'[^a-z0-1\s]')
    def normalize_texts(texts):
        normalized_texts = []
        for text in texts:
            lower = text.lower()
            no_punctuation = NON_ALPHANUM.sub(r' ', lower)
            no_non_ascii = NON_ASCII.sub(r'', no_punctuation)
            normalized_texts.append(no_non_ascii)
        return normalized_texts
    train_texts = normalize_texts([x])
    MAX_FEATURES = 12000
    tokenizer = Tokenizer(num_words=MAX_FEATURES)
    tokenizer.fit_on_texts(train_texts)
    train_texts = tokenizer.texts_to_sequences(train_texts)
    MAX_LENGTH=255
    train_texts = pad_sequences(train_texts, maxlen=MAX_LENGTH)
    return(mod.predict(train_texts)[0][0].item())
# print(predict_sent('hello how are you'))
