Tigran Modulation
=================

## How to set up a virtual environemnt
1. Ensure you have installed venv via pip
  - Ensure that you are at the root directory of this project
  - `pip3 install venv`
2. Create the venv
  - `python3 -m venv venv`
3. Start using the virtual environment
  - On macOS
    - `source venv/bin/activate`

## How to manage the packages
### Install the required packages for this project

```sh
pip3 install -r requirements.txt
```

### Update the package list
(You should be doing this from within the virtual environment)

```sh
pip3 freeze > requirements.txt
```

## How to run
### The application
First ensure you have installed all the packages

```sh
python3 main.py
```

### The tests
First ensure you have installed all the packages

```sh
python3 main.py
```