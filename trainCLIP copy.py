import tensorflow as tf
from tensorflow import keras as keras
from keras import layers as tfl
from formatText import formatText
from CLIPencoder import textEncoder

#textInput = 'Hello World'

#embeddings = formatText(textInput)

NNLayers = 7
unitsMid = 1000
unitsOut = 1

inputEmbeddings = keras.Input((None, 300))
textEnc = textEncoder()
x = textEnc(inputEmbeddings)

for i in range(NNLayers):
    x = tfl.Dense(unitsMid, activation='relu')(x)
x = tfl.GlobalAveragePooling1D()(x)
output = tfl.Dense(unitsOut, activation='sigmoid')(x)

# Create the combined model
combined_model = keras.Model(inputs=inputEmbeddings, outputs=output)

combined_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
combined_model.summary()
