from math import radians, cos, sin, atan2, sqrt


def find_haversine_distance(lat1, lon1, lat2, lon2):
    radius = 6371
    dif_lat = radians(lat2-lat1)
    dif_lon = radians(lon2-lon1)
    a = pow(sin(dif_lat/2), 2)+cos(radians(lat1)) * \
        cos(radians(lat2))*pow(sin(dif_lon/2), 2)
    c = 2*atan2(sqrt(a), sqrt(1-a))
    d = radius*c
    return d
