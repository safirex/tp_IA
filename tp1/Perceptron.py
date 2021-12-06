
import numpy as np

class Perceptron:
    def __init__(self, nb_inputs, nb_epochs, learning_rate) -> None:
        self.nb_input = nb_inputs
        self.weightList = np.zeros((nb_inputs,))
        self.nb_epochs = nb_epochs
        self.learning_rate = learning_rate
        self.biais = 1 #valeur 1 de poids 0

    def train(self,input_list,expected_ouput_list):
        
        for epo in range(self.nb_epochs):
            print("epoch n° "+str(epo))

            for i in range(len(input_list)):
                perceptron_result = self.predict(input_list[i])

                #correction des poids
                self.weightList[i%2] = self.weightList[i%2] + self.learning_rate * (
                    (expected_ouput_list[i] - perceptron_result)
                )
                #Wi' = Wi + a (yt-y)* Xi
                print(perceptron_result)
            print()
            print(self.weightList)
            print()
            
        

    def predict(self,input_list) ->int:
        sumvalue = 0
        for inp in range(self.nb_input):
            sumvalue += input_list[inp] * self.weightList[inp] + self.biais

        #sumvalue /= self.nb_input
        if(sumvalue >0.5):
            return 1
        return 0