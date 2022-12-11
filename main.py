import serial  # Serial imported for Serial communication
import time  # Required to use delay functions
import pyautogui


# Create Serial port object called arduinoSerialData
ArduinoSerial = serial.Serial('/dev/cu.usbserial-1120', 9600)

time.sleep(2)  # wait for 2 seconds for the communication to get established


while 1:

    # read the serial data and print it as line
    incoming = str(ArduinoSerial.readline())

    print(incoming)

    if 'Play/Pause' in incoming:

        pyautogui.press(['space'])

    if 'Rewind' in incoming:

        pyautogui.press('left')

    if 'Forward' in incoming:

        pyautogui.hotkey('right')

    if 'Vup' in incoming:

        pyautogui.hotkey('ctrl', 'down')

    if 'Vdown' in incoming:

        pyautogui.hotkey('ctrl', 'up')

    incoming = ""
