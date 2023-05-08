import time
import board
from adafruit_motor import stepper, motor
from adafruit_motorkit import MotorKit

# 创建MotorKit对象
kit = MotorKit(i2c=board.I2C())

# 设置步进电机速度（RPM）
rpm = 5

while True:
    # 驱动DC电机
    kit.motor4.throttle = 0.5  # 设置直流电机速度（-1.0至1.0）

    # 驱动步进电机
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)

    # 等待时间，可根据需要调整
    time.sleep(60 / (200 * rpm))  # 200是步进电机的步数