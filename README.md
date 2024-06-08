# CBL36

## Setup on raspberry pi:
- Clone the repository
- Run main.py
- Enter the pi's local ipadress and hit enter
- Enter the pi's portnumber

## Setup on the laptop/client
- Clone the repository
- Run main.py in the client folder

If you want you can also run the virtual twin which recives data from the pi.
To do this download the builded application from the repository: 
```
https://github.com/CodingDiederik/Simulation-cbl/releases
```
Extract all the contents and run the CBL Embedded systems exe file.

## Running the motors
Plug the arduino into the raspberry pi
String format for running the motor is as follows
```
Motor number (1 to 4)-Speed (0 to 255)-Duration(<9999 >1000)-Direction(1 forward 2 backward 1 or 2) 
```
## Running the tests

Ensure that `pytest` and `pytest-cov` is installed

Simply execute this command in the root directory to run the tests
```
pytest
```

To see the test coverage for the entire project, run this command in the root dir:
```
pytest --cov=.
```
