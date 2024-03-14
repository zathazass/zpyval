from zpyval.validator import instance_of, is_true

class Value:
    def __init__(self, value):
        self.__value = value
        self.validate()

    def validate(self):
        pass

    @property
    def value(self):
        return self.__value
    
    def __call__(self):
        return self.value
    
    def __str__(self):
        return str(self.value)
    
    __repr__ = __str__


class Id(Value):
    def validate(self):
        instance_of(self.value, int, 'Id must have integer value')
        is_true(self.value > 0, 'id should be greater than 0')

class Age(Value):
    def validate(self):
        instance_of(self.value, int, 'invalid age')
        is_true(self.value > 0, 'age should be greater than 0')
        is_true(self.value <= 150, 'maximum age limit is 150')

