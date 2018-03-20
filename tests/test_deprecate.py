import unittest
import warnings

from dandelion import deprecator


class TestDeprecateWarning(unittest.TestCase):

    def test_throws_warning(self):
        with warnings.catch_warnings(record=True) as w:
            @deprecator.blow(message='This will deprecate.')
            def foo():
                return ''
            foo()
            assert "deprecate" in str(w[-1].message)


class TestShuttleFunction(unittest.TestCase):

    def test_shuttle_function_without_params(self):
        def bar():
            return 'This is new'

        @deprecator.in_the_wind(ff=bar)
        def foo():
            return 'This is old'

        res = foo()

        assert res == 'This is new'

    def test_shuttle_function_with_params(self):
        def bar(bar):
            return 'This is new {}'.format(bar)

        @deprecator.in_the_wind(ff=bar)
        def foo(bar):
            return 'This is old {}'.format(bar)

        res = foo('function')

        assert res == 'This is new function'

    def test_shuttle_function_with_extra_params(self):
        def bar(bar, baz):
            return 'This is new {} {}'.format(bar, baz)

        @deprecator.in_the_wind(ff=bar)
        def foo(bar):
            return 'This is old {}'.format(bar)

        res = foo('function', 'junction')

        assert res == 'This is new function junction'
