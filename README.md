# __AirBnB_clone__

The *AirBnB_clone* project involvels creating a web application that simulates the popular AirBnB service. This project serves to deploy on a server a simple copy of the AirBnB website.

## Table of Contents

- [Background context](#background-context)
- [Files](#files)
- [Task Description](Task-description)
- [How to Use](#how-to-use)
- [Contribution Guidelines](#contribution-guidelines)
- [Licence](#licence)

## Background context

The AirBnB clone would be composed of four parts, the command interpreter, database or file storage engine, a website and API. The commandline interpreter provides a console that enables storage and manipulation of data. The console will enable a user to create objects, retrieve objects from a file or database, peform operations on the objects, update object attributes and destroy objects.
The web static layer involves using HTML/CSS to create a web front-end that interacts with the user along with templates for each object created.
The MySQL layer involves replacing the file storage engine with database storage and enables mapping of models to a table in database using an O.R.M.
The Web framework involves deployment of HTML with fabric. It involves making the static HTML file dynamic using objects stored in the file or database.
The RESTful API layer exposes the objects stored via a JSON web interface for manipulation
The Web dynamic involves using JQuery to load objects from the client side using RESTfu API[^1].

## Files

The `models` directory contains classes used for the project.
The `tests` directory contains all unit tests.
`console.py` file is the commandline interpreter entry point
The `models/base_model.py` file is the base class for all models with common attributes such as `id`, `created_at`, `updated_at` and methods including `save()` and `to_json()`.
The `models/engine` directory contains all storage classes such as `file_storage.py`

## Task Description

## How to Use
Each task file is implemented on a separate python file.
Use the console as follows:
1. Using the shell in interactive mode:
```sh
$ ./console.py
```
2. The shell usage ein non-interactive mode :
```sh
$ echo [*command*] | ./console.py
```
- Example 1(interactive):

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
- Example 2(non-interactive):

```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Contribution Guidelines
This project is a collaborative assignment and open for external contributions. It is for educational purposes only, and all work should be completed by the group individuals as part of the project requirements.
## Licence
This project is for educational purposes and does not require a specific license. It is intended for use as part of an assignment and learning activity and is not open for external distribution or contributions.

[//]: #
	[^1]: article
