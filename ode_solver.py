import math
import matplotlib.pyplot as plt

class ode_solver:
    def __init__(self, volume, n, delta_t):
        self.volume = volume
        self.n = n
        self.delta_t = delta_t

    def __str__(self):
        return f'Start volume: {self.volume}, aantal dagen: {self.n}, stapgrootte: {self.delta_t}'

    def lineair(self):
        pass

    def exponentieel_toenemend(self, c):
        dagen = []
        volumes = []
        t = 0

        for i in range(self.n):
            t = t + self.delta_t
            delta_volume = c * self.volume * self.delta_t
            self.volume = self.volume + delta_volume

            dagen.append(t)
            volumes.append(self.volume)
        
        return dagen, volumes

    def mendelsohn(self):
        pass

    def exponentieel_afvlakkend(self, c, max_volume):
        dagen = []
        volumes = []
        t = 0

        for i in range(self.n):
            t = t + self.delta_t
            delta_volume = c * (max_volume - self.volume) * self.delta_t
            self.volume = self.volume + delta_volume

            dagen.append(t)
            volumes.append(self.volume)

        return dagen, volumes
        

    def logistisch(self):
        pass

    def montroll(self, c, d, max_volume):
        dagen = []
        volumes = []
        t = 0

        for i in range(self.n):
            t = t + self.delta_t
            delta_volume = c * self.volume * (math.pow(max_volume, d) - math.pow(self.volume, d)) * self.delta_t
            self.volume = self.volume + delta_volume

            dagen.append(t)
            volumes.append(self.volume)

        return dagen, volumes

    def allee(self):
        pass

    def lineair_gelimiteerd(self, c, d):
        dagen = []
        volumes = []
        t = 0

        for i in range(self.n):
            t = t + self.delta_t
            delta_volume = c * (self.volume / (self.volume + d)) * self.delta_t
            self.volume = self.volume + delta_volume

            dagen.append(t)
            volumes.append(self.volume)

        return dagen, volumes

    def oppervlakte_gelimiteerd(self):
        pass

    def von_bertalanffy(self, c, d):
        dagen = []
        volumes = []
        t = 0

        for i in range(self.n):
            t = t + self.delta_t
            delta_volume = c * math.pow(self.volume, 2/3) - d * self.volume * self.delta_t
            self.volume = self.volume + delta_volume

            dagen.append(t)
            volumes.append(self.volume)

        return dagen, volumes

    def gompertz(self):
        pass
    
    def plot(self, dagen, volumes):
        plt.plot(dagen, volumes)
        plt.show