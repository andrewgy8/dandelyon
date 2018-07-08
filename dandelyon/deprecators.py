import sys
from datetime import datetime

from .dandelyon import Deprecator, FastForward


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


class version(Deprecator):
    def __init__(self, py_version, message=None,):
        super().__init__(message)
        self.py_version = py_version

    def logic_wrapper(self, f, *args, **kwargs):
        if sys.version > self.py_version:
            self.throw_warning(f)

        return f(*args, **kwargs)
