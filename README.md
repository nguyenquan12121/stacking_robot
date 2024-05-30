# CBL36

## Running the motors
Plug the arduino into the raspberry pi
String format for running the motor is as follows
```
Motor number (1 to 4)-Speed (0 to 255)-Duration(<9999 >1000)-Direction(1 forward 2 backward 1 or 2) 
```
## Running the tests

Ensure that `pytest` is installed

Simply run in the root directory to run the tests
```
pytest
```

To see the test coverage for `classes`, run:
```
pytest --cov=classes
```