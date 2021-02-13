import numpy as np


class Utility:
    
    def generate_sensing_matrix(seed, n_rows, n_cols):
        np.random.seed(seed)
        return np.random.randn(n_rows, n_cols)

    def generate_secret_value(seed, sens_priv_num):
        return seed/sens_priv_num
