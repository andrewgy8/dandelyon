# Dandelyon :blossom:

<a href="https://codeclimate.com/github/andrewgy8/dandelyon/maintainability"><img src="https://api.codeclimate.com/v1/badges/a86ab4d6ac65f57d09a7/maintainability" /></a>
[![CircleCI](https://circleci.com/gh/andrewgy8/dandelyon.svg?style=svg)](https://circleci.com/gh/andrewgy8/dandelyon)
[![GitHub release](https://img.shields.io/github/release/andrewgy8/dandelyon.svg)](https://github.com/andrewgy8/dandelyon/releases)

Eventually, everything will come to an end.  

There is no difference with code.

Deprecation should be easy, efficient and predictable.  

With the the help of a few decorator functions, you can communicate to your users any changes occurring in upcoming releases.

## Getting Started

Install with 

`pip install dandelyon`


**A simple deprecation warning** 

```
from dandelyon import deprecators

@deprecators.warn(message='Please consider using bar()')
def foo():
    return 'Fire!'
   
res = foo()
print(res) 
# 'Fire'
-----
# In your logs
# "Warning: Foo is a deprecated function. Please consider using bar()"  
    
```

**A shuttle from one function to another**

```
def bar():
    return 'This is new'

@deprecators.shuttle(ff=bar)
def foo():
    return 'This is old'

res = foo()

print(res) 
# 'This is new'  
```

**Or add new parameters...**

```
def bar(bar, baz):
    return 'This is a new {} {}'.format(bar, baz)

@deprecators.alias(ff=bar)
def foo():
    return 'This is old'

res = foo('function', 'junction')

print(res)  
# 'This is a new function junction'  
```

**Add a date where the function will deprecate and forward to another function**
```
expiry_date = datetime.datetime(2200, 1, 1)

def bar(bar, baz):
    return 'This is new a {} {}'.format(bar, baz)

@deprecators.countdown(expires=expiry_date, 
                  message='Please consider using bar().', 
                  ff=bar)
def foo(bar, *args, **kwargs):
    return 'This is an old {}'.format(bar)

res = foo('function', 'junction')

# Before year 2200
print(res)  
# 'This is an old function'
-----
# In your logs:
# Warning: "foo() is a deprecated function and it will be removed by 1-1-2200. Please consider using bar()."

# Later in time... 
print(res) 
# This is a new function junction

```

## Dependencies

**None**

## Running the tests

`python setup.py test`

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Add your name here!