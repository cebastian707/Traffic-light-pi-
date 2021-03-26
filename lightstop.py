#PROGRAM DONE BY CEBASTIAN SANTIAGO
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
        sleep(5)
        lights.red.off()