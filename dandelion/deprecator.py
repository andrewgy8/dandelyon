import warnings


def blow(message):
    """
    Blows a warning at the user
    :param message: 
    :return: 
    """
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            warnings.warn("{} is a deprecated function. {}".format(func.__name__, message),
                          category=DeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)
            return func(*args, **kwargs)
        return deprecated_func
    return deprecated_decorator


def in_the_wind(ff):
    """
    Shuttles a function from the deprecated function to another
    :param ff: 
    :return: 
    """
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            return ff(*args, **kwargs)
        return deprecated_func
    return deprecated_decorator
