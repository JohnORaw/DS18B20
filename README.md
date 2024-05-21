# DS18B20
Use DS18B20 temperature sensors with RPi.

This repo includes simple demo code based on code by Scott Campbell, Circuit Basics.
Enable 1W interface in RPi config and reboot.

The image below shows DS18B20 based temperature sensor wired into a CM4 IO Board. It also shows a BME280 (dfifferent project!).
These are one-wire temperature sensors.
Red and Black are power, seems to be fine with 5VDC or 3V3.
A 4.7kΩ resistor bridges between Vcc and the Yellow wires (signal).
I have connected up to 6 of these to a RPi Zero without problems.

<img title="DS18B20 on CM4" alt="DS18B20" src="/images/DS18B20.jpg">


