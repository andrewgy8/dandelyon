import warnings
from datetime import datetime


class warn(object):

    def __init__(self, message):
        self.message = message

    def __call__(self, f):

        def wrapped_f(*args, **kwargs):
            warnings.warn("{} is a deprecated function. {}"
                          .format(f.__name__, self.message),
                          category=DeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)
            return f(*args, **kwargs)
        return wrapped_f


class alias(object):

    def __init__(self, ff):
        self.ff = ff

    def __call__(self, f):

        def wrapped_f(*args, **kwargs):
            return self.ff(*args, **kwargs)
        return wrapped_f


class countdown(object):
    """
    Like alias(), it shuttles the function,
    but based on a time factor and throws a warning message.
    :param expires:
    :param message:
    :param ff:
    :return:
    """
    def __init__(self, expires, message, ff):
        self.expires = expires
        self.message = message
        self.ff = ff

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            date_time = self.expires.strftime("%d-%m-%Y")
            warnings.warn("{} is a deprecated function and it "
                          "will be removed by {}. {}"
                          .format(f.__name__, date_time, self.message),
                          category=PendingDeprecationWarning,
                          stacklevel=2)
            warnings.simplefilter('default', PendingDeprecationWarning)
            if datetime.now() < self.expires:
                return f(*args, **kwargs)
            else:
                return self.ff(*args, **kwargs)
        return wrapped_f
