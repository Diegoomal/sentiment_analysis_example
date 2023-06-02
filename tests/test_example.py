import pickle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

class Test_Example:

    def test_predicao(self):

        imdb = keras.datasets.imdb

        (_, _), (test_data, _) = imdb.load_data(num_words=10000)

        word_index = imdb.get_word_index()
        word_index = {k: (v+3) for k, v in word_index.items()}
        word_index["<PAD>"] = 0
        word_index["<START>"] = 1
        word_index["<UNK>"] = 2  # unknown
        word_index["<UNUSED>"] = 3

        test_data = keras.preprocessing.sequence.pad_sequences(
            test_data, value=word_index["<PAD>"], padding='post', maxlen=256)

        # vocab_size = 10000

        # model = keras.Sequential()
        # model.add(keras.layers.Embedding(vocab_size, 16))
        # model.add(keras.layers.GlobalAveragePooling1D())
        # model.add(keras.layers.Dense(16, activation='relu'))
        # model.add(keras.layers.Dense(1, activation='sigmoid'))

        # model.compile(optimizer='adam',
        #       loss='binary_crossentropy',
        #       metrics=['accuracy'])
        
        model = load_model('src/artefatos/modelo_treinado.h5')

        print("predito:", model.predict(test_data)[0][0])

    def test_predicao_2(self):

        print("\n")
        
        sentences = ['Rashmi likes ice cream', 'Rashmi hates chocolate.']

        print(f"Sentence:{sentences}")

        with open('src/artefatos/count_vectorizer.pkl', 'rb') as file:
            vectorizer = pickle.load(file)

        vectorized_sentences = vectorizer.transform(sentences).toarray()

        print("vectorized_sentences.shape:", vectorized_sentences.shape)

        model = keras.models.load_model('src/artefatos/modelo_treinado_2.h5')

        predicted = model.predict(vectorized_sentences)

        print(f"Predict: {predicted[0][0]} - Sentense: '{sentences[0]}'")
        print(f"Predict: {predicted[1][0]} - Sentense: '{sentences[1]}'")
        print("\n")
