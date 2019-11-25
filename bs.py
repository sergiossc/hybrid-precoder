import numpy as np
import uuid
class bs:
    def __init__(self, number_of_antennas):
        self.number_of_antennas = number_of_antennas
        self.id = uuid.uuid4()

    def set_steering_vector(self):
        self.steering_vector = np.zeros(self.number_of_antennas, 1)

    def set_number_of_rf_chains(self, number_of_rf_chains):
        self.number_of_rf_chains = number_of_rf_chains

    def set_baseband_precoder(self, number_of_datastreams):
        self.baseband_precoder = np.zeros((self.number_of_rf_chains, number_of_datastreams))
