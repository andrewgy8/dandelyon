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
