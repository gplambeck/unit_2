from microbit import *

# Experiment 0
# display.scroll("Hello World")


# SparkFun Electronics
# Experiment 0.1
# Display an image

# while True:
#     display.show(Image.PACMAN)


# SparkFun Electronics
# Experiment 0.2
# Display a custom image

# while True:
#     star = Image("00900:99599:05950:09590:90009")
#     display.show(star)


# SparkFun Electronics
# Experiment 1.0
# Blinking an LED

# while True:
#     pin0.write_digital(1)
#     sleep(1000)
#     pin0.write_digital(0)
#     sleep(1000)


# SparkFun Electronics
# Experiment 2.0
# Reading a Potentiometer

# while True:
#     potVal = pin2.read_analog()
#     pin0.write_analog(potVal)
#     sleep(25)


# SparkFun Electronics
# Experiment 3.0
# Reading a Photoresistor

# calibrationVal = pin0.read_analog()
# sleep(1000)

# while True:
#     lightVal = pin0.read_analog()
#     if lightVal < calibrationVal-50:
#         pin16.write_digital(1)
#     else:
#         pin16.write_digital(0)


# SparkFun Electronics
# Experiment 4.0
# Driving an RGB LED

# from random import randint

# redVal = randint(0, 255)
# greenVal = 0
# blueVal = 0

# while True:
#     if button_a.is_pressed():
#         redVal = 0
#         blueVal = 0
#         greenVal = randint(0, 255)
#         pin0.write_analog(redVal)
#         pin1.write_analog(greenVal)
#         pin2.write_analog(blueVal)
#     elif button_b.is_pressed():
#         redVal = 0
#         blueVal = randint(0, 255)
#         greenVal = 0
#         pin0.write_analog(redVal)
#         pin1.write_analog(greenVal)
#         pin2.write_analog(blueVal)
#     else:
#         pin0.write_analog(redVal)
#         pin1.write_analog(greenVal)
#         pin2.write_analog(blueVal)


# SparkFun Electronics
# Experiment 5.0
# Reading an SPDT Switch

# while True:
#     if pin0.read_digital():
#         pin15.write_digital(1)
#         sleep(1000)
#         pin15.write_digital(0)
#         sleep(1000)
#     else:
#         pin16.write_digital(1)
#         sleep(500)
#         pin16.write_digital(0)
#         sleep(500)


# SparkFun Electronics
# Experiment 6.0
# Reading a button press

# led_pins = [pin0, pin1, pin2]
# led_states = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
# led_states_iter = iter(led_states)
# RED = 0
# GREEN = 1
# BLUE = 2

# while True:
#     while pin16.read_digital() == 0:
#         pass
#     while pin16.read_digital() == 1:
#         pass
#     try:
#         led_state = next(led_states_iter)
#     except:
#         led_states_iter = iter(led_states)

#     pin0.write_analog(led_state[RED])
#     pin1.write_analog(led_state[GREEN])
#     pin2.write_analog(led_state[BLUE])


# SparkFun Electronics
# Experiment 7.0
# Reading a Temp Sensor

# while True:
#     rawTemp = pin2.read_analog()
#     degC = (((rawTemp*3.3)/(1023))-0.5)*100
#     display.show(str(degC))
#     sleep(1000)


# SparkFun Electronics
# Experiment 8.0
# Using a servo motor

# class Servo:
#     def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
#         self.min_us = min_us
#         self.max_us = max_us
#         self.us = 0
#         self.freq = freq
#         self.angle = angle
#         self.analog_period = 0
#         self.pin = pin
#         analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
#         self.pin.set_analog_period(analog_period)

#     def write_us(self, us):
#         us = min(self.max_us, max(self.min_us, us))
#         duty = round(us * 1024 * self.freq // 1000000)
#         self.pin.write_analog(duty)
#         sleep(100)
#         self.pin.write_digital(0)  # turn the pin off

#     def write_angle(self, degrees=None):
#         if degrees is None:
#             degrees = math.degrees(radians)
#         degrees = degrees % 360
#         total_range = self.max_us - self.min_us
#         us = self.min_us + total_range * degrees // self.angle
#         self.write_us(us)


# Servo(pin0).write_angle(0)
# while True:
#     if button_a.is_pressed():
#         for angle in range(0, 90, 5):
#             Servo(pin0).write_angle(angle)
#             sleep(200)
#     if button_b.is_pressed():
#         Servo(pin0).write_angle(0)
#         sleep(1000)
#         Servo(pin0).write_angle(90)
#         sleep(1000)
#         Servo(pin0).write_angle(0)
#         sleep(1000)
#     else:
#         Servo(pin0).write_angle(180)


# SparkFun Electronics
# Experiment 9.0
# Using a buzzer

# import music

# while True:
#     if pin15.read_digital() == 1:
#         music.play("C4:8")
#     elif pin16.read_digital() == 1:
#         music.play("D1:8")
#     else:
#         pass


# SparkFun Electronics
# Experiment 10
# Using the Accelerometer

# class Servo:
#     def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
#         self.min_us = min_us
#         self.max_us = max_us
#         self.us = 0
#         self.freq = freq
#         self.angle = angle
#         self.analog_period = 0
#         self.pin = pin
#         analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
#         self.pin.set_analog_period(analog_period)

#     def write_us(self, us):
#         us = min(self.max_us, max(self.min_us, us))
#         duty = round(us * 1024 * self.freq // 1000000)
#         self.pin.write_analog(duty)
#         sleep(100)
#         self.pin.write_digital(0)  # turn the pin off

#     def write_angle(self, degrees=None):
#         if degrees is None:
#             degrees = math.degrees(radians)
#         degrees = degrees % 360
#         total_range = self.max_us - self.min_us
#         us = self.min_us + total_range * degrees // self.angle
#         self.write_us(us)


# Servo(pin0).write_angle(0)
# while True:
#     num = accelerometer.get_x()
#     Servo(pin0).write_angle(num * 180 / 2048 + 90)


# SparkFun Electronics
# Experiment 11
# Using the Compass (Magnetometer)

# compass.calibrate()
# while True:
#     bearing = compass.heading()
#     sleep(10)

#     #bearing is the degrees
#     if ( bearing > 10 and bearing < 180 ):
#         pin0.write_digital(0)
#         pin16.write_digital(1)
#     #bearing is the degrees
#     elif ( bearing > 180 and bearing < 350 ):
#         pin0.write_digital(1)
#         pin16.write_digital(0)
#     #bearing is the degrees
#     else:
#         pin0.write_digital(1)
#         pin16.write_digital(1)
