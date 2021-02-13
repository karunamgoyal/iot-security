import numpy as np
from utils import Utility


class Encryption_CS:
    
    def encrypt(seed, sens_priv_num, c_factor, sensor_data):
        data_size = np.size(sensor_data)
        sensing_matrix = Utility.generate_sensing_matrix(seed, round((1 - c_factor) * data_size), data_size)
        compressed_data = np.dot(sensing_matrix, sensor_data)
        return compressed_data * Utility.generate_secret_value(seed, sens_priv_num)
