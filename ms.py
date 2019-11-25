import uuid
class ms:
    def __init__(self, number_of_antennas):
        self.number_of_antennas = number_of_antennas
        self.id = uuid.uuid4()

    def set_receiving_vector(self):
        self.receiving_vector = np.zeros(self.number_of_antennas, 1)
