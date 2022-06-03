# auto generated
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.RX, board.TX, board.SDA, board.SCL)
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
        board.GP06,
    )
    diode_orientation = DiodeOrientation.COLUMNS
    i2c = board.I2C
