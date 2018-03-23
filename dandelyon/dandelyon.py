import warnings
from datetime import datetime


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
    Shuttles a function from the deprecated function 
    to another valid function specified by the user
    :param ff: 
    :return: 
    """
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            return ff(*args, **kwargs)
        return deprecated_func
    return deprecated_decorator


def spring(expires, message, ff):
    """
    Like in_the_wind(), it shuttles the function, 
    but based on a time factor. 
    :param expires: 
    :param message: 
    :param ff: 
    :return: 
    """
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            date_time = expires.strftime("%d-%m-%Y")
            warnings.warn("{} is a deprecated function and it "
                          "will be destroyed by {}. {}"
                          .format(func.__name__, date_time, message),
                          category=DeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)
            if datetime.now() < expires:
                return func(*args, **kwargs)
            else:
                return ff(*args, **kwargs)
        return deprecated_func
    return deprecated_decorator
