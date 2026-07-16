from helpers.distance_helper import LOCATIONS


def validate_int(value: str, field_name: str) -> int:
    try: 
        return int(value)
    except ValueError:
        raise ValueError(f"{field_name} must be a whole number, got {value}")


def validate_positive_float(value: str, field_name: str) -> float:
    try:
        result = float(value)
    except ValueError:
        raise ValueError(f"{field_name} must be a number, got {value}")

    if result <=0:
        raise ValueError(f"{field_name} must be greater than zero, got {result}")
    return result


def validate_location_code(code: str) -> str:
    if code not in LOCATIONS:
        raise ValueError(f"{code} is not a valid location code: {code}")
    return code
