# auto generated
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP27,
        board.GP26,
        board.GP22,
        board.GP20,
        board.GP23,
        board.GP21,
    )
    row_pins = (board.GP05, board.GP06, board.GP07, board.GP08, board.GP09)
    diode_orientation = DiodeOrientation.COLUMNS
    uart_pin = board.RX
    rgb_pixel_pin = board.TX
    data_pin = board.RX
    i2c = board.I2C
    SCL=board.SCL
    SDA=board.SDA

    # flake8: noqa
    coord_mapping = [
     0,  1,  2,  3,  4,  5,  36, 35, 34, 33, 32, 31,
     6,  7,  8,  9, 10, 11,  42, 41, 40, 39, 38, 37,
    12, 13, 14, 15, 16, 17,  48, 47, 46, 45, 44, 43,
    18, 19, 20, 21, 22, 23,  54, 53, 52, 51, 50, 49,
        26, 27, 28, 29, 30,  60, 59, 58, 57, 56,
    ]
