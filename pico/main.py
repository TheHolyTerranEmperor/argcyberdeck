import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


#pinouts and assigning GPIO (assigning rows and cols)
COL_PINS = (board.GP0, board.GP1, board.GP2)
ROW_PINS = (board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)

#Keycodes for buttons

KEYCODES = (
    Keycode.SEVEN, Keycode.EIGHT, Keycode.NINE
    Keycode.FOUR, Keycode.FIVE, Keycode.SIX,
    Keycode.ONE, Keycode.TWO, Keycode.THREE,
    Keycode.KEYPAD_ASTERISK, Keycode.ZERO, Keycode.POUND
    Keycode.W, Keycode.S, Keycode.T, 
    Keycode.A, Keycode.D, Keycode.G
)
keys = keypad.KeyMatrix(ROW_PINS, COL_PINS)

kbd = Keyboard(usb_hid.devices)

while True:
    event = keys.events.get()
    if event:
        key_number = event.key_number
        if event.pressed:
            kbd.press(KEYCODES[key_number])
        if event.released:
            kbd.release(KEYCODES[key_number])
