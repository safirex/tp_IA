import Character as ch
import Army as arm
import numpy as np
import pandas as pd
import random as rd
import math

CSVPATH ="characters.csv"
rd.seed(15)


def main():


    data = pd.read_csv(CSVPATH, header=None)
    characters = []
    # Discover, visualize, and preprocess data using pandas if needed.
    data = data.to_numpy()

    for datarow in data[1:]:
        char = ch.Character(datarow)
        random = rd.random()*80+20
        army = arm.Army(random,char.morale_value)
        char.setArmy(army)
        characters.append(char)

    #set the moral value arrays
    armies_moral_tab = []
    characters_moral_tab = []
    for i in range(0,len(characters)):
        characters_moral_tab.append(characters[i].morale_value)
        armies_moral_tab.append( characters[i].army.get_Total_Moral())
    armies_moral_tab = np.array(armies_moral_tab)
    characters_moral_tab = np.array(characters_moral_tab)
    sum_val_armies_moral = np.sum(armies_moral_tab)


    ### creation du model IA
    
    # user datas
    input_choice = np.array([[0,0],[0,1],[1,0],[1,1]])
    expected_output = np.array([0,0,0,1])

    # variation des poids de synapses
    error_value  = np.zeros((10,10)) #for every weight calc the error val
    print(error_value)
    for w1 in range(-5,5):
        for w2 in range (-5,5):
            error_delta = 0 #addition of error for every input, reset for each weight configuration

            for input in range(0, len(input_choice)):
                a1 = input_choice[input][0]
                a2 = input_choice[input][1]

                perceptron_output_value = a1*w1 + a2*w2    #value yi 
                error_delta += 1/2*math.pow((perceptron_output_value - expected_output[input]),2) #error = epsilon i ..yi-ti 
            error_delta = error_delta
            error_value[5+w1][5+w2] = float(error_delta)
    print(error_value)


    
if __name__ == '__main__':
    main()
    
