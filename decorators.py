def check_access(func):
    def wrapper(obj, *args, **kwargs):
        if obj.has_access():
            return func(obj, *args, **kwargs)
        raise Exception('Has access is not True')
    return wrapper
