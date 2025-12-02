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
    
    def lineair_example(self,c):
        def model():
            return self.volume + (c*self.delta_t)
        return self.solver(model())

    # @DeprecationWarning
    # def ode_looper(self,c):
    #     dagen = []
    #     volumes = []
    #     t = 0
    #     for i in range(self.n):
    #         if i == 0:
    #             t += self.delta_t
    #             delta_volume = mt.lineair(self.volume, c, self.delta_t)
    #             dagen.append(t)
    #             volumes.append(delta_volume)
    #         else:
    #             t += self.delta_t
    #             delta_volume = mt.lineair(volumes[i-1], c, self.delta_t)
    #             dagen.append(t)
    #             volumes.append(delta_volume)

    #     return dagen, volumes

    # Volgens mij is dit Euler solver:
    # def solver(self, model):
    #     t = 0
    #     volume = self.volume
    #     dagen = [t]
    #     volumes = [volume]

    #     for i in range(self.n):
    #         t += self.delta_t
    #         delta_volume = model(volume)
    #         volume += delta_volume

    #         dagen.append(t)
    #         volumes.append(volume)
    #     return dagen, volumes
    # Runge-Kutta is beter, die proberen te gebruiken

    def lineair(self, c, volume):
        def model(y):
            return y + c
        return self.runge_kutta_solver(model, volume)

    def exponentieel_toenemend(self, c, volume):
        def model(y):
            return c * y
        return self.runge_kutta_solver(model, volume)

    # @DeprecationWarning
    # def mendelsohn_testmodel(self,c):
    #     dagen = []
    #     volumes = []
    #     t = self.delta_t
    #     for i in range(self.n):
    #         if i == 0:
    #             t += self.delta_t
    #             delta_volume = mt.mendelsohn(self.volume, c, self.delta_t)
    #             dagen.append(t)
    #             volumes.append(delta_volume)
    #         else:
    #             t += self.delta_t
    #             delta_volume = mt.mendelsohn(volumes[i-1], c, self.delta_t)
    #             dagen.append(t)
    #             volumes.append(delta_volume)

    #     return dagen,volumes

    def mendelsohn(self, c, d, volume):
        def model(y):
            return c * math.pow(y, d)
        return self.runge_kutta_solver(model, volume)

    def exponentieel_afvlakkend(self, c, max_volume, volume):
        def model(y):
            return c * (max_volume - y)
        return self.runge_kutta_solver(model, volume)
        
    def logistisch(self, c, max_volume, volume):
        def model(y):
            return c * y * (max_volume - y)

        return self.runge_kutta_solver(model, volume)

    def montroll(self, c, d, max_volume, volume):
        def model(y):
            safe_volume = max(y, 1e-6)
            safe_max = max(max_volume, safe_volume)
            return c * safe_volume * (math.pow(safe_max, d) - math.pow(safe_volume, d))
        return self.runge_kutta_solver(model, volume)

    def allee(self, c, min_volume, max_volume, volume):
        def model(y):
            return c * (y - min_volume) * (max_volume - y)
        return self.runge_kutta_solver(model, volume)
    
    def lineair_gelimiteerd(self, c, d, volume):
        def model(y):
            return c * (y / (y + d))
        return self.runge_kutta_solver(model, volume)

    def oppervlakte_gelimiteerd(self, c, d, volume):
        def model(y):
            return c * ((y + d) / 3)
        return self.runge_kutta_solver(model, volume)

    def von_bertalanffy(self, c, d, volume):
        def model(y):
            safe_volume = max(y, 0)
            return (c * math.pow(safe_volume, 2/3) - d * y)
        return self.runge_kutta_solver(model, volume)

    def gompertz(self, c, volume_max, volume):
        def model(y):
            if y <= 0:
                y = 1e-6
            log_calc = math.log((volume_max / y))
            result = c * y * log_calc
            return result
        return self.runge_kutta_solver(model, volume)

    def runge_kutta_solver(self, model, volume):
        t = 0.0
        y = volume
        dagen = [t]
        volumes = [y]

        for i in range (int(self.n)):
            dydt1 = model(y)
            y1 = y + 0.5 * dydt1 * self.delta_t

            dydt2 = model(y1)
            y2 = y + 0.5 * dydt2 * self.delta_t

            dydt3 = model(y2)
            y3 = y + dydt2 * self.delta_t

            dydt4 = model(y3)
            t = t + self.delta_t
            y = y + (dydt1 + 2.0 * dydt2 + 2.0 * dydt3 + dydt4) / 6.0 * self.delta_t

            dagen.append(t)
            volumes.append(y)
        return dagen, volumes

    # def runge_kutta(self, a, b):
    #     def ODE(t, y):
    #         return a * y + b
    #     t = 0.0
    #     y = self.volume
    #     dagen = [t]
    #     volumes = [y]

    #     for i in range (self.n):
    #         dydt1 = ODE(t, y)
    #         y1 = y + 0.5 * dydt1 * self.delta_t

    #         dydt2 = ODE(t, y1)
    #         y2 = y + 0.5 * dydt2 * self.delta_t

    #         dydt3 = ODE(t, y2)
    #         y3 = y + dydt2 * self.delta_t

    #         dydt4 = ODE(t, y3)
    #         t = t + self.delta_t
    #         y = y + (dydt1 + 2.0 * dydt2 + 2.0 * dydt3 + dydt4) / 6.0 * self.delta_t

    #         dagen.append(t)
    #         volumes.append(y)
    #     return dagen, volumes
    
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
        while attempts < 10000:
            attempts += 1
            new_params = {key: val + random.gauss(sigma=0.1) for key , val in params.items()}
            new_mse = MSE_calc(echte_volumes,**new_params)
            if new_mse<mse:
                params = new_params
                mse = new_mse
                attempts = 0


        return params, mse
    
    def aic(self, mse, n, k):
        aic_waarde = n * math.log(mse) + 2 * k
        return aic_waarde
 
    def plot(self, dagen, volumes, label):
        plt.plot(dagen, volumes, label = label)
        