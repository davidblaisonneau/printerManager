#!/usr/bin/python3
# -*-coding:utf8 -*

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Relay:
    """Definition of a relay:
    - name
    - GPIO pin"""
    GPIO.setmode(GPIO.BCM)
    
    def __init__(self, pin, name=""):
        """Set the relay"""
        self.name = name
        self.pin = pin
        
    def _get_state_(self):
        """Get the GPIO state"""
        GPIO.setup(self.pin, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
        return not GPIO.input(self.pin)
        
    def _set_state_(self,state):
        """Setup the GPIO Pin"""
        GPIO.setup(self.pin, GPIO.OUT)
        if state.lower() == 'on' or state == True:
            GPIO.output(self.pin, GPIO.LOW)
        elif state.lower() == 'off' or state == False:
            GPIO.output(self.pin, GPIO.HIGH)
        else:
            print("Error, '{}' is not a good state".format(state))

    def  __str__(self):
        return "Relay: GPIO {}[{}}: state {}".format(self.pin, self.name, self._get_state_())

    state = property(_get_state_, _set_state_)

