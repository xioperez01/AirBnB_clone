[![GitHub issues](https://img.shields.io/github/issues/xioperez01/AirBnB_clone?style=plastic)](https://github.com/xioperez01/AirBnB_clone/issues)
[![GitHub forks](https://img.shields.io/github/forks/xioperez01/AirBnB_clone?color=orange&style=plastic)](https://github.com/xioperez01/AirBnB_clone/network)
[![GitHub stars](https://img.shields.io/github/stars/xioperez01/AirBnB_clone?color=violet&style=plastic)](https://github.com/xioperez01/AirBnB_clone/stargazers)
[![Twitter](https://img.shields.io/twitter/url?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fxioperez01%2FAirBnB_clone)
# AirBnB_clone #
**A command interpreter to manage your AirBnB objects.**

This **AirBnB** clone consists of creating a shell to manage AirBnB objects.
As a command interpreter take the Shell example, but limited to a specific case. In this case, you want to be able to manage the project objects:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
## How to install it? :question: :question: ##
To have this repository and its content, you must execute the following on your terminal:
~~~
$ git clone https://github.com/xioperez01/AirBnB_clone.git
$cd AirBnB_Clone
~~~
## How to use it? :question: :question: ##
You can use it in interactive mode:
~~~
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
~~~
Or you can use it in non-interactive mode:
~~~
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
~~~
## Environment ##
* Languages: Python3.4.3
* OS: Ubuntu 14.04 LTS
* Compiler: python3
* PEP 8 - [Style](https://www.python.org/dev/peps/pep-0008/) // [Docstring](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
## Autors :ribbon: ##
 Angie Pérez [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/30px-Twitter_Bird.svg.png)](https://twitter.com/xiommyperez)


