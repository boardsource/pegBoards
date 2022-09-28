# auto generated
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.GP26, board.GP27, board.GP28)
    col_pins = (board.GP21, board.GP23, board.GP20, board.GP22)
    diode_orientation = DiodeOrientation.COLUMNS
    i2c = board.I2C
