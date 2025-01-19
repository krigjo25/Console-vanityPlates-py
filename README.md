# VanityPlates
An application to ensure custom plates meets
the requirement by CS50 Motor Vehicles, CS50MV

The application was implemented as a CS50P assignment.<br>
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/Console-Vanityplates-py.git

# Using git bash
git clone https://github.com/krigjo25/Console-Vanityplates-py.git

# Using Github Cli
gh repo clone Console-Vanityplates-py
```

2. Navigate to the project directory
```sh
cd Console-Vanityplates-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```

4. Run the file
```sh
python app.py
```

##  Usage

```sh
Usage : type in the terminal python app.py.
python app.py
```

## Example
```sh
python app.py

Plate:  <A>
expected output: "Invalid"

Plate:  <CS50>
expected output: "Valid"
```

Replace `<A>` with the desired Plate, 
replace `<CS50>` with the desired Plate.

##  Testing framework / Datasets
Pytest was used as a testing framework during this project
```sh
pytest -s test_app.py      #   Testing the application with Inputs
pytest -k test_app.py      #   Testing the application without inputs
pytest --html=index.html   #   Testing the application, retrieve a html file
```
The data sets which is used to test the application is at located in the [test folder](test_app.y)

## LICENCE
The application is under [The Unlicensed](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25