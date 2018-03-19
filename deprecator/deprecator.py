import warnings
from datetime import datetime


def warn(message):
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            warnings.warn("{} is a deprecated function. {}".format(func.__name__, message),
                          category=DeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)
            return func(*args, **kwargs)
        return deprecated_func
    return deprecated_decorator


def time_bomb(expires, message, ff):
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


def shuttle(ff):
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            return ff(*args, **kwargs)
        return deprecated_func
    return deprecated_decorator


