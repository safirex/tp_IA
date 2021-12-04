import Character as ch
import Army as arm
import numpy as np
import pandas as pd
import random as rd

CSVPATH ="characters.csv"
rd.seed(15)



def main():


    data = pd.read_csv(CSVPATH, header=None)
    characters = []
    # Discover, visualize, and preprocess data using pandas if needed.
    data = data.to_numpy()
    moral_sum = 0
    for datarow in data[1:]:
        char = ch.Character(datarow)
        random = rd.random()*80+20
        moral_sum += random
        army = arm.Army(random,char.morale_value)
        char.setArmy(army)
        characters.append(char)

    print(moral_sum)

if __name__ == '__main__':
    main()
    
