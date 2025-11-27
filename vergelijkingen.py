from math import log

def lineair(volume,c,t):
    result = volume + (c*t)
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