import numpy as np
import pandas
from tensorflow import keras
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense
#import livelossplot
#from livelossplot import PlotLossesKeras
import math
import matplotlib.pyplot as plt


def readFromCsv(path):
      
  import pandas as pd
  from numpy import genfromtxt

  #data = genfromtxt(fname = path)
  data = pandas.read_csv(path).to_numpy()

  return data

x = readFromCsv("input.csv")

'''
#inputs affichage 7 seg
#list 9x7
x = np.array  ([[1,1,1,1,1,1,0], #0
                [0,1,1,0,0,0,0],
                [1,1,0,1,1,0,1], #2
                [1,1,1,1,0,0,1],
                [0,0,1,0,0,1,1],
                [1,0,1,1,0,1,1],
                [1,0,1,1,1,1,1],
                [1,1,1,0,0,0,0],
                [1,1,1,1,1,1,1],
                [1,1,1,1,0,1,1] #9
                ]) #tout à 1 = 8

'''
print(x.shape) #(9,7) 
#x = np.reshape(x, (len(x), 1, 7)) #reshape pour keras delimite les listes

# Teachers
'''
y = np.asarray([0,1,2,3,4,5,6,7,8,9]) # peut etre remplacé par itérateur du premier tab
'''

#extract teacher value
y = x[:,-1]
x = x[:,:-1]

#on ignore 0 pour qulque raison que ce soit
x= x[1:]
y= y[1:]

# change le tableau de Y valeurs entre 0 et 9 à un tableau2D de (Y+1 x Y) valeur entre 0 et 1
y = keras.utils.to_categorical(y)

print(x)
print(x.shape)
print(y)
print(y.shape)



#    Je prépare ma descente du gradient avec un learning rate à 0.1
sgd = keras.optimizers.SGD(learning_rate=0.5)

#    Mon modèle est de type séquentiel. Cela veut dire que les couches (layers) du réseau de neurones se suivent les unes après les autres
model = Sequential()

#    J'ajoute une couche à mon modèle. J'indique que cette couche a une taille d'input de 7, et une taille d'output de 10
#couche d'input de l'IA
model.add(Dense(10, input_dim=7, activation='softmax'))

#   J'affiche une représentation du modèle
model.summary()

#   Je compile le modèle avec la descente du gradient et une losse de type (t-y)² (celle vu en cours)
model.compile(optimizer=sgd, loss='mean_squared_error')

#   Je lance l'apprentissage du modèle sur 500 epochs
callback = keras.callbacks.EarlyStopping(monitor='loss', patience=3, min_delta = 0.000001)

history = model.fit(x, y, epochs=6000,
                    callbacks=[callback],)



print(len(history.history['loss']))
plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()


'''
to_predict = np.array([[0,1,1,0,0,0,0],   #1
                       [1,1,1,1,0,0,0],   # 3 sans barre milieu
                       [1,1,1,1,1,0,1],   #0
                       [1,1,1,0,0,0,0],   #7
                       [1,1,0,1,1,0,0]    # 2 sans barre milieu
                       ])
'''

data = readFromCsv("predictions.csv")
expectations = data[:,-1]
to_predict = data[:,:-1]

IA_output = model.predict(to_predict)
error_r8=0
for v in range(len(IA_output)):
  print(max(IA_output[v]))
  print("got "+str(np.argmax(IA_output[v]))+ " expected "+str(expectations[v]))
  if (np.argmax(IA_output[v]) != expectations[v]):
        error_r8+=1
  print()
error_r8/=v
print("error rate of "+str(error_r8))
