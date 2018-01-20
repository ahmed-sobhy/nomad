import pandas as pd
import numpy as np


SIZE_X = 25
SIZE_Y = 25
SIZE_Z = 25
CHANNELS = 4

largest = 24.5068695497
smallest = -2.06731332728

RES = (largest - smallest) / SIZE_X

train = np.zeros((2400, SIZE_X, SIZE_Y, SIZE_Z, CHANNELS))

def parse():
    for i in range(2400):
        directory = "train/" + str(i+1) + "/geometry.xyz"

        with open(directory, "r") as f:
            for j, line in enumerate(f):
                if j > 5:
                    elem_type =  line.rstrip('\n').split(" ")[4]
                    x = float(line.split(" ")[1])
                    y = float(line.split(" ")[2])
                    z = float(line.split(" ")[3])

                    x = max(min(int((x - smallest)/RES), SIZE_X-1), 0)
                    y = max(min(int((y - smallest) / RES), SIZE_X-1), 0)
                    z = max(min(int((z - smallest) / RES), SIZE_X-1), 0)



                    if elem_type == 'O':
                        c = 0
                        train[i, x, y, z, c] = 1
                    elif elem_type == 'Ga':
                        c = 1
                        train[i, x, y, z, c] = 1
                    elif elem_type == 'Al':
                        c = 2
                        train[i, x, y, z, c] = 1
                    else:
                        c = 3
                        train[i, x, y, z, c] = 1

    return train


parse()