# auto generated
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP04,
        board.GP05,
        board.GP06,
        board.GP07,
        board.GP08,
        board.GP09,
        board.GP22,
        board.GP20,
        board.GP23,
        board.GP21
    )

    row_pins = (
        board.GP29,
        board.GP28,
        board.GP27,
        board.GP26,

    )

    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.TX
    rgb_num_pixels = 11
    i2c = board.I2C
    led_key_pos = [1,0,9,8,2,7,10,3,6,5,4]
    brightness_limit = 1.0
    num_pixels = 11
    coord_mapping = [0,  1,  2,  3,  4,  6,  7,  8,  9, 36,
                     10, 11, 12, 13, 14, 16, 17, 18, 19, 37,
                     20, 21, 22, 23, 24, 26, 27, 28, 29, 38,
                             32,33,34,39
                   ]
