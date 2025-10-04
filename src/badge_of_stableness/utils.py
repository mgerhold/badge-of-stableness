def clamp[T: int | float](value: T, min_value: T, max_value: T) -> T:
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
    return max(min(value, max_value), min_value)
