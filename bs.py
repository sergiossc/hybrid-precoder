import numpy as np
import uuid
class bs:
    """
    This is a BS device with Uniform Linear Antenna (ULA) Array. 
    """
    def __init__(self, number_of_tx_antennas, number_of_rx_antennas):
        self.number_of_tx_antennas = number_of_tx_antennas
        self.number_of_rx_antennas = number_of_rx_antennas
        self.id = uuid.uuid4()

    def set_steering_vector(self, signal_transmited):
        self.steering_vector = np.zeros(self.number_of_tx_antennas)

    def set_receiving_vector(self):
        self.receiving_vector = np.zeros(self.number_of_rx_antennas)

    def set_number_of_rf_chains(self, number_of_rf_chains):
        self.number_of_rf_chains = number_of_rf_chains

    def set_number_of_datastreams(self, number_of_datastreams):
        self.number_of_datastreams = number_of_rf_chains

    def set_baseband_precoder(self, number_of_datastreams):
        self.baseband_precoder = np.zeros((self.number_of_rf_chains, number_of_datastreams))

    def set_rf_precoder(self, number_of_datastreams):
        self.baseband_precoder = np.zeros((self.number_of_antennas, self.number_of_rf_chains))


my_bs = bs(4, 4)

print(my_bs.id)
my_bs.set_steering_vector()
print(my_bs.steering_vector)
