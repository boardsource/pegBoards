import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner

class KMKKeyboard(_KMKKeyboard):
	def __init__(self):
        # create and register the scanner
        self.matrix =[MatrixScanner(
            # required arguments:
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            # optional arguments with defaults:
            columns_to_anodes=DiodeOrientation.COL2ROW,
            interval=0.02,
            max_events=64
        ),
        RotaryioEncoder(
            pin_a=board.GP07,
            pin_b=board.GP23,
            # optional
            divisor=4,
        )]
    col_pins = (board.GP04, board.GP06, board.GP20, board.GP26, board.GP27)
    row_pins = (board.GP29, board.RX, board.GP05, board.GP22)
    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = board.TX
    rgb_pixel_pin = board.GP09
    i2c = board.I2C
    SCL=board.SCL
    SDA=board.SDA
    brightness_limit = 1.0
    num_pixels = 44
    led_key_pos = [ 17,16,15,14,13,     35,36,37,38,39,
                    8, 9, 10,11,12,     34,33,32,31,30,
                    7, 6, 5, 4, 3 ,     25,26,27,28,29,
                          0, 1, 2,      24,23,22,
                        18,19,20,21, 43,42,41,40]

    # NOQA
    # flake8: noqa
    coord_mapping = [
     0,  1,  2,  3,  4,  22, 23, 24, 25, 26,
     5,  6,  7,  8,  9,  27, 28, 29, 30, 31,
    10, 11, 12, 13, 14,  32, 33, 34, 35, 36,
            17, 18, 19,  37, 38, 39,
			20,21,40,41
    ]