import numpy as np
from tensorflow import keras
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense
#import livelossplot
#from livelossplot import PlotLossesKeras
import math
import matplotlib.pyplot as plt


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

print(x.shape) #(9,7) 
#x = np.reshape(x, (len(x), 1, 7)) #reshape pour keras delimite les listes

# -> Teachers
y = np.asarray([0,1,2,3,4,5,6,7,8,9]) # peut etre remplacé par itérateur du premier tab




#on ignore 0 pour qulque raison que ce soit
x= x[1:]
y= y[1:]

y = keras.utils.to_categorical(y)

print(x)
print(x.shape)
print(y)
print(y.shape)


#utiliser keras.utils.to_categorical() sur sortie de l'ia pour permettre calcul d'erreur




#    Je prépare ma descente du gradient avec un learning rate à 0.1
sgd = keras.optimizers.SGD(learning_rate=0.5)

#    Mon modèle est de type séquentiel. Cela veut dire que les couches (layers) du réseau de neurones se suivent les unes après les autres
model = Sequential()

#    J'ajoute une couche à mon modèle. J'indique que cette couche a une taille d'input de 7, et une taille d'output de 1
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
#plt.plot(history.history['val_acc'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

to_predict = np.array([[0,1,1,0,0,0,0],   #1
                       [1,1,1,1,0,0,0],   # 3 sans barre milieu
                       [1,1,1,1,1,0,1],   #0
                        [1,1,1,0,0,0,0],  #7
                       [1,1,0,1,1,0,0]    # 2 sans barre milieu
                       ])


for v in  model.predict(to_predict):
  print(v)
  print(max(v[:]))