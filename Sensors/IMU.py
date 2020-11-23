# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time
import board
import busio
import adafruit_lsm9ds1

class IMU:
     # init method or constructor    
    def __init__(self):   
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

    # returns a touple of values x acceleration, y acceleration, z acceleration. 
    # values are in (m/s^2)
    def getAccel(self): 
        accel_x, accel_y, accel_z = self.sensor.acceleration
        return (accel_x, accel_y, accel_z)

    # returns a touple of values x magnetometer, y magnetometer, z magnetometer
    # values are in gauss
    def getMag(self):    
        mag_x, mag_y, mag_z = self.sensor.magnetic
        return (mag_x, mag_y, mag_z)


    # returns a touple of values x gyro, y gyro, z gyro. 
    # values are in (degrees/sec)
    def getGyro(self):
        gyro_x, gyro_y, gyro_z = self.sensor.gyro
        return (gyro_x, gyro_y, gyro_z)

    # returns the temperature reading
    # values are in C
    def getTemp(self):
        temp = self.sensor.temperature
        return temp


# saving this as formatting might be useful in gui

    # # Print values.
    # print(
    #     "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
    #         accel_x, accel_y, accel_z
    #     )
    # )
    # print(
    #     "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag_x, mag_y, mag_z)
    # )
    # print(
    #     "Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
    #         gyro_x, gyro_y, gyro_z
    #     )
    # )
    # print("Temperature: {0:0.3f}C".format(temp))