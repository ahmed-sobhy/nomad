from keras.models import Model , Sequential
from keras.layers import Input, Dense, BatchNormalization, Dropout

def model():

    # create model
    model = Sequential()
    model.add(Dense(130, input_dim=261, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(130, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(130, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(130, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(130, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(130, activation='relu'))
    model.add(Dropout(0.2))


    model.add(Dense(2,activation='relu'))
    return model
