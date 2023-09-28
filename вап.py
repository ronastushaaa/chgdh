class J:
    min = 10
    max = 100

    def __init__(self, k):
        self.k = k

    def double(self):
        return self.k * 2

    @classmethod
    def validate(cls,x):
        return cls.min < x < cls.max

    @staticmethod
    def double_validate( x):
        return J.min*2 < x < J.max*2



