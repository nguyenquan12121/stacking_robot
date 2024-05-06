#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>
#include <stdbool.h>

#define DC_Motor_1 1
#define DC_Motor_2 2
#define DC_Motor_3 3
#define DC_Motor_4 4

//#define DIR_LATCH 0
//#define DIR_CLK 1
//#define DIR_SER 2

#define PIN 3
#define DIRECTION 4
#define IS_RUNNING 5
#define RUNNING_DIRECTION 6
#define PWM 7
#define PWM_FREQUENCY 8
#define PWM_DUTY_CYCLE 9

#define clockwise 0
#define counterclockwise 1
#define stop 2


int DIR_LATCH = 0;
int DIR_CLK = 0;
int DIR_SER = 0;


int MOTORS[5][10] = {
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 4, 8, 4 | 8, 0, 0, 0, 0, 0, 100},
    {0, 2, 16, 2 | 16, 0, 0, 0, 0, 0, 100},
    {0, 32, 128, 32 | 128, 0, 0, 0, 0, 0, 100},
    {0, 1, 64, 1 | 64, 0, 0, 0, 0, 0, 100}
};


void shiftWrite(int value) {
    digitalWrite(DIR_LATCH, LOW);
    for (int i = 0; i < 8; i++) {
        int temp = value & 0x80;
        digitalWrite(DIR_CLK, LOW);
        if (temp == 0x80) {
            digitalWrite(DIR_SER, HIGH);
        } else {
            digitalWrite(DIR_SER, LOW);
        }
        digitalWrite(DIR_CLK, HIGH);
        value <<= 0x01;
    }
    digitalWrite(DIR_LATCH, HIGH);
}

void set74HC595Pins(int dir_latch, int dir_clk, int dir_ser) {
    DIR_LATCH = dir_latch;
    DIR_CLK = dir_clk;
    DIR_SER = dir_ser;
    pinMode(dir_latch, OUTPUT);
    pinMode(dir_clk, OUTPUT);
    pinMode(dir_ser, OUTPUT);
}

void setL293DPins(int PWM0A, int PWM0B, int PWM2A, int PWM2B) {
    MOTORS[1][PIN] = PWM0B;
    MOTORS[2][PIN] = PWM0A;
    MOTORS[3][PIN] = PWM2A;
    MOTORS[4][PIN] = PWM2B;       
    pinMode(PWM0A, OUTPUT);
    pinMode(PWM0B, OUTPUT);
    pinMode(PWM2A, OUTPUT);
    pinMode(PWM2B, OUTPUT);
}

void runDCMotor(int dcMotor, int direction, int speed) {
    int allMotorsDirection = MOTORS[dcMotor][direction + 1];
    for (int i = 1; i <= 4; i++) {
        if (i == dcMotor) {
            continue;
        }
        if (MOTORS[i][RUNNING_DIRECTION] != 0) {
            allMotorsDirection += MOTORS[i][RUNNING_DIRECTION];
        }
    }
    shiftWrite(allMotorsDirection);
    if (speed == 0) {
        digitalWrite(MOTORS[dcMotor][PIN], HIGH);
    } else if (speed >= 0 && speed <= 100) {
        MOTORS[dcMotor][PWM] = softPwmCreate(MOTORS[dcMotor][PIN], 0 , speed);
        softPwmWrite(MOTORS[dcMotor][PIN], speed);
    } else {
        printf("WARNING: Speed argument must be in range 0-100! But %d given. Keeping previous setting (%d).\n", speed, MOTORS[dcMotor][PWM_DUTY_CYCLE]);
    }

    MOTORS[dcMotor][IS_RUNNING] = 1;
    MOTORS[dcMotor][RUNNING_DIRECTION] = MOTORS[dcMotor][direction + 1];
}


void stopDCMotor(int dcMotor) {
    int allMotorsDirection = MOTORS[dcMotor][stop + 1];
    for (int i = 1; i <= 4; i++) {
        if (i == dcMotor) {
            continue;
        }
        if (MOTORS[i][RUNNING_DIRECTION] != 0) {
            allMotorsDirection += MOTORS[i][RUNNING_DIRECTION];
        }
    }
    shiftWrite(allMotorsDirection);

    if (MOTORS[dcMotor][PWM] == 0) {
        digitalWrite(MOTORS[dcMotor][PIN], LOW);
    } else {
        softPwmStop(MOTORS[dcMotor][PIN]);
        MOTORS[dcMotor][PWM] = 0;
    }

    MOTORS[dcMotor][IS_RUNNING] = 0;
    MOTORS[dcMotor][RUNNING_DIRECTION] = 0;
}



int main() {
    wiringPiSetupGpio();

    set74HC595Pins(21, 20, 16);
    setL293DPins(5, 6, 13, 19);
    printf("RUNNING MOTOR 1 CLOCKWISE \n");
    runDCMotor(DC_Motor_1, clockwise, 50);
    runDCMotor(DC_Motor_2, clockwise, 50);
    runDCMotor(DC_Motor_3, clockwise, 50);
    runDCMotor(DC_Motor_4, clockwise, 50);
    delay(2000);

    stopDCMotor(DC_Motor_1);
    stopDCMotor(DC_Motor_2);
    stopDCMotor(DC_Motor_3);
    stopDCMotor(DC_Motor_4);
    printf("STOPPING MOTORS\n");
    delay(2000);

    printf("RUNNING MOTOR 1 COUNTER-CLOCKWISE \n");
    runDCMotor(DC_Motor_1, counterclockwise, 50);
    runDCMotor(DC_Motor_2, counterclockwise, 50);
    runDCMotor(DC_Motor_3, counterclockwise, 50);
    runDCMotor(DC_Motor_4, counterclockwise, 50);

    delay(2000);
    printf("STOPPING MOTORS\n");

    stopDCMotor(DC_Motor_1);
    stopDCMotor(DC_Motor_2);
    stopDCMotor(DC_Motor_3);
    stopDCMotor(DC_Motor_4);

    delay(2000);
    return 0;
}

