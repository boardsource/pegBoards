# auto generated
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.TX,board.RX,board.SDA,board.SCL)
    col_pins = (
        board.GP29,
        board.GP28,
        board.GP27,
        board.GP26,
        board.GP22,
        board.GP20,
        board.GP23,
        board.GP21,
        board.GP09,
        board.GP08,
        board.GP07,
        board.GP06

    )
    diode_orientation = DiodeOrientation.COLUMNS
    brightness_limit = 0.6
    num_pixels = 58
    rgb_pixel_pin = board.GP05
    led_key_pos =[10,11,12,13,14,15,16,17,18,19,20,21,
                 22,23,24,25,26,27,28,29,30,31,32,33,
                 34,35,36,37,38,39,40,41,42,43,44,45,
                 46,47,48,49,50,51,52,53,54,55,56,57,
                 0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ]
