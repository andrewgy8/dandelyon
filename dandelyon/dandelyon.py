import warnings
from datetime import datetime


class Deprecator(object):
    def __init__(self, message):
        self.message = message

    def throw_warning(self, f):
        warnings.warn("{} is a deprecated function. {}"
                      .format(f.__name__, self.message),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)

    def throw_expiry_warning(self, f, date_time):
        warnings.warn("{} is a deprecated function and it "
                      "will be removed by {}. {}"
                      .format(f.__name__, date_time, self.message),
                      category=PendingDeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', PendingDeprecationWarning)


class warn(Deprecator):
    """
    Blows a warning at the user
    :param message: 
    :return: 
    """
    def __init__(self, message):
        super().__init__(message)

    def __call__(self, f):

        def wrapped_f(*args, **kwargs):
            self.throw_warning(f)

            return f(*args, **kwargs)
        return wrapped_f


class alias(object):
    """
    Shuttles a function from the deprecated function 
    to another valid function specified by the user
    :param ff: 
    :return: 
    """
    def __init__(self, ff):
        self.ff = ff

    def __call__(self, f):

        def wrapped_f(*args, **kwargs):
            return self.ff(*args, **kwargs)
        return wrapped_f


class countdown(Deprecator):
    """
    Like alias(), it shuttles the function,
    but based on a time factor and throws a warning message.
    :param expires:
    :param message:
    :param ff:
    :return:
    """
    def __init__(self, expires, message, ff):
        super().__init__(message)
        self.expires = expires
        self.ff = ff

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            date_time = self.expires.strftime("%d-%m-%Y")

            self.throw_expiry_warning(f, date_time)

            if datetime.now() < self.expires:
                return f(*args, **kwargs)
            else:
                return self.ff(*args, **kwargs)
        return wrapped_f
