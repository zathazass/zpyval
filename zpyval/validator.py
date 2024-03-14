def instance_of(value, klass, message=''):
    if not isinstance(value, klass):
        raise ValueError(message or f'value should be {klass.__name__}')
    

def is_true(cond, message):
    if not cond:
        raise ValueError(message)
    

def not_null(value):
    if value is None:
        raise ValueError('null value not allowed')