# -*- coding: utf-8 -*-
"""
Created on Fri May  6 22:28:05 2022

@author: User
"""

import pandas as pd
import numpy as np
import sklearn
import tensorflow as tf

path=r'\data.csv'

bc =pd.read_csv(path)

bc.drop(['id','Unnamed: 32'], axis=1, inplace=True)

X_features = bc.drop('diagnosis', axis=1)
y_labels = bc.diagnosis.replace({'B': 0, 'M': 1})

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_features, y_labels, test_size= 0.2, random_state=12345)

X_train=np.array(X_train)
X_test=np.array(X_test)
y_train=np.array(y_train)
nClass= len(np.unique(y_test))

import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer, StandardScaler

buffer_size = 1000
batch_size= 5

standardizer = sklearn.preprocessing.StandardScaler()
standardizer.fit(X_train)
X_train = standardizer.transform(X_train)
X_test = standardizer.transform(X_test)


model=tf.keras.Sequential()

model.add(tf.keras.layers.InputLayer(input_shape=X_features.shape[1],))
model.add(tf.keras.layers.Dense(128, activation='relu')) 
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(32, activation='relu'))

model.add(tf.keras.layers.Flatten())


model.add(tf.keras.layers.Dense(nClass,activation='sigmoid'))

model.summary()
#%%

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#%%
history=model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=8, epochs=10)

import matplotlib.pyplot as plt


loss= history.history['loss']
val_loss = history.history['val_loss']
epochs= history.epoch

plt.plot(epochs, loss, label= 'Training Loss')
plt.plot(epochs, val_loss, label= 'Validation Loss')
plt.title('Training vs Validation Loss')
plt.legend()
plt.figure()
plt.show()