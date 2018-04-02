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
        def bar(bam):
            return 'This is new {}'.format(bam)

        @dandelyon.alias(ff=bar)
        def foo(bam):
            return 'This is old {}'.format(bam)

        res = foo('function')

        assert res == 'This is new function'

    def test_shuttle_function_with_extra_params(self):
        def bar(bam, baz):
            return 'This is new {} {}'.format(bam, baz)

        @dandelyon.alias(ff=bar)
        def foo(bam):
            return 'This is old {}'.format(bam)

        res = foo('function', 'junction')

        assert res == 'This is new function junction'


class TestCountdownDeprecation(unittest.TestCase):
    def test_countdown_returns_new_function(self):
        def bar(bam, baz):
            return 'This is new {} {}'.format(bam, baz)

        @dandelyon.countdown(expires=datetime.now(),
                             message='Unique String',
                             ff=bar)
        def foo(bam):
            return 'This is old {}'.format(bam)

        res = foo('function', 'junction')

        assert res == 'This is new function junction'

    def test_countdown_does_not_warn_twice(self):
        expiry_date = datetime.now() + timedelta(days=1)

        def bar(bam, baz):
            return 'This is new {} {}'.format(bam, baz)

        @dandelyon.countdown(expires=expiry_date,
                             message='Test Deprecation',
                             ff=bar)
        def foo(bam, *args, **kwargs):
            return 'This is old {}'.format(bam)

        with warnings.catch_warnings(record=True) as w:
            res = foo('function', 'junction')
            res2 = foo('function', 'junction')

        assert "is a deprecated function and it " \
               "will be removed by" in str(w[-1].message)

        assert (res and res2) == 'This is old function'

        assert len(w) == 1






