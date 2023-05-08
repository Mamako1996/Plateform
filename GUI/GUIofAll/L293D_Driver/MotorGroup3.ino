#include <AFMotor.h> 

AF_DCMotor motor1(1);               // create motor #1, 64KHz pwm - linked to the M3 port on L293D driver
AF_DCMotor motor2(2);               // create motor #2, 64KHz pwm - linked to the M4 port on L293D driver
AF_DCMotor motor3(3);               // create motor #3, 64KHz pwm - linked to the M3 port on L293D driver
AF_DCMotor motor4(4);               // create motor #4, 64KHz pwm - linked to the M4 port on L293D driver

  int delayTime = ;

  int rpm1 = ;                     // set a initial rotational speed 300rpm ~ 800rpm (recommended)
  int rpm2 = ;                     // set a initial rotational speed 300rpm ~ 800rpm (recommended)
  int rpm3 = ;                     // set a initial rotational speed 300rpm ~ 800rpm (recommended)
  int rpm4 = ;                     // set a initial rotational speed 300rpm ~ 800rpm (recommended)

  int maxSpeed = 4500;              // input motor max speed

  int spd1 = rpm1 / (maxSpeed/255); // linear equation [y = x / (maxSpeed/255)]
                                    // x is the actual rotational speed rmp; 
                                    // y is The number represented in the development board
                                    // 255 represents the max speed for setSpeed() method in AFMotor(range: 0~255)
                                    // 0 means stop
  int spd2 = rpm2 / (maxSpeed/255);
  int spd3 = rpm3 / (maxSpeed/255);
  int spd4 = rpm4 / (maxSpeed/255);

void setup() {
  Serial.begin(9600);               // set up Serial library at 9600 bps
}

void loop() {
  motor1.setSpeed(spd1);             // Motor 3 set the speed spd which is relative to actual rotational speed
  motor1.run(FORWARD);              // Motor 3 turn it on going forward (Clockwise)

  motor2.setSpeed(spd2);                // Motor 4 set the speed spd which is relative to actual rotational speed
  motor2.run(FORWARD);              // Motor 4turn it on going forward (Clockwise)

  motor3.setSpeed(spd3);             // Motor 3 set the speed spd which is relative to actual rotational speed
  motor3.run(FORWARD);              // Motor 3 turn it on going forward (Clockwise)

  motor4.setSpeed(spd4);                // Motor 4 set the speed spd which is relative to actual rotational speed
  motor4.run(FORWARD);              // Motor 4turn it on going forward (Clockwise)

  delay(delayTime);                      // Both motor 3 and motor 4 use 5 second complete the rotation process
  exit(0);
}
