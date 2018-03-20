<a href="https://codeclimate.com/github/andrewgy8/deprecator/maintainability"><img src="https://api.codeclimate.com/v1/badges/58843681d3cc1cf5e58c/maintainability" /></a>
[![CircleCI](https://circleci.com/gh/andrewgy8/deprecator.svg?style=svg)](https://circleci.com/gh/andrewgy8/deprecator)

# Dandelion

Deprecating shouldn't have to be difficult. And indeed should be part of a software's normal lifecycle.  

## Getting Started

#### TBA
Install with 

`pip install dandelion`


**A simple deprecation warning** 

```
from dandelion import dandelion

@dandelion.blow(message='This is an old function.')
def foo():
    print('Im old')
   
# Warning: This is an old function
    
```

***A shuttle from one function to another**

```
def bar():
    return 'This is new'

@dandelion.shuttle(ff=bar)
def foo():
    return 'This is old'

res = foo()

print(res) # 'This is new'  
```

**Or add new parameters...**

```
def bar(bar, baz):
    return 'This is a new {} {}'.format(bar, baz)

@dandelion.shuttle(ff=bar)
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

@deprecator.spring(expires=expiry_date, message='Unique String', ff=bar)
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

## Deployment

Add additional notes about how to deploy this on a live system

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Andrew Graham-Yooll**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Add your name here!