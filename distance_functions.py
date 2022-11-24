#Gal Levy 208540872
from ways.tools import compute_distance

def cost_function(x, y):
    return x+y

def huristic_function(lat1, lon1, lat2, lon2):
    return compute_distance(lat1, lon1, lat2, lon2) / 110