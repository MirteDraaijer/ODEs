from math import log

def lineair(volume,c,t):
    result =  volume+ (c*t)
    print(f'{c=}'.split('=')[0])
    print(f'{c=}')
    return result

def mendelsohn(volume,c,t,d):
    result = c*(volume^d)*t
    return result

def logistische_groei(volume,c,t,max_volume):
    result = c*volume*(max_volume-volume)*t
    return result

def allee(volume,c,t,max_volume,min_volume):
    result = c*(volume-min_volume)*(max_volume-volume)*t
    return result

def opper_vlakte_lim_groei(volume,c,t,d):
    result = c*((volume+d)/3)*t
    return result

def gompertz(volume,c,t,volume_max):
    log_calc = log((volume_max/volume))
    result = c*volume*log_calc*t
    return result

# depcricated functies from ode solver
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

    def lineair_example(self,c):
        def model():
            return self.volume + (c*self.delta_t)
        return self.solver(model())