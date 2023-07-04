# ATM-controller

## Overview

This project is an ATM Controller that handles the logic of Receiving a Card Number, Checking if the PIN code is correct, allow the user of the ATM to Select an account and check the balance of said account and withdraw/depost funds, while validating the data at every step, and not showing sensetive information. The project only contains the ATM Controller logic and no integrations to hardware or APIs.

## Installation

1.  Clone the repository to your local machine using the following command:

        `git clone https://github.com/FRNBDN/ATM-controller.git`

2.  Navigate to the project directory:

        `cd ATM-controller`

3.  Create a virtual environment (optional but recommended) to isolate the project dependencies:

        `python -m venv venv`

4.  Activate the virtual environment:

    - For Windows

            `venv\Scripts\activate`

    - For Linux/macOS:

             `source venv/bin/activate`

5.  Run the tests to ensure everything is set up correctly:

        `python -m unittest test`

### Requirements

- Python 3.11.1

## Usage Example

The project is built with API and Hardware and integration in mind, utilising functions for the mock api calls to help make integration with real world hardware and APIs as easy as possible. The app is also made with the intention of allowing for a UI being developed for it.

## Runing the program

    `python run.py`

To run the ATM controller program, you can execute the `run.py` file. Please note that the user inputs in the code are currently hardcoded for demonstration purposes and should be replaced with appropriate user input from a UI integration in a production environment.

## Testing

### Testing Framework

- Unittest

Unittest was chosen due to the familiarity I have with the APITestCase from my DRF Projects, making it easy to use and the familaiarity between the APITestCase and Unittest, would also make it easier to write and organize tests effectively with future API implemenations. It is also a Built-in module and popular, so other developers using the code will be familiar with the syntax and conventions.

### How to run tests

`python -m unittest test`

### Creating additional tests

#### Unittests

- Follow the format of the test.py file

#### Testing run.py

If you wish to test the project further, the user inputs have been marked with "# User Input" comments in the run.py file.

![UserInputComment](/images/userinput.png)

The Card Number used is marked with a "# Mock Card Input" comment.

![MockCardComment](/images/mockcard.png)
