import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences

# from config import MAX_LENGTH

VOCAB_SIZE = 20000
MAX_LENGTH = 150
def preprocess_single_review(text, tokenizer):

    sequence = tokenizer.texts_to_sequences([text])

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding='post',
        truncating='post'
    )

    return padded