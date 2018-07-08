import warnings
from datetime import datetime


class Deprecator:
    """
    Base deprecation class used to contain logic 
    controller and warning functions.
    """
    def __init__(self, message):
        self.message = message

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            return self.logic_wrapper(f, *args, **kwargs)
        return wrapped_f

    def logic_wrapper(self, f, *args, **kwargs):
        pass

    def throw_warning(self, f):
        if self.message:
            Deprecator._warn(self.message)
            return
        Deprecator._warn("{} is a deprecated function. {}"
                         .format(f.__name__, self.message))

    def throw_expiry_warning(self, f, date_time):
        if not self.message:
            return None

        Deprecator._warn("{} is a deprecated function and it "
                          "will be removed by {}. {}"
                         .format(f.__name__, date_time, self.message))

    @staticmethod
    def _warn(message_str):
        warnings.warn(message_str,
                      category=PendingDeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', PendingDeprecationWarning)


class FastForward(Deprecator):
    """
    Fast-forward class. Used for pushing a function to another
    when the user designates that the function is deprecated.
    """
    def __init__(self, message, ff):
        super().__init__(message)
        self.ff = ff


class warn(Deprecator):
    """
    Blows a standard warning at the user.

    :param message:
    :return:
    """
    def __init__(self, message):
        super().__init__(message)

    def logic_wrapper(self, f, *args, **kwargs):
        self.throw_warning(f)
        return f(*args, **kwargs)


@warn(message='Please change the import path to dandelyon.deprecators')
class alias(FastForward):
    """
    Shuttles a function from the deprecated function
    to another valid function specified by the user.

    :param ff:
    :return:
    """
    def __init__(self, ff):
        super().__init__(message=None, ff=ff)

    def logic_wrapper(self, f, *args, **kwargs):
        return self.ff(*args, **kwargs)


@warn(message='Please change the import path to dandelyon.deprecators')
class countdown(FastForward):
    """
    Like alias(), it shuttles the function,
    but based on a time factor and throws a warning message.

    :param expires:
    :param message:
    :param ff:
    :return:
    """
    _CALLED = None

    def __init__(self, expires, message, ff):
        super().__init__(message=message, ff=ff)
        self.expires = expires

    def logic_wrapper(self, f, *args, **kwargs):
        if self._CALLED:
            return self.shuttle(f, *args, **kwargs)

        date_time = self.expires.strftime("%d-%m-%Y")

        self.throw_expiry_warning(f, date_time)
        self._CALLED = True

        return self.shuttle(f, *args, **kwargs)

    def shuttle(self, f, *args, **kwargs):
        if datetime.now() < self.expires:
            return f(*args, **kwargs)
        return self.ff(*args, **kwargs)
