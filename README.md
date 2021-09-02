# ECEN361-Keyboard-Project
![20210401_210549](https://user-images.githubusercontent.com/59662034/113489899-1858d180-9484-11eb-8efd-6420d04b1416.jpg)
This project is built on top of Redox by Mattia Dal Ben (https://github.com/mattdibi/redox-keyboard) and KMK by @klardotsh and @kdb424 (https://github.com/KMKfw/kmk_firmware)

## Code
The code I wrote for this project can be found in code.py. This file is what the circuitpython device (Pi Pico in this case) actually runs.

## Modifications
For this project, I had to make modifications to both Redox and KMK. Here are my changes to the Redox base plate.

![Screenshot 2021-04-03 131714](https://user-images.githubusercontent.com/59662034/113489232-476d4400-9480-11eb-85e8-7752f72356e7.png)

Here are the changes I made to KMK

Original:
```python
#led.py
import pulseio
...
self.led = pulseio.PWMOut(led_pin)

#kmk_keyboard.py
def init_uart(self, pin, timeout=20):
  if self.is_target:
    return busio.UART(tx=None, rx=pin, timeout=timeout)
  else:
    return busio.UART(tx=pin, rx=None, timeout=timeout)
```
Mine:
```python
#led.py
import pwmio
...
self.led = pwmio.PWMOut(led_pin)
    
#kmk_keyboard.py
def init_uart(self, pin, timeout=20):
  if self.is_target:
    return busio.UART(tx=None, rx=pin[1], timeout=timeout)
  else:
    return busio.UART(tx=pin[0], rx=None, timeout=timeout)
```

## Schematic
![Keyboard Schematic](https://user-images.githubusercontent.com/59662034/113489465-b008f080-9481-11eb-91b7-ec0e60d2d66d.png)
It is important to note that the GND pin on the USB breakout board be connected directly to TP1 and not any of the Pico's other GND pins. If USB ground is not connected to TP1, USB type C will not work. 
Also, the even though the diodes are on the rows, they must be defined in KMK as being on columns. This is because the diode orientation used in the circuit is for pulling pins low, but KMK pulls its pins high. 

## Pictures
![20210403_134713](https://user-images.githubusercontent.com/59662034/113489881-037c3e00-9484-11eb-957b-8990d6eb3983.jpg)
![20210403_134805](https://user-images.githubusercontent.com/59662034/113489884-070fc500-9484-11eb-9b45-03687a35145e.jpg)
![20210403_135133](https://user-images.githubusercontent.com/59662034/113489887-08d98880-9484-11eb-9896-abe366d6e344.jpg)
note: final base plate not shown
![20210403_134835](https://user-images.githubusercontent.com/59662034/113489890-0a0ab580-9484-11eb-9f34-e0ed75f33ec4.jpg)

