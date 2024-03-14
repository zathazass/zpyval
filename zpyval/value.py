class Value:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value
    
    def __call__(self):
        return self.value
    
    def __str__(self):
        return str(self.value)
    
    __repr__ = __str__