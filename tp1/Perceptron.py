import keras

class Perceptron:
    def __init__(self, nb_inputs, nb_epochs, learning_rate) -> None:
        self.nb_input = nb_inputs
        self.nb_epochs = nb_epochs
        self.learning_rate = learning_rate
        self.biais = [1,0] #valeur 1 de poids 0

    def train(self,input_list,expected_ouput_list):
        for epo in range(self.nb_epochs):
            for i in range(len(input_list)):
                perceptron_result = self.predict(input_list[i])

                #correction des poids
            pass
        pass

    def predict(self,input_list) ->int:
        pass