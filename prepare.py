import pandas as pd

def prepare():
    train = pd.read_csv("train.csv")

    labels = train[['formation_energy_ev_natom','bandgap_energy_ev']]
    del train['formation_energy_ev_natom']
    del train['bandgap_energy_ev']
    #train = (train - train.mean()) / (train.max() - train.min())
    return train, labels.as_matrix()

