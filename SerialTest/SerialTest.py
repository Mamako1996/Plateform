import serial

serialPort1 = "COM6"  # port 1
serialPort2 = "COM7"  # port 2
serialPort3 = "COM8"  # port 3

baudRate = 9600  # Baud rate
ser1 = serial.Serial(serialPort1, baudRate, timeout=1)
ser2 = serial.Serial(serialPort2, baudRate, timeout=1)
ser3 = serial.Serial(serialPort3, baudRate, timeout=1)
print("Parameter Settings: Serial port =%s, baud rate =%d" % (serialPort1, baudRate))

stop = b"0"  # Convert 0 to ASCII code for easy sending
run = b"1"  # in a similar way
while 1:
    c = input('Please enter instruction:')
    c = ord(c)  # Convert c to UTF-8 standard numbers
    if c == 48:
        ser1.write(stop)
        ser2.write(stop)
        ser3.write(stop)
    if c == 49:
        ser1.write(run)
        ser2.write(run)
        ser3.write(run)
