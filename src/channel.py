import numpy as np

class AWGNChannel:
    def __init__(self, noise_power):
        self.noise_power = noise_power

    def transmit(self, signal):
        noise = np.random.normal(0, np.sqrt(self.noise_power), signal.shape)
        return signal + noise

    def receive(self, received_signal):
        return received_signal  # Placeholder for processing

# Example usage
if __name__ == '__main__':
    channel = AWGNChannel(noise_power=0.1)
    signal = np.array([1, 0, 1, 0])  # Sample binary signal
    received_signal = channel.transmit(signal)
    print("Received Signal:", received_signal)