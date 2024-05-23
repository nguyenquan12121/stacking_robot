from enum import Enum

class MachineState(Enum):
    WAITING_LUGGAGE = 1
    CONVEYOR_BELT_MOVING = 2
    CONVEYOR_BELT_DROP = 3
    ELAVATOR_TO_BOTTOM = 4
    ELAVATOR_TO_TOP = 5
    PUSHER_PUSH = 6
    PUSHER_BACK = 7
    ERROR = 8