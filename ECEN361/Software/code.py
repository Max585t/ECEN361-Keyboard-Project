import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string
import digitalio

redox_l = KMKKeyboard()

#redox_l.debug_enabled = True
redox_l.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
redox_l.row_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)
redox_l.diode_orientation = DiodeOrientation.COLUMNS

redox_l.split_type = "UART"
redox_l.uart_pin = (board.GP0, board.GP1) # Must include this to get pico uart to work. kmk_keyboard.py lines 172, 174 changed from ...x=pin, to x=pin[0 or 1]
redox_l.split_flip = True
redox_l.split_offsets = [7, 7, 7, 7, 7]

qt_strg = send_string("quit()")

redox_l.keymap = [
    # Qwerty
    #     ,------------------------------------------------.               ,------------------------------------------------. 
    #     |  esc |   1  |   2  |   3  |   4  |   5  |delete|               |delete|   6  |   7  |   8  |   9  |   0  |  fn  |
    #     |------+------+------+------+------+------+------|               |------+------+------+------+------+------+------|
    #     | tab  |   Q  |   W  |   E  |   R  |   T  |  esc |               | rclck|   Y  |   U  |   I  |   O  |   P  |bckspc|
    #     |------+------+------+------+------+-------------|               |------+------+------+------+------+-------------|
    #     | ctrl |   A  |   S  |   D  |   F  |   G  |  {[  |               | -_   |   H  |   J  |   K  |   L  |   :  |  \|  |
    #     |------+------+------+------+------+------|------|               |------+------+------+------+------+------|------|
    #     | Shift|   Z  |   X  |   C  |   V  |   B  |  }]  |               | +=   |   N  |   M  |  ,<  |  .>  |  ?/  |Shift |
    #     |------+------+------+------+------+------+------|               |------+------+------+------+------+------+------|
    #     | caps |  gui |  alt |tilde |space |bacspc|play  |               | ctrl |  gui |Space |arrowL|arrowD|arrowU|arrowR|
    #     `------------------------------------------------'               `------------------------------------------------'
    [
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,           KC.N5,   KC.DEL,             KC.N6,         KC.N7,    KC.N8,    KC.N9,    KC.N0,   KC.MINS,  KC.BSPC,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,            KC.T,    KC.LALT(KC.A),      KC.LALT(KC.V), KC.Y,     KC.U,     KC.I,     KC.O,    KC.P,     KC.BSLS,
        KC.LCTL,  KC.A,    KC.S,    KC.D,    KC.F,            KC.G,    KC.LBRC,            KC.QUOT,       KC.H,     KC.J,     KC.K,     KC.L,    KC.SCLN,  KC.ENT,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,            KC.B,    KC.RBRC,            KC.EQL,        KC.N,     KC.M,     KC.COMM,  KC.DOT,  KC.SLSH,  KC.MO(1),
        KC.CAPS,  KC.LALT, KC.GRV,  KC.MNU,  KC.LALT(KC.TAB), KC.SPC,  qt_strg,            KC.ENT,        KC.SPC,   KC.RGUI,  KC.LEFT,  KC.DOWN, KC.UP,    KC.RGHT,
    ],
    [
        KC.TRNS,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F12,       KC.F6,     KC.F7,    KC.F8,   KC.F9,    KC.F10,  KC.F11,   KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,      KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,      KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,      KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS,  KC.MO(0),
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,      KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS,  KC.TRNS,
    ],
]

if __name__ == '__main__':
    led = digitalio.DigitalInOut(board.GP15)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True
    redox_l.go()