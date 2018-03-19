import unittest
import warnings

from deprecator import deprecator


class TestDeprecateWarning(unittest.TestCase):

    def test_throws_warning(self):
        with warnings.catch_warnings(record=True) as w:
            @deprecator.warn(message='This will deprecate.')
            def foo():
                return ''
            foo()
            assert "deprecate" in str(w[-1].message)
