from keras.models import Model , Sequential
from keras.layers import Input, Dense, BatchNormalization, Dropout, Conv3D, Flatten

def model():

    # create model
    model = Sequential()
    model.add(Conv3D(1, kernel_size=(3, 3, 3), strides=(2, 2, 2), padding='valid', activation="relu", input_shape=(25, 25, 25, 4)))
    model.add(Flatten())
    model.add(Dense(2,activation='relu'))
    return model
