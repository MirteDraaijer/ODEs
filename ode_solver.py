import math
import matplotlib.pyplot as plt
import random

class ode_solver:
    def __init__(self, volume, n, delta_t):
        self.volume = volume
        self.n = n
        self.delta_t = delta_t

    def __str__(self):
        return f'Start volume: {self.volume}, aantal dagen: {self.n}, stapgrootte: {self.delta_t}'
    
    def lineair(self, c):
        def model(volume):
            return volume + c
        return self.runge_kutta_solver(model)

    def exponentieel_toenemend(self, c):
        def model(volume):
            return c * volume
        return self.runge_kutta_solver(model)

    def mendelsohn(self, c, d):
        def model(volume):
            volume = max(volume, 1e-12)
            volume = min(volume, 1e150)
            return c * (volume ** d)
        return self.runge_kutta_solver(model)

    def exponentieel_afvlakkend(self, c, max_volume):
        def model(volume):
            return c * (max_volume - volume)
        return self.runge_kutta_solver(model)
        
    def logistisch(self, c, max_volume):
        def model(volume):
            return c * volume * (max_volume - volume)

        return self.runge_kutta_solver(model)

    def montroll(self, c, d, max_volume):
        def model(volume):
            safe_volume = max(volume, 1e-6)
            safe_max = max(max_volume, safe_volume)
            return c * safe_volume * (math.pow(safe_max, d) - math.pow(safe_volume, d))
        return self.runge_kutta_solver(model)

    def allee(self, c, min_volume, max_volume):
        def model(volume):
            return c * (volume - min_volume) * (max_volume - volume)
        return self.runge_kutta_solver(model)
    
    def lineair_gelimiteerd(self, c, d):
        def model(volume):
            return c * (volume / (volume + d))
        return self.runge_kutta_solver(model)

    def oppervlakte_gelimiteerd(self, c, d):
        def model(volume):
            return c * ((volume + d) / 3)
        return self.runge_kutta_solver(model)

    def von_bertalanffy(self, c, d):
        def model(volume):
            safe_volume = max(volume, 0)
            return (c * math.pow(safe_volume, 2/3) - d * volume)
        return self.runge_kutta_solver(model)

    def gompertz(self, c, volume_max):
        volume_max = max(volume_max, 1e-12)
        model = lambda v: c * v * math.log(volume_max / v) if v > 1e-6 else 0
        return self.runge_kutta_solver(model)

    def runge_kutta_solver(self, model):
        t = 0.0
        y = self.volume
        dagen = [t]
        volumes = [y]

        for i in range (int(self.n)):
            dydt1 = model(y)
            y1 = y + 0.5 * dydt1 * self.delta_t

            dydt2 = model(y1)
            y2 = y + 0.5 * dydt2 * self.delta_t

            dydt3 = model(y2)
            y3 = y + dydt3 * self.delta_t

            dydt4 = model(y3)
            t = t + self.delta_t
            y = y + (dydt1 + 2.0 * dydt2 + 2.0 * dydt3 + dydt4) / 6.0 * self.delta_t

            dagen.append(t)
            volumes.append(y)
        return dagen, volumes

    
    def fit(self, echte_volumes, model, params0):
        params = params0.copy()
        
        def MSE_calc(echte_vol, **params):
            squared_sum = 0.0
            dagen, predicted = model(**params)
            for echte_vol, predicted_vol in zip(echte_vol,predicted):
                error = echte_vol-predicted_vol
                squared_sum += (error*error)
            result = squared_sum/len(predicted)
            return result
        
        mse = MSE_calc(echte_volumes, **params)
        attempts = 0
        while attempts < 1000:
            attempts += 1
            new_params = {key: val + random.gauss(0, 0.01) for key , val in params.items()}
            new_mse = MSE_calc(echte_volumes,**new_params)
            if new_mse<mse:
                params = new_params
                mse = new_mse
                attempts = 0


        return params, mse
    
    def aic(self, mse, n, k):
        aic_waarde = n * math.log(mse) + 2 * k
        return aic_waarde
    
    def bic(self,mse,n,k):
        result = n * math.log(mse) + math.log(n) * k
        return result
 
    def plot(self, dagen, volumes, label):
        plt.plot(dagen, volumes, label = label)
        