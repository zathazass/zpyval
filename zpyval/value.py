from zpyval.validator import (
    instance_of, is_true, contains, not_blank, allow_null
)

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

class Gender(Value):
    female_choices = ['F', 'f', 'female', 'Female', 'FEMALE']
    male_choices = ['M', 'm', 'male', 'Male', 'MALE']
    female_str = 'female'
    male_str = 'male'

    @property
    def value(self):
        value = super().value
        if value in self.female_choices:
            return self.female_str
        if value in self.male_choices:
            return self.male_str
        return value

    def validate(self):
        if allow_null(self.value): return
        not_blank(self.value)
        contains(self.value, self.female_choices + self.male_choices)
