import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coordinates using Haversine formula"""
    R = 6371  # Earth's radius in kilometers
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return R * c

def filter_providers_by_distance(providers, user_lat, user_lon, max_distance_km=50):
    """Filter providers within specified distance"""
    filtered = []
    for provider in providers:
        if provider.latitude and provider.longitude:
            distance = calculate_distance(user_lat, user_lon, provider.latitude, provider.longitude)
            if distance <= max_distance_km:
                provider.distance = round(distance, 2)
                filtered.append(provider)
    
    return sorted(filtered, key=lambda p: p.distance)