class Range(object):
    def __init__(self, min: str, max: str):
        self.min = min
        self.max = max

    def __repr__(self) -> str:
        return self.to_str()

    def to_str(self):
        return str({'min': self.min, 'max': self.max})
