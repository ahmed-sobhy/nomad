from modelConv import model
from keras import  optimizers
import keras.backend as K
from prepare import prepare
from parseConv import  parse
import pandas as pd



train, labels = prepare()
train = parse()
#train2 = parse()

#train = pd.concat([train1, train2], axis=1).as_matrix()

print(train.shape)
print(labels.shape)

model = model()

optimizer = optimizers.Adam(lr=0.0001)


def customLoss(yTrue,yPred):
    return K.sqrt(K.mean(K.pow(K.log(yTrue+1) - K.log(yPred+1),2)))

model.compile(optimizer, loss=customLoss)
model.summary()
model.fit(train, labels, batch_size= 32 ,epochs = 1000000, validation_split= 0.2, verbose= 1)


