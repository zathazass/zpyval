from zpyval.validator import (
    instance_of, is_true, contains, not_blank, allow_null, not_null,
    matches_pattern
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
    teenage_range = (11, 20)
    adult_age = 18
    min_age = 0
    max_age = 150

    def validate(self):
        instance_of(self.value, int, 'invalid age')
        is_true(self.value > self.min_age, f'age should be greater than {self.min_age}')
        is_true(self.value <= self.max_age, f'maximum age limit is {self.max_age}')

    def is_teenage(self):
        return (self.value >= self.teenage_range[0]) \
               and (self.value < self.teenage_range[1])
    
    def is_adult(self):
        return self.value > self.adult_age

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


class Username(Value):
    pattern = r'^[A-Za-z]+[A-Za-z0-9@_]*$'
    pattern_message = 'Username should startswith A-Za-z and allow only @_ as special chars.'
    
    def validate(self):
        not_null(self.value)
        instance_of(self.value, str, 'username should be str')
        not_blank(self.value)
        matches_pattern(self.pattern, self.value, self.pattern_message)


class Active(Value):
    truthy_values = [1, True, 'true', 'on']
    falsy_values = [0, False, 'false', 'off']

    @property
    def value(self):
        value = super().value
        if value in self.truthy_values:
            return True
        elif value in self.falsy_values:
            return False
        return value
    
    def validate(self):
        not_null(self.value)
        not_blank(self.value)
        contains(self.value, self.truthy_values + self.falsy_values)


class Email(Value):
    known_domains = ['gmail', 'yahoo', 'rediff', 'outlook']
    pattern = r'^[a-zA-Z._+-]+[a-zA-Z0-9._+-]*@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*(\.[a-zA-Z]{2,})$'

    @property
    def value(self):
        value = str(super().value)
        return value.lower()

    def validate(self):
        instance_of(self.value, str, 'email should be string')
        not_blank(self.value)
        matches_pattern(self.pattern, self.value, 'invalid email')

    def is_work(self):
        return not self.is_public()
    
    def is_public(self):
        for i in self.known_domains:
            if f'@{i}.' in self.value:
                return True
        return False
    
    def domain(self):
        return self.value.split('@')[1].split('.')[0]
    
    def tld(self):
        return self.value.rpartition('.')[-1]
