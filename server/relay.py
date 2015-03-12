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
    
    def __init__(self, pin, name="", default_state=False):
        """Set the relay"""
        self.name = name
        self.pin = pin
        self.state = default_state
        GPIO.setup(self.pin, GPIO.OUT)
        self.on() if self.state else self.off()
        
    def on(self):
        """Setup the GPIO Pin"""
        print("Set {} to on".format(self.pin))
        self.state = True
        GPIO.output(self.pin, GPIO.LOW)
        
    def off(self):
        """Setup the GPIO Pin"""
        print("Set {} to off".format(self.pin))
        self.state = False
        GPIO.output(self.pin, GPIO.HIGH)
        
    def  __repr__(self):
        return "relay : ['pin': {}, 'name': {}, 'state': {}]".format(
                self.pin,
                self.name,
                self.state)


