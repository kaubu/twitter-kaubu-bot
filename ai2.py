# Based on code from here: https://towardsdatascience.com/lstm-how-to-train-neural-networks-to-write-like-lovecraft-e56e1165f514

import glob
import os

# Installed
import numpy
# import keras
from tensorflow import keras
from tensorflow.keras import layers

# corpus_path = input("Corpus path: ")
corpus_path = f"{os.getcwd()}/datasets/corpora/lovecraft/*.txt"

## Reading the files ##
print("Reading the files...")
file_names = glob.glob(corpus_path)
corpus = ""

for file_name in file_names:
    with open(file_name, "r") as f:
        corpus += f.read()

valid_chars = [' ', '!', '\"', '#', '&', "\'", '(', ')', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
corpus = ''.join([c if c in valid_chars else '' for c in corpus])

# print(len(corpus)) # 2,881,584 characters

## One-hot encoding ##
print("One-hot encoding...")
chars = list(set(corpus))
VOCAB_SIZE = len(chars)
char_to_ix = {
    char: ix for ix, char in enumerate(chars)
}
# Receive 50 characters and try to predict the next 50
SEQ_LENGTH = 50
slices = len(corpus) // SEQ_LENGTH

X = numpy.zeros((slices, SEQ_LENGTH, VOCAB_SIZE))
y = numpy.zeros((slices, SEQ_LENGTH, VOCAB_SIZE))

for i in range(0, slices):
    if (i % 500) == 0:
        print(i)
    
    X_sequence = corpus[i*SEQ_LENGTH:(i+1)*SEQ_LENGTH]
    X_sequence_ix = [char_to_ix[value] for value in X_sequence]
    input_sentence = numpy.zeros((SEQ_LENGTH, VOCAB_SIZE))
    for j in range(SEQ_LENGTH):
        input_sentence[j][X_sequence_ix[j]] = 1.
    X[i] = input_sentence

    y_sequence = corpus[i*SEQ_LENGTH+1:(i+1)*SEQ_LENGTH+1]
    y_sequence_ix = [char_to_ix[value] for value in y_sequence]
    target_sequence = numpy.zeros((SEQ_LENGTH, VOCAB_SIZE))
    for j in range(SEQ_LENGTH):
        target_sequence[j][y_sequence_ix[j]] = 1.
    y[i] = target_sequence

## Defining LSTM ##
print("Defining LSTM...")
UNITS = 100
TOTAL_OUTPUT = SEQ_LENGTH*VOCAB_SIZE
inputs = keras.Input(
    shape=(SEQ_LENGTH,VOCAB_SIZE),
    name="sentences"
)

x = layers.LSTM(
    units=UNITS,
    name="LSTM_layer_1",
    return_sequences=True
)(inputs)
x = layers.LSTM(
    units=UNITS,
    name="LSTM_layer_2",
    return_sequences=True
)(x)
x = layers.TimeDistributed(layers.Dense(VOCAB_SIZE))(x)
outputs = layers.Dense(
    VOCAB_SIZE,
    activation="softmax",
    name="predicted_sentence"
)(x)
outputs = layers.Reshape((SEQ_LENGTH,VOCAB_SIZE))(outputs)
model = keras.Model(inputs=inputs, outputs=outputs)

## Training ##
print("Training...")
customAdam = keras.optimizers.Adam(learning_rate=0.0001)
model.compile(
    optimizer=customAdam,
    # Loss function to minimize
    loss="binary_crossentropy",
    # List of metrics to monitor'
    metrics=[
        "mean_squared_error",
        "binary_crossentropy"
    ]
)

es = keras.callbacks.EarlyStopping(
    monitor="loss",
    mode="min",
    verbose=1,
    patience=5,
)

print("# Fit model on training data")

history = model.fit(
    X,
    y,
    batch_size=512,
    # Default: 500 epochs
    epochs=10,
    validation_split=0.1,
    callbacks=[es]
)

chars_np = numpy.asarray(chars)

def output_idx(i):
    return numpy.argmax(model.predict([[X[i]]])[0], 1)

def output_str(i):
    return "".join(list(chars_np[output_idx(i)]))

output_str(0)