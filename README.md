<a href="https://codeclimate.com/github/andrewgy8/deprecator/maintainability"><img src="https://api.codeclimate.com/v1/badges/58843681d3cc1cf5e58c/maintainability" /></a>
<a href="https://codeclimate.com/github/andrewgy8/deprecator/test_coverage"><img src="https://api.codeclimate.com/v1/badges/58843681d3cc1cf5e58c/test_coverage" /></a>

# Deprecator

Deprecating shouldn't have to be difficult. And indeed should be part of a software's normal lifecycle.  

## Getting Started

#### TBA
Install with 

`pip install deprecator`

```
from deprecator import deprecator

@deprecator.warn(message='This is an old function.')
def foo():
    print('Im old')
    return 
    
```

## Running the tests

`python setup.py test`

## Deployment

Add additional notes about how to deploy this on a live system

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Andrew Graham-Yooll**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Add your name here!