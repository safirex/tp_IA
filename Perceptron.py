
import numpy as np

class Perceptron:
    def __init__(self, nb_inputs, nb_epochs, learning_rate) -> None:
        self.nb_input = nb_inputs + 1 #ajout du biais dans la table des poids
        self.weightList = np.zeros((self.nb_input,)) 
        self.nb_epochs = nb_epochs
        self.learning_rate = learning_rate
        self.biais = 1 #valeur 1 de poids 0

    def train(self,input_list,expected_ouput_list):
        print(input_list)

        print(self.weightList)
        nbSynapse = self.nb_input
        for epo in range(self.nb_epochs):
            print("epoch n° "+str(epo))
            for i in range(len(input_list)):

                # add bias value to input list
                inputs = input_list[i]
                inputs = np.append(inputs,self.biais)
                print(inputs)

                perceptron_result = self.predict(inputs)

                #correction des poids
                self.weightList[i%nbSynapse] = self.weightList[i%nbSynapse] + self.learning_rate * (
                    (expected_ouput_list[i] - perceptron_result)
                )
                #Wi' = Wi + a (yt-y)* Xi

                surface_erreur = 1/2  * (expected_ouput_list[i] - perceptron_result)
                print("surface err: "+ str(surface_erreur))
                print("result: "+ str(perceptron_result))
            print()
            print(self.weightList)
            print()
            
        

    def predict(self,input_list) ->int:
        sumvalue = 0

        # E (wi*xi)  bias included
        for inp in range(self.nb_input):
            sumvalue += input_list[inp] * self.weightList[inp] 

        #sumvalue /= self.nb_input
        if(sumvalue >0):
            return 1
        return 0