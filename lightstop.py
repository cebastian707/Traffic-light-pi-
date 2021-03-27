#PROGRAM DONE BY CEBASTIAN SANTIAGO
#simple traffic light sequence with a buzzer when the night turns red  using the raspberry pi Gpio pins 
from time import sleep
from gpiozero import Button ,TrafficLights,Buzzer

buzzer = Buzzer(15)
lights = TrafficLights(25,8,7)

button = Button(21)

while True:
        button.wait_for_press()
        lights.green.on()
        sleep(5)
        lights.green.off()
        lights.amber.on()
        sleep(5)
        lights.amber.off()
        lights.red.on()
        buzzer.on()
        sleep(5)
        lights.red.off()
        buzzer.off()
