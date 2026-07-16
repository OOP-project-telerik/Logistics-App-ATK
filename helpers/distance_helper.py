LOCATIONS = ('SYD', 'MEL', 'ADL', 'ASP', 'BRI', 'DAR', 'PER')

# Distances in km. Each unordered pair stored once, keyed by a sorted tuple
# of the two location codes, so SYD-MEL and MEL-SYD share one entry.
_DISTANCES = {
    ('MEL', 'SYD'): 877,
    ('ADL', 'SYD'): 1376,
    ('ASP', 'SYD'): 2762,
    ('BRI', 'SYD'): 909,
    ('DAR', 'SYD'): 3935,
    ('PER', 'SYD'): 4016,
    ('ADL', 'MEL'): 725,
    ('ASP', 'MEL'): 2255,
    ('BRI', 'MEL'): 1765,
    ('DAR', 'MEL'): 3752,
    ('MEL', 'PER'): 3509,
    ('ADL', 'ASP'): 1530,
    ('ADL', 'BRI'): 1927,
    ('ADL', 'DAR'): 3027,
    ('ADL', 'PER'): 2785,
    ('ASP', 'BRI'): 2993,
    ('ASP', 'DAR'): 1497,
    ('ASP', 'PER'): 2481,
    ('BRI', 'DAR'): 3426,
    ('BRI', 'PER'): 4311,
    ('DAR', 'PER'): 4025,
}


def get_distance(start: str, end: str) -> int:
    """Return the distance in km between two location codes."""
    if start not in LOCATIONS or end not in LOCATIONS:
        raise ValueError("City doesn't exist! Please enter a valid city name")
    
    key = tuple(sorted((start,end)))
    return _DISTANCES[key]


def get_distances_for_stops(stops: list) -> list:
    """Given an ordered list of stops, e.g. ['BRI', 'SYD', 'MEL'],
    return the list of consecutive distances, e.g. [909, 877].
    This is what a route's `distances` list is built from."""
    distances = []
    for i in range(len(stops) -1):
        distances.append(get_distance(stops[i], stops[i+1]))
    return distances
