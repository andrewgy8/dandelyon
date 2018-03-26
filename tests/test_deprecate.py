import unittest
import warnings
from datetime import datetime, timedelta

from dandelyon import dandelyon


class TestDeprecateWarning(unittest.TestCase):

    def test_throws_warning(self):
        with warnings.catch_warnings(record=True) as w:
            @dandelyon.warn(message='This will deprecate.')
            def foo():
                return ''
            foo()
            assert "deprecate" in str(w[-1].message)


class TestShuttleFunction(unittest.TestCase):

    def test_shuttle_function_without_params(self):
        def bar():
            return 'This is new'

        @dandelyon.alias(ff=bar)
        def foo():
            return 'This is old'

        res = foo()

        assert res == 'This is new'

    def test_shuttle_function_with_params(self):
        def bar(bar):
            return 'This is new {}'.format(bar)

        @dandelyon.alias(ff=bar)
        def foo(bar):
            return 'This is old {}'.format(bar)

        res = foo('function')

        assert res == 'This is new function'

    def test_shuttle_function_with_extra_params(self):
        def bar(bar, baz):
            return 'This is new {} {}'.format(bar, baz)

        @dandelyon.alias(ff=bar)
        def foo(bar):
            return 'This is old {}'.format(bar)

        res = foo('function', 'junction')

        assert res == 'This is new function junction'


class TestTimeBombDeprecation(unittest.TestCase):
    def test_time_bomb_returns_new_function(self):
        def bar(bar, baz):
            return 'This is new {} {}'.format(bar, baz)

        @dandelyon.countdown(expires=datetime.now(), message='Unique String', ff=bar)
        def foo(bar):
            return 'This is old {}'.format(bar)

        res = foo('function', 'junction')

        assert res == 'This is new function junction'

    def test_time_bomb_returns_original_function(self):
        expiry_date = datetime.now() + timedelta(days=1)

        def bar(bar, baz):
            return 'This is new {} {}'.format(bar, baz)

        @dandelyon.countdown(expires=expiry_date, message='Unique String', ff=bar)
        def foo(bar, *args, **kwargs):
            return 'This is old {}'.format(bar)

        res = foo('function', 'junction')

        assert res == 'This is old function'
