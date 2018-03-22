<a href="https://codeclimate.com/github/andrewgy8/dandelyon/maintainability"><img src="https://api.codeclimate.com/v1/badges/a86ab4d6ac65f57d09a7/maintainability" /></a>
[![CircleCI](https://circleci.com/gh/andrewgy8/dandelyon.svg?style=svg)](https://circleci.com/gh/andrewgy8/dandelyon)

# Dandelyon

Things are born. As time passes, things get old.  And eventually, everything will eventually come to an end.  

This is no different with code.

We believe deprecation should be easy, efficient and predictable.  

## Getting Started

Install with 

`pip install dandelyon`


**A simple deprecation warning** 

```
from dandelyon import dandelyon

@dandelyon.blow(message='This is an old function.')
def foo():
    print('Im old')
   
# Warning: This is an old function
    
```

***A shuttle from one function to another**

```
def bar():
    return 'This is new'

@dandelyon.shuttle(ff=bar)
def foo():
    return 'This is old'

res = foo()

print(res) # 'This is new'  
```

**Or add new parameters...**

```
def bar(bar, baz):
    return 'This is a new {} {}'.format(bar, baz)

@dandelyon.shuttle(ff=bar)
def foo():
    return 'This is old'

res = foo('function', 'junction')

print(res) # 'This is a new function junction'  
```

**Add a time-bomb to your function and shuttle**
```
expiry_date = datetime.datetime(2200, 1, 1)

def bar(bar, baz):
    return 'This is new a {} {}'.format(bar, baz)

@dandelyon.spring(expires=expiry_date, message='Unique String', ff=bar)
def foo(bar, *args, **kwargs):
    return 'This is old {}'.format(bar)

res = foo('function', 'junction')

# Before year 2200
print(res)  # This is an old function

# Later in time... 
print(res) # This is a new function junction

```

## Running the tests

`python setup.py test`

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Andrew Graham-Yooll**

See also the list of [contributors](https://github.com/andrewgy8/dandelyon/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Add your name here!