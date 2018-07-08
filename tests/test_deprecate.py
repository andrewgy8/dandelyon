import unittest
import warnings
from datetime import datetime, timedelta

from dandelyon import deprecators


class TestDeprecateWarning(unittest.TestCase):

    def test_throws_warning(self):
        with warnings.catch_warnings(record=True) as w:
            @deprecators.warn(message='This will deprecate.')
            def foo():
                return ''
            foo()
            assert "deprecate" in str(w[-1].message)


class TestShuttleFunction(unittest.TestCase):

    def test_shuttle_function_without_params(self):
        def bar():
            return 'This is new'

        @deprecators.alias(ff=bar)
        def foo():
            return 'This is old'

        res = foo()

        assert res == 'This is new'

    def test_shuttle_function_with_params(self):
        def bar(bam):
            return 'This is new {}'.format(bam)

        @deprecators.alias(ff=bar)
        def foo(bam):
            return 'This is old {}'.format(bam)

        res = foo('function')

        assert res == 'This is new function'

    def test_shuttle_function_with_extra_params(self):
        def bar(bam, baz):
            return 'This is new {} {}'.format(bam, baz)

        @deprecators.alias(ff=bar)
        def foo(bam):
            return 'This is old {}'.format(bam)

        res = foo('function', 'junction')

        assert res == 'This is new function junction'


class TestCountdownDeprecation(unittest.TestCase):
    def test_countdown_returns_new_function(self):
        def bar(bam, baz):
            return 'This is new {} {}'.format(bam, baz)

        @deprecators.countdown(expires=datetime.now(),
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

        @deprecators.countdown(expires=expiry_date,
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


class TestPythonVersionWarning(unittest.TestCase):
    def test_returns_warning_when_python_version_is_being_deprecated(self):
        @deprecators.version(py_version='3.5')
        def foo():
            return 'This is old'

        with warnings.catch_warnings(record=True) as w:
            res = foo()

        assert "foo is a deprecated function" in str(w[-1].message)
        assert res == 'This is old'

    def test_returns_no_warning_when_python_version_is_ok(self):
        @deprecators.version(py_version='3.9')
        def foo():
            return 'This is old'

        with warnings.catch_warnings(record=True) as w:
            res = foo()

        assert w == []
        assert res == 'This is old'
