import pandas as pd
import numpy as np


def parse():
    largest = 10
    smallest = 10
    data = {"lattice_vector1_x" : [],
                 "lattice_vector1_y" : [],
                 "lattice_vector1_z" : [],
                 "lattice_vector2_x" : [],
                 "lattice_vector2_y" : [],
                 "lattice_vector2_z" : [],
                 "lattice_vector3_x" : [],
                 "lattice_vector3_y" : [] ,
                 "lattice_vector3_z" : [],
                 }
    for i in range(1,81):
        name1 = "atom_x_" + str(i)
        name2 = "atom_y_" + str(i)
        name3 = "atom_z_" + str(i)
        name4 = "atom_type_" + str(i)
        data[name1] = []
        data[name2] = []
        data[name3] = []
        data[name4] = []



    for i in range(1,2401):
        directory = "train/" + str(i) + "/geometry.xyz"

        with open(directory, "r") as f:
            for j, line in enumerate(f):
                if j > 2 :
                    if j > 5:
                        x = float(line.split(" ")[1])
                        y = float(line.split(" ")[2])
                        z = float(line.split(" ")[3])
                        type = (line.split(" ")[4])


                        if x >largest:
                            largest = x
                        if y > largest:
                            largest = y
                        if z > largest:
                            largest = z

                        if x <smallest:
                            smallest = x
                        if y < smallest:
                            smallest = y
                        if z < smallest:
                            smallest = z

                        #if type == "0":
                        #print(line)

                        atom_x = "atom_x_" + str(j - 5)
                        atom_y = "atom_y_" + str(j - 5)
                        atom_z = "atom_z_" + str(j - 5)
                        atom_type = "atom_type_" + str(j - 5)

                        data[atom_x].append(x)
                        data[atom_y].append(y)
                        data[atom_z].append(z)
                        data[atom_type].append(type)


                    else:
                        lat_x = "lattice_vector" + str(j - 2) + "_x"
                        lat_y = "lattice_vector" + str(j - 2) + "_y"
                        lat_z = "lattice_vector" + str(j - 2) + "_z"
                        data[lat_x].append(float(line.split(" ")[1]))
                        data[lat_y].append(float(line.split(" ")[2]))
                        data[lat_z].append(float(line.split(" ")[3]))


    for key in data:
        while len(data[key]) < 2400:
            data[key].append(0)

    train = pd.DataFrame(data=data)

    for i in range(1, 81):
        name = "atom_type_" + str(i)
        #p = pd.get_dummies(train[name])



        del train[name]
        #train = pd.concat([train , p], axis= 1)

    #train = (train - train.mean()) / (train.max() - train.min())

    print largest
    print smallest



    return train

parse()