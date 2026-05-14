# Sentiment Analysis using LSTM, GRU, and BiLSTM

Deep learning-based sentiment analysis project using Yelp reviews and recurrent neural networks (LSTM, GRU, and BiLSTM). This project includes data preprocessing, model training, evaluation, and a Streamlit web application for real-time sentiment prediction.

---

## Project Overview

This project performs binary sentiment classification on Yelp reviews using multiple recurrent neural network architectures.

The main goals of the project are:

* Build an end-to-end NLP pipeline
* Compare LSTM, GRU, and BiLSTM architectures
* Train models on large-scale Yelp review data
* Deploy a real-time sentiment analysis web app using Streamlit
* Follow modular and production-style project structure

---

## Features

* Text preprocessing and tokenization
* Sequence padding using Keras preprocessing
* LSTM model
* GRU model
* Bidirectional LSTM model
* Early stopping and model checkpointing
* Streamlit web application
* Modular Python project structure
* Saved tokenizer and trained models
* Real-time sentiment prediction

---

## Tech Stack

### Languages & Frameworks

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* Pandas
* Scikit-learn

### Deep Learning Models

* LSTM
* GRU
* BiLSTM

---

## Dataset

Dataset used:

* Yelp Academic Dataset Reviews

The dataset contains real-world Yelp reviews used for sentiment classification.

Sentiment mapping:

* Positive → 1
* Negative → 0

The dataset was balanced before training to avoid class imbalance issues.

---

## Model Performance

| Model  | Test Accuracy |
| ------ | ------------- |
| LSTM   | ~80%          |
| GRU    | 94.58%        |
| BiLSTM | 93.53%   |

The GRU model achieved the best overall performance.

---

## Project Structure

```bash
sentiment_analysis_lstm-gru/
│
├── app/
│   └── streamlit_app.py
│
├── models/
│   ├── best_gru.keras
│   └── tokenizer.pkl
│
├── src/
│   ├── config.py
│   ├── preprocess.py
│   └── predict.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── notebooks/
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/anujtyagi7560/Sentiment-Analysis-using-LSTM-GRU.git
```

### 2. Navigate to Project Folder

```bash
cd Sentiment-Analysis-using-LSTM-GRU
```

### 3. Create Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Streamlit App

Run the following command from the project root directory:

```bash
streamlit run app/streamlit_app.py
```

The app will open in your browser.

![alt text](image.png)

---

## Example Predictions

### Positive Review

```text
The food was amazing and the staff was extremely friendly.
```

Prediction:

```text
Positive
```

---

### Negative Review

```text
Terrible experience. The service was slow and disappointing.
```

Prediction:

```text
Negative
```

---

## Training Pipeline

The training pipeline includes:

1. Load Yelp dataset
2. Map sentiment labels
3. Balance classes
4. Tokenization
5. Sequence padding
6. Train/validation/test split
7. Model training
8. Evaluation
9. Model saving

---

## Future Improvements

* Deploy app on Streamlit Cloud
* Add attention mechanisms
* Use pretrained embeddings (GloVe/Word2Vec)
* Add Docker support
* Add CI/CD workflows
* Train transformer-based models (BERT)

---

## Author

Anshul Tyagi

GitHub:

[https://github.com/anujtyagi7560](https://github.com/anujtyagi7560)

---

## License

This project is licensed under the MIT License.
