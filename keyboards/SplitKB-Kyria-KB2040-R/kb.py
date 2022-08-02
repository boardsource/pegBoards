import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.A3,
        board.A2,
        board.A1,
        board.A0,
        board.SCK,
        board.MISO,
        board.MOSI,
        board.D10,
    )
    row_pins = (board.D8, board.D7, board.D6, board.D4)
    diode_orientation = DiodeOrientation.COL2ROW
    data_pin = board.D1
    rgb_pixel_pin = board.D0
    SCL = board.D3
    SDA = board.D2
    encoder_pin_0 = board.D9
    encoder_pin_1 = board.D5

    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,  5,                     37, 36, 35, 34, 33, 32,
         8,  9, 10, 11, 12, 13,                     45, 44, 43, 42, 41, 40,
        16, 17, 18, 19, 20, 21, 22, 23,     55, 54, 53, 52, 51, 50, 49, 48,
                    27, 28, 29, 30, 31,     63, 62, 61, 60, 59
    ]
    # fmt: on
