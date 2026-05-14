import pickle
import tensorflow as tf

from preprocess import preprocess_single_review

# Load model
model = tf.keras.models.load_model("models/best_gru.keras")

# Load tokenizer
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


def predict_sentiment(text):

    processed = preprocess_single_review(text, tokenizer)

    prediction = model.predict(processed)[0][0]

    sentiment = "Positive" if prediction >= 0.5 else "Negative"

    return sentiment, float(prediction)