class Range(object):
    """When prices are particularly volatile, the API may return a range of prices that are possible."""

    """Estimated minimum price (c/kWh)"""
    min: float
    """Estimated maximum price (c/kWh)"""
    max: float

    def __init__(self, min: float, max: float):
        self.min = min
        self.max = max

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str({'min': self.min, 'max': self.max})
