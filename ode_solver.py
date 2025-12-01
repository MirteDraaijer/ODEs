import math
import matplotlib.pyplot as plt
import vergelijkingen as mt
import random

class ode_solver:
    def __init__(self, volume, n, delta_t):
        self.volume = volume
        self.n = n
        self.delta_t = delta_t

    def __str__(self):
        return f'Start volume: {self.volume}, aantal dagen: {self.n}, stapgrootte: {self.delta_t}'
    
    def lineair_example(self,c):
        def model():
            return self.volume + (c*self.delta_t)
        return self.solver(model())

    @DeprecationWarning
    def ode_looper(self,c):
        dagen = []
        volumes = []
        t = 0
        for i in range(self.n):
            if i == 0:
                t += self.delta_t
                delta_volume = mt.lineair(self.volume, c, self.delta_t)
                dagen.append(t)
                volumes.append(delta_volume)
            else:
                t += self.delta_t
                delta_volume = mt.lineair(volumes[i-1], c, self.delta_t)
                dagen.append(t)
                volumes.append(delta_volume)

        return dagen, volumes

    def solver(self, model):
        dagen = []
        volumes = []
        t = 0

        for i in range(self.n):
            t += self.delta_t
            delta_volume = model()
            self.volume += delta_volume

            dagen.append(t)
            volumes.append(self.volume)
        return dagen, volumes

    def lineair(self,c):
        def model():
            return self.volume + (c*self.delta_t)
        return self.solver(model)

    def exponentieel_toenemend(self, c):
        def model():
            return c * self.volume * self.delta_t
        return self.solver(model)

    @DeprecationWarning
    def mendelsohn_testmodel(self,c):
        dagen = []
        volumes = []
        t = self.delta_t
        for i in range(self.n):
            if i == 0:
                t += self.delta_t
                delta_volume = mt.mendelsohn(self.volume, c, self.delta_t)
                dagen.append(t)
                volumes.append(delta_volume)
            else:
                t += self.delta_t
                delta_volume = mt.mendelsohn(volumes[i-1], c, self.delta_t)
                dagen.append(t)
                volumes.append(delta_volume)

        return dagen,volumes

    def mendelsohn(self,c,d):
        def model():
            return c*(self.volume^d)*self.delta_t
        return self.solver(model())


    def exponentieel_afvlakkend(self, c, max_volume):
        def model():
            return c * (max_volume - self.volume) * self.delta_t
        return self.solver(model)
        
    def logistisch(self,c,max_volume):
        def model():
            return c*self.volume*(max_volume-self.volume)*self.delta_t

        return self.solver(model)

    def montroll(self, c, d, max_volume):
        def model():
            return c * self.volume * (math.pow(max_volume, d) - math.pow(self.volume, d)) * self.delta_t
        return self.solver(model)

    def allee(self, c, min_volume, max_volume):
        def model():
            return c*(self.volume-min_volume) * (max_volume-self.volume)*self.delta_t
        return self.solver(model)
    
    def lineair_gelimiteerd(self, c, d):
        def model():
            return c * (self.volume / (self.volume + d)) * self.delta_t
        return self.solver(model)

    def oppervlakte_gelimiteerd(self,c,d):
        def model():
            return c*((self.volume+d)/3)*self.delta_t
        return self.solver(model)

    def von_bertalanffy(self, c, d):
        def model():
            return (c * math.pow(self.volume, 2/3) - d * self.volume) * self.delta_t
        return self.solver(model)

    def gompertz(self,c,volume_max):
        def model():
            log_calc = math.log((volume_max/self.volume))
            result = c*self.volume*log_calc*self.delta_t
            return result
        return self.solver(model)
    
    def runge_kutta(self, a, b):
        def ODE(t, y):
            return a * y + b
        t = 0.0
        y = self.volume
        dagen = [t]
        volumes = [y]

        for i in range (self.n):
            dydt1 = ODE(t, y)
            y1 = y + 0.5 * dydt1 * self.delta_t

            dydt2 = ODE(t, y1)
            y2 = y + 0.5 * dydt2 * self.delta_t

            dydt3 = ODE(t, y2)
            y3 = y + dydt2 * self.delta_t

            dydt4 = ODE(t, y3)
            t = t + self.delta_t
            y = y + (dydt1 + 2.0 * dydt2 + 2.0 * dydt3 + dydt4) / 6.0 * self.delta_t

            dagen.append(t)
            volumes.append(y)
        return dagen, volumes
    
    def fit(self,echte_volumes):
        params = {"a": 0.0,"b":0.0}
        
        def MSE_calc(echte_vol,a,b):
            squared_sum = 0.0
            dagen, predicted = self.runge_kutta(a,b)
            for echte_vol, predicted_vol in zip(echte_vol,predicted):
                error = echte_vol-predicted_vol
                squared_sum += (error*error)
            result = squared_sum/len(predicted)
            return result
        
        mse = MSE_calc(echte_volumes, **params)
        attempts = 0
        while attempts < 10000:
            attempts += 1
            new_params = {key: val + random.gauss(sigma=0.1) for key , val in params.items()}
            new_mse = MSE_calc(echte_volumes,**new_params)
            if new_mse<mse:
                params = new_params
                mse = new_mse
                attempts = 0


        return params
 
    def plot(self, dagen, volumes, label):
        plt.plot(dagen, volumes, label = label)