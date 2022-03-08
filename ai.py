# Based on code from here: https://stackabuse.com/text-generation-with-python-and-tensorflow-keras/

# Built-in
import sys

# Installed
import numpy

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint

# Constants
TRAIN_MODEL = True

def tokenize_words(text):
    # Lowercase everything to standardize it
    text = text.lower()

    # Instantiate the tokenizer
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(text)

    # If the created token isn't in the stop words,
    # make it part of "filtered"
    filtered = filter(lambda token: token not in stopwords.words("english"), tokens)
    return " ".join(filtered)

if __name__ == "__main__":
    print(f"TRAIN_MODEL={TRAIN_MODEL}")
    train_model = input("Do you want to train model? (y/n): ")

    if train_model == "y":
        TRAIN_MODEL = True
    elif train_model == "n":
        TRAIN_MODEL = False
    # else, keep it the same

    inputfile = input("File in ./datasets: ")
    print("Opening file...")
    with open(f"datasets/{inputfile}") as f:
        print("Reading file...")
        file = f.read()
        print("Tokenizing words...")
        processed_inputs = tokenize_words(file)

        print("Sorting words...")
        # Sort the list
        chars = sorted(list(set(processed_inputs)))
        # Convert the chars to numbers using enumerate
        char_to_num = dict((c, i) for i, c in enumerate(chars))

        # Store the total length of all inputs for later
        input_len = len(processed_inputs)
        vocab_len = len(chars)
        print(f"Total number of characters: {input_len}")
        print(f"Total number of vocab: {vocab_len}")

        # How long an individual sequence is
        seq_length = 100
        # Input and output data
        x_data = []
        y_data = []

        # Go through entire list of inputs-
        # and convert the characters to numbers.
        print("Converting characters to numbers...")
        for i in range(0, input_len - seq_length, 1):
            # Define input and output sequences
            # 
            # Input is the current character plus 
            # desired sequence length
            in_seq = processed_inputs[i:i + seq_length]

            # Out sequence is the initial character
            # plus total sequence length
            out_seq = processed_inputs[i + seq_length]

            # We now convert list of characters to 
            # integers based on previously(?) and add 
            # the values to our lists
            x_data.append([char_to_num[char] for char in in_seq])
            y_data.append(char_to_num[out_seq])

        # Save total number of patterns
        n_patterns = len(x_data)
        print(f"Total patterns: {n_patterns}")

        print("Performing numpy conversions...")
        # Convert input sequences into a processed
        # numpy array that the network can use
        X = numpy.reshape(x_data, (n_patterns, seq_length, 1))
        # Convert the numpy array values into floats so
        # that the sigmoid activation function the
        # network uses can interpret them and output
        # probabilities from 0 to 1
        X = X/float(vocab_len)

        # One-hot encode our label data
        print("Encoding label data...")
        y = np_utils.to_categorical(y_data)

        # Create our LSTM model
        print("Creating model...")
        model = Sequential()
        model.add(
            LSTM(
                256,
                input_shape=(X.shape[1], X.shape[2]), 
                return_sequences=True
            )
        )
        model.add(Dropout(0.2))
        model.add(
            LSTM(256, return_sequences=True)
        )
        model.add(Dropout(0.2))
        model.add(LSTM(128))
        model.add(Dropout(0.2))
        model.add(
            Dense(y.shape[1], activation="softmax")
        )

        # Compile the model
        print("Compiling the model...")
        model.compile(
            loss="categorical_crossentropy",
            optimizer="adam"
        )

        if TRAIN_MODEL:
            # Where the model file will be located
            print("Setting model checkpoint...")
            filepath = input("Model file name to save to: ")
            filepath = f"models/{filepath}.hdf5"
            checkpoint = ModelCheckpoint(
                filepath,
                monitor="loss",
                verbose=1,
                save_best_only=True,
                mode="min"
            )
            desired_callbacks = [checkpoint]

            # Fit the model and let it train
            print("Fitting model...")
            print("Training model...")
            model.fit(
                X,
                y,
                # Number of epochs to train for
                # Add more in order to get more
                epochs=int(input("Epochs: ")), 
                # Try reducing this if the dataset is too small
                # Default: 256
                batch_size=256,
                callbacks=desired_callbacks
            )
            print("""Training done!
Run again with TRAIN_MODEL set to False to skip this next time""")
        else:
            print("Skipping model creation...")
        
        filepath = input("File in ./models/ (usually ends in .hdf5): ")
        filepath = f"./models/{filepath}"

        model.load_weights(filepath)
        model.compile(
            loss="categorical_crossentropy",
            optimizer="adam"
        )

        num_to_char = dict(
            (i, c) for i, c in enumerate(chars)
        )

        start = numpy.random.randint(0, len(x_data) - 1)
        pattern = x_data[start]
        print("Random seed:")
        print(f"\"{''.join([num_to_char[value] for value in pattern])}\"")

        # Iterate through a chosen number of characters
        # and then append it to the list of generated
        # characters plus the initial seed
        print("Generating characters...")
        for i in range(1000):
            x = numpy.reshape(pattern, (1, len(pattern), 1))
            x = x / float(vocab_len)
            prediction = model.predict(x, verbose=0)
            index = numpy.argmax(prediction)
            result = num_to_char[index]

            sys.stdout.write(result)

            pattern.append(index)
            # pattern = pattern[1:len(pattern)]