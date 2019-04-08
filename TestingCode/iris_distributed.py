from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('ajumal').setMaster('local[2]')
sc = SparkContext(conf=conf)
from sklearn.datasets import load_iris
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
iris_data=load_iris()
x=iris_data.data
t=iris_data.target

Z=np.insert(x,4,t,axis=1)
np.random.shuffle(Z)
x_train, x_test = Z[:120,:4], Z[120:,:4]
y_train1, y_test1=  Z[:120,4], Z[120:,4]
y_train=np_utils.to_categorical(y_train1,num_classes=3)
y_test=np_utils.to_categorical(y_test1,num_classes=3)
import keras
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
from keras.regularizers import l2
model=Sequential();
model.add(Dense(64,activation='relu'));
model.add(Dense(128,activation='relu'));
model.add(Dense(3,activation='softmax'));
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy']);
from elephas.utils.rdd_utils import to_simple_rdd
rdd = to_simple_rdd(sc, x_train, y_train)

from elephas.spark_model import SparkModel


spark_model = SparkModel(model, frequency='epoch', mode='asynchronous',num_workers=3)
spark_model.fit(rdd, epochs=10, batch_size=10, verbose=1, validation_split=0.2)

#score = spark_model.master_network.evaluate(x_test, y_test, verbose=1)
